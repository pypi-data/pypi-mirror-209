# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/data/summary.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.data import fco_metadata_pb2 as tecton__proto_dot_data_dot_fco__metadata__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftecton_proto/data/summary.proto\x12\x11tecton_proto.data\x1a$tecton_proto/data/fco_metadata.proto\"\xcd\x01\n\x0bSummaryItem\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\x12\x14\n\x05value\x18\x03 \x01(\tR\x05value\x12!\n\x0cmulti_values\x18\x04 \x03(\tR\x0bmultiValues\x12P\n\x14nested_summary_items\x18\x05 \x03(\x0b\x32\x1e.tecton_proto.data.SummaryItemR\x12nestedSummaryItems\"\x94\x01\n\nFcoSummary\x12\x41\n\x0c\x66\x63o_metadata\x18\x01 \x01(\x0b\x32\x1e.tecton_proto.data.FcoMetadataR\x0b\x66\x63oMetadata\x12\x43\n\rsummary_items\x18\x02 \x03(\x0b\x32\x1e.tecton_proto.data.SummaryItemR\x0csummaryItemsB\x13\n\x0f\x63om.tecton.dataP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.data.summary_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.dataP\001'
  _SUMMARYITEM._serialized_start=93
  _SUMMARYITEM._serialized_end=298
  _FCOSUMMARY._serialized_start=301
  _FCOSUMMARY._serialized_end=449
# @@protoc_insertion_point(module_scope)
