# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='notification.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x12notification.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe6\x01\n\x0cNotification\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\ndelete_all\x18\x03 \x01(\x08\x12\x0f\n\x07\x64\x65letes\x18\x04 \x03(\x0c\x12%\n\x07updates\x18\x05 \x03(\x0b\x32\x14.Notification.Update\x12\x10\n\x08retracts\x18\x06 \x03(\x0c\x12\x15\n\rpath_elements\x18\x07 \x03(\x0c\x1a$\n\x06Update\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"%\n\x07\x44\x61taset\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"_\n\x11NotificationBatch\x12\t\n\x01\x64\x18\x01 \x01(\t\x12$\n\rnotifications\x18\x02 \x03(\x0b\x32\r.Notification\x12\x19\n\x07\x64\x61taset\x18\x03 \x01(\x0b\x32\x08.DatasetB\x05Z\x03genb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_NOTIFICATION_UPDATE = _descriptor.Descriptor(
  name='Update',
  full_name='Notification.Update',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Notification.Update.key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Notification.Update.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=286,
)

_NOTIFICATION = _descriptor.Descriptor(
  name='Notification',
  full_name='Notification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Notification.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='Notification.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_all', full_name='Notification.delete_all', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deletes', full_name='Notification.deletes', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updates', full_name='Notification.updates', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='retracts', full_name='Notification.retracts', index=5,
      number=6, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path_elements', full_name='Notification.path_elements', index=6,
      number=7, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NOTIFICATION_UPDATE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=286,
)


_DATASET = _descriptor.Descriptor(
  name='Dataset',
  full_name='Dataset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Dataset.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dataset.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=325,
)


_NOTIFICATIONBATCH = _descriptor.Descriptor(
  name='NotificationBatch',
  full_name='NotificationBatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='d', full_name='NotificationBatch.d', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='notifications', full_name='NotificationBatch.notifications', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='NotificationBatch.dataset', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=327,
  serialized_end=422,
)

_NOTIFICATION_UPDATE.containing_type = _NOTIFICATION
_NOTIFICATION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_NOTIFICATION.fields_by_name['updates'].message_type = _NOTIFICATION_UPDATE
_NOTIFICATIONBATCH.fields_by_name['notifications'].message_type = _NOTIFICATION
_NOTIFICATIONBATCH.fields_by_name['dataset'].message_type = _DATASET
DESCRIPTOR.message_types_by_name['Notification'] = _NOTIFICATION
DESCRIPTOR.message_types_by_name['Dataset'] = _DATASET
DESCRIPTOR.message_types_by_name['NotificationBatch'] = _NOTIFICATIONBATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Notification = _reflection.GeneratedProtocolMessageType('Notification', (_message.Message,), dict(

  Update = _reflection.GeneratedProtocolMessageType('Update', (_message.Message,), dict(
    DESCRIPTOR = _NOTIFICATION_UPDATE,
    __module__ = 'notification_pb2'
    # @@protoc_insertion_point(class_scope:Notification.Update)
    ))
  ,
  DESCRIPTOR = _NOTIFICATION,
  __module__ = 'notification_pb2'
  # @@protoc_insertion_point(class_scope:Notification)
  ))
_sym_db.RegisterMessage(Notification)
_sym_db.RegisterMessage(Notification.Update)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), dict(
  DESCRIPTOR = _DATASET,
  __module__ = 'notification_pb2'
  # @@protoc_insertion_point(class_scope:Dataset)
  ))
_sym_db.RegisterMessage(Dataset)

NotificationBatch = _reflection.GeneratedProtocolMessageType('NotificationBatch', (_message.Message,), dict(
  DESCRIPTOR = _NOTIFICATIONBATCH,
  __module__ = 'notification_pb2'
  # @@protoc_insertion_point(class_scope:NotificationBatch)
  ))
_sym_db.RegisterMessage(NotificationBatch)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003gen'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
