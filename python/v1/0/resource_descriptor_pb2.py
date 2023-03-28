# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1.0/resource_descriptor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1.0/resource_descriptor.proto',
  package='io.in_toto.attestation.v1_0',
  syntax='proto3',
  serialized_options=b'Z+github.com/in-toto/attestation/go/spec/v1.0',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ev1.0/resource_descriptor.proto\x12\x1bio.in_toto.attestation.v1_0\x1a\x1cgoogle/protobuf/struct.proto\"\x8d\x03\n\x12ResourceDescriptor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12K\n\x06\x64igest\x18\x03 \x03(\x0b\x32;.io.in_toto.attestation.v1_0.ResourceDescriptor.DigestEntry\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\x0c\x12\x18\n\x10\x64ownloadLocation\x18\x05 \x01(\t\x12\x11\n\tmediaType\x18\x06 \x01(\t\x12U\n\x0b\x61nnotations\x18\x07 \x03(\x0b\x32@.io.in_toto.attestation.v1_0.ResourceDescriptor.AnnotationsEntry\x1a-\n\x0b\x44igestEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aK\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01\x42-Z+github.com/in-toto/attestation/go/spec/v1.0b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_RESOURCEDESCRIPTOR_DIGESTENTRY = _descriptor.Descriptor(
  name='DigestEntry',
  full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.DigestEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.DigestEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.DigestEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=414,
)

_RESOURCEDESCRIPTOR_ANNOTATIONSENTRY = _descriptor.Descriptor(
  name='AnnotationsEntry',
  full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.AnnotationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.AnnotationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.AnnotationsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=491,
)

_RESOURCEDESCRIPTOR = _descriptor.Descriptor(
  name='ResourceDescriptor',
  full_name='io.in_toto.attestation.v1_0.ResourceDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digest', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.digest', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.content', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='downloadLocation', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.downloadLocation', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mediaType', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.mediaType', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='io.in_toto.attestation.v1_0.ResourceDescriptor.annotations', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_RESOURCEDESCRIPTOR_DIGESTENTRY, _RESOURCEDESCRIPTOR_ANNOTATIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=491,
)

_RESOURCEDESCRIPTOR_DIGESTENTRY.containing_type = _RESOURCEDESCRIPTOR
_RESOURCEDESCRIPTOR_ANNOTATIONSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_RESOURCEDESCRIPTOR_ANNOTATIONSENTRY.containing_type = _RESOURCEDESCRIPTOR
_RESOURCEDESCRIPTOR.fields_by_name['digest'].message_type = _RESOURCEDESCRIPTOR_DIGESTENTRY
_RESOURCEDESCRIPTOR.fields_by_name['annotations'].message_type = _RESOURCEDESCRIPTOR_ANNOTATIONSENTRY
DESCRIPTOR.message_types_by_name['ResourceDescriptor'] = _RESOURCEDESCRIPTOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceDescriptor = _reflection.GeneratedProtocolMessageType('ResourceDescriptor', (_message.Message,), {

  'DigestEntry' : _reflection.GeneratedProtocolMessageType('DigestEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESOURCEDESCRIPTOR_DIGESTENTRY,
    '__module__' : 'v1.0.resource_descriptor_pb2'
    # @@protoc_insertion_point(class_scope:io.in_toto.attestation.v1_0.ResourceDescriptor.DigestEntry)
    })
  ,

  'AnnotationsEntry' : _reflection.GeneratedProtocolMessageType('AnnotationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _RESOURCEDESCRIPTOR_ANNOTATIONSENTRY,
    '__module__' : 'v1.0.resource_descriptor_pb2'
    # @@protoc_insertion_point(class_scope:io.in_toto.attestation.v1_0.ResourceDescriptor.AnnotationsEntry)
    })
  ,
  'DESCRIPTOR' : _RESOURCEDESCRIPTOR,
  '__module__' : 'v1.0.resource_descriptor_pb2'
  # @@protoc_insertion_point(class_scope:io.in_toto.attestation.v1_0.ResourceDescriptor)
  })
_sym_db.RegisterMessage(ResourceDescriptor)
_sym_db.RegisterMessage(ResourceDescriptor.DigestEntry)
_sym_db.RegisterMessage(ResourceDescriptor.AnnotationsEntry)


DESCRIPTOR._options = None
_RESOURCEDESCRIPTOR_DIGESTENTRY._options = None
_RESOURCEDESCRIPTOR_ANNOTATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
