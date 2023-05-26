# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/peer/snapshot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from hfc.protos.common import common_pb2 as hfc_dot_protos_dot_common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/peer/snapshot.proto',
  package='protos',
  syntax='proto3',
  serialized_options=b'\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peer',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ehfc/protos/peer/snapshot.proto\x12\x06protos\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1ehfc/protos/common/common.proto\"n\n\x0fSnapshotRequest\x12\x31\n\x10signature_header\x18\x01 \x01(\x0b\x32\x17.common.SignatureHeader\x12\x12\n\nchannel_id\x18\x02 \x01(\t\x12\x14\n\x0c\x62lock_number\x18\x03 \x01(\x04\"V\n\rSnapshotQuery\x12\x31\n\x10signature_header\x18\x01 \x01(\x0b\x32\x17.common.SignatureHeader\x12\x12\n\nchannel_id\x18\x02 \x01(\t\";\n\x15SignedSnapshotRequest\x12\x0f\n\x07request\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"6\n\x1dQueryPendingSnapshotsResponse\x12\x15\n\rblock_numbers\x18\x01 \x03(\x04\x32\xeb\x01\n\x08Snapshot\x12\x43\n\x08Generate\x12\x1d.protos.SignedSnapshotRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x06\x43\x61ncel\x12\x1d.protos.SignedSnapshotRequest\x1a\x16.google.protobuf.Empty\"\x00\x12W\n\rQueryPendings\x12\x1d.protos.SignedSnapshotRequest\x1a%.protos.QueryPendingSnapshotsResponse\"\x00\x42R\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,hfc_dot_protos_dot_common_dot_common__pb2.DESCRIPTOR,])




_SNAPSHOTREQUEST = _descriptor.Descriptor(
  name='SnapshotRequest',
  full_name='protos.SnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_header', full_name='protos.SnapshotRequest.signature_header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='protos.SnapshotRequest.channel_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='block_number', full_name='protos.SnapshotRequest.block_number', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=103,
  serialized_end=213,
)


_SNAPSHOTQUERY = _descriptor.Descriptor(
  name='SnapshotQuery',
  full_name='protos.SnapshotQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_header', full_name='protos.SnapshotQuery.signature_header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='protos.SnapshotQuery.channel_id', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=301,
)


_SIGNEDSNAPSHOTREQUEST = _descriptor.Descriptor(
  name='SignedSnapshotRequest',
  full_name='protos.SignedSnapshotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='protos.SignedSnapshotRequest.request', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='protos.SignedSnapshotRequest.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=303,
  serialized_end=362,
)


_QUERYPENDINGSNAPSHOTSRESPONSE = _descriptor.Descriptor(
  name='QueryPendingSnapshotsResponse',
  full_name='protos.QueryPendingSnapshotsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_numbers', full_name='protos.QueryPendingSnapshotsResponse.block_numbers', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=364,
  serialized_end=418,
)

_SNAPSHOTREQUEST.fields_by_name['signature_header'].message_type = hfc_dot_protos_dot_common_dot_common__pb2._SIGNATUREHEADER
_SNAPSHOTQUERY.fields_by_name['signature_header'].message_type = hfc_dot_protos_dot_common_dot_common__pb2._SIGNATUREHEADER
DESCRIPTOR.message_types_by_name['SnapshotRequest'] = _SNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['SnapshotQuery'] = _SNAPSHOTQUERY
DESCRIPTOR.message_types_by_name['SignedSnapshotRequest'] = _SIGNEDSNAPSHOTREQUEST
DESCRIPTOR.message_types_by_name['QueryPendingSnapshotsResponse'] = _QUERYPENDINGSNAPSHOTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SnapshotRequest = _reflection.GeneratedProtocolMessageType('SnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTREQUEST,
  '__module__' : 'hfc.protos.peer.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:protos.SnapshotRequest)
  })
_sym_db.RegisterMessage(SnapshotRequest)

SnapshotQuery = _reflection.GeneratedProtocolMessageType('SnapshotQuery', (_message.Message,), {
  'DESCRIPTOR' : _SNAPSHOTQUERY,
  '__module__' : 'hfc.protos.peer.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:protos.SnapshotQuery)
  })
_sym_db.RegisterMessage(SnapshotQuery)

SignedSnapshotRequest = _reflection.GeneratedProtocolMessageType('SignedSnapshotRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDSNAPSHOTREQUEST,
  '__module__' : 'hfc.protos.peer.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:protos.SignedSnapshotRequest)
  })
_sym_db.RegisterMessage(SignedSnapshotRequest)

QueryPendingSnapshotsResponse = _reflection.GeneratedProtocolMessageType('QueryPendingSnapshotsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPENDINGSNAPSHOTSRESPONSE,
  '__module__' : 'hfc.protos.peer.snapshot_pb2'
  # @@protoc_insertion_point(class_scope:protos.QueryPendingSnapshotsResponse)
  })
_sym_db.RegisterMessage(QueryPendingSnapshotsResponse)


DESCRIPTOR._options = None

_SNAPSHOT = _descriptor.ServiceDescriptor(
  name='Snapshot',
  full_name='protos.Snapshot',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=421,
  serialized_end=656,
  methods=[
  _descriptor.MethodDescriptor(
    name='Generate',
    full_name='protos.Snapshot.Generate',
    index=0,
    containing_service=None,
    input_type=_SIGNEDSNAPSHOTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Cancel',
    full_name='protos.Snapshot.Cancel',
    index=1,
    containing_service=None,
    input_type=_SIGNEDSNAPSHOTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='QueryPendings',
    full_name='protos.Snapshot.QueryPendings',
    index=2,
    containing_service=None,
    input_type=_SIGNEDSNAPSHOTREQUEST,
    output_type=_QUERYPENDINGSNAPSHOTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SNAPSHOT)

DESCRIPTOR.services_by_name['Snapshot'] = _SNAPSHOT

# @@protoc_insertion_point(module_scope)
