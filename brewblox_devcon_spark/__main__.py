"""
Example of how to import and use the brewblox service
"""

from brewblox_service import service

from brewblox_devcon_spark import api, brewblox_logger, device, broadcaster

LOGGER = brewblox_logger(__name__)


def create_parser(default_name='spark'):
    parser = service.create_parser(default_name='spark')
    parser.add_argument('--database',
                        help='Backing file for the object database. [%(default)s]',
                        default='brewblox_db.json')
    parser.add_argument('--system-database',
                        help='Backing file for the system object database. [%(default)s]',
                        default='brewblox_sys_db.json')
    parser.add_argument('--device-port',
                        help='Spark device port. Automatically determined if not set. [%(default)s]')
    parser.add_argument('--device-id',
                        help='Spark serial number. Any spark is valid if not set. '
                        'This will be ignored if --device-port is specified. [%(default)s]')
    parser.add_argument('--simulation',
                        help='Start in simulator mode. Will not connect to a physical device. [%(default)s]',
                        action='store_true')
    parser.add_argument('--broadcast-interval',
                        help='Interval (in seconds) between broadcasts of controller state. [%(default)s]',
                        type=int,
                        default=5)
    return parser


def main():
    app = service.create_app(parser=create_parser())

    device.setup(app)
    api.setup(app)
    broadcaster.setup(app)

    service.furnish(app)

    # service.run() will start serving clients async
    service.run(app)


if __name__ == '__main__':
    main()
