# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TempSensorMock.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='TempSensorMock.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14TempSensorMock.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xd0\x02\n\x0eTempSensorMock\x12-\n\x05value\x18\x01 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x8a\xb5\x18\x02(\x01\x92?\x02\x38 \x12\x19\n\tconnected\x18\x03 \x01(\x08\x42\x06\x8a\xb5\x18\x02\x30\x01\x12#\n\x07setting\x18\x04 \x01(\x11\x42\x12\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x36\n\x0c\x66luctuations\x18\x05 \x03(\x0b\x32 .blox.TempSensorMock.Fluctuation\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x01\x1a^\n\x0b\x46luctuation\x12+\n\tamplitude\x18\x01 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\"\n\x06period\x18\x02 \x01(\rB\x12\x8a\xb5\x18\x02\x08\x03\x8a\xb5\x18\x03\x10\xe8\x07\x92?\x02\x38 :\r\x8a\xb5\x18\x03\x18\xad\x02\x8a\xb5\x18\x02H\x02\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_TEMPSENSORMOCK_FLUCTUATION = _descriptor.Descriptor(
  name='Fluctuation',
  full_name='blox.TempSensorMock.Fluctuation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amplitude', full_name='blox.TempSensorMock.Fluctuation.amplitude', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\006\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='blox.TempSensorMock.Fluctuation.period', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\212\265\030\003\020\350\007\222?\0028 ', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=382,
)

_TEMPSENSORMOCK = _descriptor.Descriptor(
  name='TempSensorMock',
  full_name='blox.TempSensorMock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.TempSensorMock.value', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \212\265\030\002(\001\222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connected', full_name='blox.TempSensorMock.connected', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.TempSensorMock.setting', index=2,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fluctuations', full_name='blox.TempSensorMock.fluctuations', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.TempSensorMock.strippedFields', index=4,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\222?\002\020\001', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TEMPSENSORMOCK_FLUCTUATION, ],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\003\030\255\002\212\265\030\002H\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=397,
)

_TEMPSENSORMOCK_FLUCTUATION.containing_type = _TEMPSENSORMOCK
_TEMPSENSORMOCK.fields_by_name['fluctuations'].message_type = _TEMPSENSORMOCK_FLUCTUATION
DESCRIPTOR.message_types_by_name['TempSensorMock'] = _TEMPSENSORMOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TempSensorMock = _reflection.GeneratedProtocolMessageType('TempSensorMock', (_message.Message,), {

  'Fluctuation' : _reflection.GeneratedProtocolMessageType('Fluctuation', (_message.Message,), {
    'DESCRIPTOR' : _TEMPSENSORMOCK_FLUCTUATION,
    '__module__' : 'TempSensorMock_pb2'
    # @@protoc_insertion_point(class_scope:blox.TempSensorMock.Fluctuation)
    })
  ,
  'DESCRIPTOR' : _TEMPSENSORMOCK,
  '__module__' : 'TempSensorMock_pb2'
  # @@protoc_insertion_point(class_scope:blox.TempSensorMock)
  })
_sym_db.RegisterMessage(TempSensorMock)
_sym_db.RegisterMessage(TempSensorMock.Fluctuation)


_TEMPSENSORMOCK_FLUCTUATION.fields_by_name['amplitude']._options = None
_TEMPSENSORMOCK_FLUCTUATION.fields_by_name['period']._options = None
_TEMPSENSORMOCK.fields_by_name['value']._options = None
_TEMPSENSORMOCK.fields_by_name['connected']._options = None
_TEMPSENSORMOCK.fields_by_name['setting']._options = None
_TEMPSENSORMOCK.fields_by_name['strippedFields']._options = None
_TEMPSENSORMOCK._options = None
# @@protoc_insertion_point(module_scope)
