# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/canary/update.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.common import pair_pb2 as tecton__proto_dot_common_dot_pair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tecton_proto/canary/update.proto\x12\x13tecton_proto.canary\x1a\x1etecton_proto/common/pair.proto\"\x88\x04\n\x0c\x43\x61naryUpdate\x12\x1d\n\ntable_name\x18\x01 \x01(\tR\ttableName\x12\x44\n\x10serialized_items\x18\x02 \x03(\x0b\x32\x19.tecton_proto.common.PairR\x0fserializedItems\x12\x31\n\x14\x63ondition_expression\x18\x03 \x01(\tR\x13\x63onditionExpression\x12\x64\n!dynamo_expression_attribute_names\x18\x04 \x03(\x0b\x32\x19.tecton_proto.common.PairR\x1e\x64ynamoExpressionAttributeNames\x12\x66\n\"dynamo_expression_attribute_values\x18\x05 \x03(\x0b\x32\x19.tecton_proto.common.PairR\x1f\x64ynamoExpressionAttributeValues\x12\x12\n\x04time\x18\x06 \x01(\tR\x04time\x12&\n\x0fis_status_table\x18\x07 \x01(\x08R\risStatusTable\x12V\n\x11\x66\x65\x61ture_view_type\x18\x08 \x01(\x0e\x32*.tecton_proto.canary.CanaryFeatureViewTypeR\x0f\x66\x65\x61tureViewType*d\n\x15\x43\x61naryFeatureViewType\x12\r\n\tUNDEFINED\x10\x00\x12\x19\n\x15TEMPORAL_FEATURE_VIEW\x10\x01\x12!\n\x1dWINDOW_AGGREGATE_FEATURE_VIEW\x10\x02\x42\x15\n\x11\x63om.tecton.canaryP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.canary.update_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.tecton.canaryP\001'
  _CANARYFEATUREVIEWTYPE._serialized_start=612
  _CANARYFEATUREVIEWTYPE._serialized_end=712
  _CANARYUPDATE._serialized_start=90
  _CANARYUPDATE._serialized_end=610
# @@protoc_insertion_point(module_scope)
