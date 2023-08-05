# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/validation/validator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.args import entity_pb2 as tecton__proto_dot_args_dot_entity__pb2
from tecton_proto.args import virtual_data_source_pb2 as tecton__proto_dot_args_dot_virtual__data__source__pb2
from tecton_proto.args import transformation_pb2 as tecton__proto_dot_args_dot_transformation__pb2
from tecton_proto.args import feature_view_pb2 as tecton__proto_dot_args_dot_feature__view__pb2
from tecton_proto.args import feature_service_pb2 as tecton__proto_dot_args_dot_feature__service__pb2
from tecton_proto.common import schema_pb2 as tecton__proto_dot_common_dot_schema__pb2
from tecton_proto.common import spark_schema_pb2 as tecton__proto_dot_common_dot_spark__schema__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'tecton_proto/validation/validator.proto\x12\x17tecton_proto.validation\x1a\x1etecton_proto/args/entity.proto\x1a+tecton_proto/args/virtual_data_source.proto\x1a&tecton_proto/args/transformation.proto\x1a$tecton_proto/args/feature_view.proto\x1a\'tecton_proto/args/feature_service.proto\x1a tecton_proto/common/schema.proto\x1a&tecton_proto/common/spark_schema.proto\"I\n\x14\x45ntityValidationArgs\x12\x31\n\x04\x61rgs\x18\x01 \x01(\x0b\x32\x1d.tecton_proto.args.EntityArgsR\x04\x61rgs\"\xeb\x01\n\x1fVirtualDataSourceValidationArgs\x12<\n\x04\x61rgs\x18\x01 \x01(\x0b\x32(.tecton_proto.args.VirtualDataSourceArgsR\x04\x61rgs\x12\x43\n\x0c\x62\x61tch_schema\x18\x02 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x0b\x62\x61tchSchema\x12\x45\n\rstream_schema\x18\x03 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x0cstreamSchema\"Y\n\x1cTransformationValidationArgs\x12\x39\n\x04\x61rgs\x18\x01 \x01(\x0b\x32%.tecton_proto.args.TransformationArgsR\x04\x61rgs\"\xe5\x01\n\x19\x46\x65\x61tureViewValidationArgs\x12\x36\n\x04\x61rgs\x18\x01 \x01(\x0b\x32\".tecton_proto.args.FeatureViewArgsR\x04\x61rgs\x12<\n\x0bview_schema\x18\x02 \x01(\x0b\x32\x1b.tecton_proto.common.SchemaR\nviewSchema\x12R\n\x16materialization_schema\x18\x03 \x01(\x0b\x32\x1b.tecton_proto.common.SchemaR\x15materializationSchema\"Y\n\x1c\x46\x65\x61tureServiceValidationArgs\x12\x39\n\x04\x61rgs\x18\x01 \x01(\x0b\x32%.tecton_proto.args.FeatureServiceArgsR\x04\x61rgs\"\xeb\x03\n\x11\x46\x63oValidationArgs\x12j\n\x13virtual_data_source\x18\x01 \x01(\x0b\x32\x38.tecton_proto.validation.VirtualDataSourceValidationArgsH\x00R\x11virtualDataSource\x12G\n\x06\x65ntity\x18\x02 \x01(\x0b\x32-.tecton_proto.validation.EntityValidationArgsH\x00R\x06\x65ntity\x12W\n\x0c\x66\x65\x61ture_view\x18\x03 \x01(\x0b\x32\x32.tecton_proto.validation.FeatureViewValidationArgsH\x00R\x0b\x66\x65\x61tureView\x12`\n\x0f\x66\x65\x61ture_service\x18\x04 \x01(\x0b\x32\x35.tecton_proto.validation.FeatureServiceValidationArgsH\x00R\x0e\x66\x65\x61tureService\x12_\n\x0etransformation\x18\x05 \x01(\x0b\x32\x35.tecton_proto.validation.TransformationValidationArgsH\x00R\x0etransformationB\x05\n\x03\x66\x63o\"h\n\x11ValidationRequest\x12S\n\x0fvalidation_args\x18\x01 \x03(\x0b\x32*.tecton_proto.validation.FcoValidationArgsR\x0evalidationArgsB\x19\n\x15\x63om.tecton.validationP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.validation.validator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.tecton.validationP\001'
  _ENTITYVALIDATIONARGS._serialized_start=338
  _ENTITYVALIDATIONARGS._serialized_end=411
  _VIRTUALDATASOURCEVALIDATIONARGS._serialized_start=414
  _VIRTUALDATASOURCEVALIDATIONARGS._serialized_end=649
  _TRANSFORMATIONVALIDATIONARGS._serialized_start=651
  _TRANSFORMATIONVALIDATIONARGS._serialized_end=740
  _FEATUREVIEWVALIDATIONARGS._serialized_start=743
  _FEATUREVIEWVALIDATIONARGS._serialized_end=972
  _FEATURESERVICEVALIDATIONARGS._serialized_start=974
  _FEATURESERVICEVALIDATIONARGS._serialized_end=1063
  _FCOVALIDATIONARGS._serialized_start=1066
  _FCOVALIDATIONARGS._serialized_end=1557
  _VALIDATIONREQUEST._serialized_start=1559
  _VALIDATIONREQUEST._serialized_end=1663
# @@protoc_insertion_point(module_scope)
