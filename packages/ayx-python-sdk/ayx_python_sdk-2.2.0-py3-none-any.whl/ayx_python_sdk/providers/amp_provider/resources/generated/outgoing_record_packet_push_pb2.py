# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: outgoing_record_packet_push.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import record_packet_pb2 as record__packet__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!outgoing_record_packet_push.proto\x12\x03sdk\x1a\x13record_packet.proto\"Y\n\x18OutgoingRecordPacketPush\x12\x13\n\x0b\x61nchor_name\x18\x01 \x01(\t\x12(\n\rrecord_packet\x18\x02 \x01(\x0b\x32\x11.sdk.RecordPacketb\x06proto3')



_OUTGOINGRECORDPACKETPUSH = DESCRIPTOR.message_types_by_name['OutgoingRecordPacketPush']
OutgoingRecordPacketPush = _reflection.GeneratedProtocolMessageType('OutgoingRecordPacketPush', (_message.Message,), {
  'DESCRIPTOR' : _OUTGOINGRECORDPACKETPUSH,
  '__module__' : 'outgoing_record_packet_push_pb2'
  # @@protoc_insertion_point(class_scope:sdk.OutgoingRecordPacketPush)
  })
_sym_db.RegisterMessage(OutgoingRecordPacketPush)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OUTGOINGRECORDPACKETPUSH._serialized_start=63
  _OUTGOINGRECORDPACKETPUSH._serialized_end=152
# @@protoc_insertion_point(module_scope)
