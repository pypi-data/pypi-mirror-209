# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/online_store_writer/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.canary import type_pb2 as tecton__proto_dot_canary_dot_type__pb2
from tecton_proto.data import feature_view_pb2 as tecton__proto_dot_data_dot_feature__view__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-tecton_proto/online_store_writer/config.proto\x12 tecton_proto.online_store_writer\x1a\x1etecton_proto/canary/type.proto\x1a$tecton_proto/data/feature_view.proto\"\x95\x03\n\x1eOnlineStoreWriterConfiguration\x12*\n\x11status_table_name\x18\x01 \x01(\tR\x0fstatusTableName\x12&\n\x0f\x64\x61ta_table_name\x18\x02 \x01(\tR\rdataTableName\x12*\n\x11\x63\x61nary_table_name\x18\x03 \x01(\tR\x0f\x63\x61naryTableName\x12@\n\x0b\x63\x61nary_type\x18\x04 \x01(\x0e\x32\x1f.tecton_proto.canary.CanaryTypeR\ncanaryType\x12\x1b\n\tcanary_id\x18\x05 \x01(\tR\x08\x63\x61naryId\x12\x38\n\x18\x63\x61nary_downsample_factor\x18\x06 \x01(\x05R\x16\x63\x61naryDownsampleFactor\x12T\n\x13online_store_params\x18\x08 \x01(\x0b\x32$.tecton_proto.data.OnlineStoreParamsR\x11onlineStoreParamsJ\x04\x08\x07\x10\x08\"\xaa\x01\n OnlineStoreMetadataConfiguration\x12\x30\n\x14\x65xecution_table_name\x18\x01 \x01(\tR\x12\x65xecutionTableName\x12T\n\x13online_store_params\x18\x02 \x01(\x0b\x32$.tecton_proto.data.OnlineStoreParamsR\x11onlineStoreParamsB \n\x1c\x63om.tecton.onlinestorewriterP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.online_store_writer.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.tecton.onlinestorewriterP\001'
  _ONLINESTOREWRITERCONFIGURATION._serialized_start=154
  _ONLINESTOREWRITERCONFIGURATION._serialized_end=559
  _ONLINESTOREMETADATACONFIGURATION._serialized_start=562
  _ONLINESTOREMETADATACONFIGURATION._serialized_end=732
# @@protoc_insertion_point(module_scope)
