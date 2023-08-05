# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/materialization/params.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.data import feature_view_pb2 as tecton__proto_dot_data_dot_feature__view__pb2
from tecton_proto.data import virtual_data_source_pb2 as tecton__proto_dot_data_dot_virtual__data__source__pb2
from tecton_proto.data import transformation_pb2 as tecton__proto_dot_data_dot_transformation__pb2
from tecton_proto.dataobs import config_pb2 as tecton__proto_dot_dataobs_dot_config__pb2
from tecton_proto.online_store_writer import config_pb2 as tecton__proto_dot_online__store__writer_dot_config__pb2
from tecton_proto.materialization import materialization_task_pb2 as tecton__proto_dot_materialization_dot_materialization__task__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)tecton_proto/materialization/params.proto\x12\x1ctecton_proto.materialization\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ctecton_proto/common/id.proto\x1a$tecton_proto/data/feature_view.proto\x1a+tecton_proto/data/virtual_data_source.proto\x1a&tecton_proto/data/transformation.proto\x1a!tecton_proto/dataobs/config.proto\x1a-tecton_proto/online_store_writer/config.proto\x1a\x37tecton_proto/materialization/materialization_task.proto\"\xf3\x10\n\x19MaterializationTaskParams\x12\x41\n\x0c\x66\x65\x61ture_view\x18\x16 \x01(\x0b\x32\x1e.tecton_proto.data.FeatureViewR\x0b\x66\x65\x61tureView\x12\x36\n\x17materialization_task_id\x18# \x01(\tR\x15materializationTaskId\x12!\n\x0cis_streaming\x18\t \x01(\x08R\x0bisStreaming\x12\x46\n\x11window_start_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0fwindowStartTime\x12\x42\n\x0fwindow_end_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rwindowEndTime\x12H\n\x12\x66\x65\x61ture_start_time\x18\x1a \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10\x66\x65\x61tureStartTime\x12\x44\n\x10\x66\x65\x61ture_end_time\x18\x1b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0e\x66\x65\x61tureEndTime\x12\x1d\n\ntile_count\x18\n \x01(\x05R\ttileCount\x12$\n\x0es3_output_path\x18\x03 \x01(\tR\x0cs3OutputPath\x12:\n\x19streaming_checkpoint_path\x18\x05 \x01(\tR\x17streamingCheckpointPath\x12M\n#streaming_trigger_interval_override\x18\" \x01(\tR streamingTriggerIntervalOverride\x12\x44\n\x1f\x64ynamodb_cross_account_role_arn\x18\r \x01(\tR\x1b\x64ynamodbCrossAccountRoleArn\x12J\n\"dynamodb_cross_account_external_id\x18\x1e \x01(\tR\x1e\x64ynamodbCrossAccountExternalId\x12\x32\n\x15\x64\x62\x66s_credentials_path\x18! \x01(\tR\x13\x64\x62\x66sCredentialsPath\x12\x32\n\x15is_overwrite_backfill\x18\x0e \x01(\x08R\x13isOverwriteBackfill\x12V\n\x14virtual_data_sources\x18\x11 \x03(\x0b\x32$.tecton_proto.data.VirtualDataSourceR\x12virtualDataSources\x12\'\n\x0fidempotence_key\x18\x12 \x01(\tR\x0eidempotenceKey\x12\x36\n\nattempt_id\x18) \x01(\x0b\x32\x17.tecton_proto.common.IdR\tattemptId\x12\x39\n\x19spark_job_execution_table\x18\x13 \x01(\tR\x16sparkJobExecutionTable\x12,\n\x12job_metadata_table\x18( \x01(\tR\x10jobMetadataTable\x12=\n\x1buse_new_consumption_metrics\x18* \x01(\x08R\x18useNewConsumptionMetrics\x12,\n\x12use_stream_handoff\x18+ \x01(\x08R\x10useStreamHandoff\x12\x46\n spark_job_execution_table_region\x18\x14 \x01(\tR\x1csparkJobExecutionTableRegion\x12\x1b\n\tcanary_id\x18\x15 \x01(\tR\x08\x63\x61naryId\x12K\n\x0ftransformations\x18\x17 \x03(\x0b\x32!.tecton_proto.data.TransformationR\x0ftransformations\x12}\n\x1aonline_store_writer_config\x18\x18 \x01(\x0b\x32@.tecton_proto.online_store_writer.OnlineStoreWriterConfigurationR\x17onlineStoreWriterConfig\x12\x31\n\x15write_to_online_store\x18\x1d \x01(\x08R\x12writeToOnlineStore\x12\x1f\n\x0bingest_path\x18\x1f \x01(\tR\ningestPath\x12\x61\n\x13\x64\x65letion_parameters\x18  \x01(\x0b\x32\x30.tecton_proto.materialization.DeletionParametersR\x12\x64\x65letionParameters\x12z\n\x1c\x64\x65lta_maintenance_parameters\x18\' \x01(\x0b\x32\x38.tecton_proto.materialization.DeltaMaintenanceParametersR\x1a\x64\x65ltaMaintenanceParameters\x12x\n\x19\x64\x61ta_observability_config\x18% \x01(\x0b\x32<.tecton_proto.dataobs.DataObservabilityMaterializationConfigR\x17\x64\x61taObservabilityConfig\x12)\n\x10\x66\x65\x61ture_services\x18& \x03(\tR\x0f\x66\x65\x61tureServicesJ\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03J\x04\x08\x04\x10\x05J\x04\x08\x06\x10\x07J\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\x0f\x10\x10J\x04\x08\x19\x10\x1aJ\x04\x08\x1c\x10\x1dJ\x04\x08$\x10%B\x1e\n\x1a\x63om.tecton.materializationP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.materialization.params_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.tecton.materializationP\001'
  _MATERIALIZATIONTASKPARAMS._serialized_start=401
  _MATERIALIZATIONTASKPARAMS._serialized_end=2564
# @@protoc_insertion_point(module_scope)
