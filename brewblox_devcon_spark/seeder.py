"""
Regulates actions that should be taken when the service connects to a controller.
"""


import asyncio
import warnings
from datetime import datetime

from aiohttp import web
from brewblox_service import brewblox_logger, features, scheduler

from brewblox_devcon_spark import datastore, status
from brewblox_devcon_spark.api import object_api
from brewblox_devcon_spark.codec import codec

LOGGER = brewblox_logger(__name__)


def setup(app: web.Application):
    features.add(app, Seeder(app))


def get_seeder(app: web.Application):
    return features.get(app, Seeder)


class Seeder(features.ServiceFeature):

    def __init__(self, app: web.Application):
        super().__init__(app)

        self._config = app['config']
        self._task: asyncio.Task = None

    async def startup(self, app: web.Application):
        await self.shutdown(app)
        self._task = await scheduler.create_task(app, self._seed())

    async def shutdown(self, _):
        await scheduler.cancel_task(self.app, self._task)
        self._task = None

    async def _seed(self):
        spark_status = status.get_status(self.app)

        while True:
            spark_status.seeded.clear()
            await spark_status.connected.wait()
            await self._seed_datastore()
            await self._seed_time()
            spark_status.seeded.set()
            await spark_status.disconnected.wait()

    ##########

    async def _seed_datastore(self):
        try:
            app_name = self.app['config']['name']
            await asyncio.gather(
                datastore.get_datastore(self.app).read(f'{app_name}-blocks-db'),
                datastore.get_config(self.app).read(f'{app_name}-config-db'),
            )

            codec.get_codec(self.app).update_unit_config()

        except Exception as ex:  # pragma: no cover
            warnings.warn(f'Failed to seed datastore - {type(ex).__name__}({ex})')

    async def _seed_time(self):
        try:
            now = datetime.now()
            api = object_api.ObjectApi(self.app)
            await api.write(
                input_id=datastore.TIME_CONTROLLER_ID,
                profiles=[i for i in range(8)],
                input_type='Ticks',
                input_data={
                    'secondsSinceEpoch': now.timestamp()
                })

        except Exception as ex:  # pragma: no cover
            warnings.warn(f'Failed to seed controller time - {type(ex).__name__}({ex})')
