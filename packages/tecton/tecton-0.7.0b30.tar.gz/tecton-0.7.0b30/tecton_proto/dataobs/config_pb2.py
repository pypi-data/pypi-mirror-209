# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/dataobs/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from tecton_proto.dataobs import expectation_pb2 as tecton__proto_dot_dataobs_dot_expectation__pb2
from tecton_proto.dataobs import metric_pb2 as tecton__proto_dot_dataobs_dot_metric__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!tecton_proto/dataobs/config.proto\x12\x14tecton_proto.dataobs\x1a\x1egoogle/protobuf/duration.proto\x1a&tecton_proto/dataobs/expectation.proto\x1a!tecton_proto/dataobs/metric.proto\"\xa9\x03\n\x17\x44\x61taObservabilityConfig\x12\x1c\n\tworkspace\x18\x01 \x01(\tR\tworkspace\x12*\n\x11\x66\x65\x61ture_view_name\x18\x02 \x01(\tR\x0f\x66\x65\x61tureViewName\x12U\n\'feature_expectation_validation_schedule\x18\x03 \x01(\tR$featureExpectationValidationSchedule\x12\x36\n\x07metrics\x18\x04 \x03(\x0b\x32\x1c.tecton_proto.dataobs.MetricR\x07metrics\x12[\n\x14\x66\x65\x61ture_expectations\x18\x05 \x03(\x0b\x32(.tecton_proto.dataobs.FeatureExpectationR\x13\x66\x65\x61tureExpectations\x12X\n\x13metric_expectations\x18\x06 \x03(\x0b\x32\'.tecton_proto.dataobs.MetricExpectationR\x12metricExpectations\"\xb2\x01\n&DataObservabilityMaterializationConfig\x12\x18\n\x07\x65nabled\x18\x01 \x01(\x08R\x07\x65nabled\x12\x42\n\x0fmetric_interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0emetricInterval\x12*\n\x11metric_table_name\x18\x03 \x01(\tR\x0fmetricTableNameB\x16\n\x12\x63om.tecton.dataobsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.dataobs.config_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.tecton.dataobsP\001'
  _DATAOBSERVABILITYCONFIG._serialized_start=167
  _DATAOBSERVABILITYCONFIG._serialized_end=592
  _DATAOBSERVABILITYMATERIALIZATIONCONFIG._serialized_start=595
  _DATAOBSERVABILITYMATERIALIZATIONCONFIG._serialized_end=773
# @@protoc_insertion_point(module_scope)
