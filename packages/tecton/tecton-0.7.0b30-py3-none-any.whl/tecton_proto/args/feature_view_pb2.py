# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/feature_view.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tecton_proto.args import basic_info_pb2 as tecton__proto_dot_args_dot_basic__info__pb2
from tecton_proto.args import pipeline_pb2 as tecton__proto_dot_args_dot_pipeline__pb2
from tecton_proto.args import data_source_pb2 as tecton__proto_dot_args_dot_data__source__pb2
from tecton_proto.args import diff_options_pb2 as tecton__proto_dot_args_dot_diff__options__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.common import framework_version_pb2 as tecton__proto_dot_common_dot_framework__version__pb2
from tecton_proto.common import schema_pb2 as tecton__proto_dot_common_dot_schema__pb2
from tecton_proto.common import spark_schema_pb2 as tecton__proto_dot_common_dot_spark__schema__pb2
from tecton_proto.common import data_source_type_pb2 as tecton__proto_dot_common_dot_data__source__type__pb2
from tecton_proto.args import version_constraints_pb2 as tecton__proto_dot_args_dot_version__constraints__pb2
from tecton_proto.common import analytics_options_pb2 as tecton__proto_dot_common_dot_analytics__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$tecton_proto/args/feature_view.proto\x12\x11tecton_proto.args\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"tecton_proto/args/basic_info.proto\x1a tecton_proto/args/pipeline.proto\x1a#tecton_proto/args/data_source.proto\x1a$tecton_proto/args/diff_options.proto\x1a\x1ctecton_proto/common/id.proto\x1a+tecton_proto/common/framework_version.proto\x1a tecton_proto/common/schema.proto\x1a&tecton_proto/common/spark_schema.proto\x1a*tecton_proto/common/data_source_type.proto\x1a+tecton_proto/args/version_constraints.proto\x1a+tecton_proto/common/analytics_options.proto\"\xe7\n\n\x0f\x46\x65\x61tureViewArgs\x12?\n\x0f\x66\x65\x61ture_view_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\rfeatureViewId\x12N\n\x11\x66\x65\x61ture_view_type\x18\x02 \x01(\x0e\x32\".tecton_proto.args.FeatureViewTypeR\x0f\x66\x65\x61tureViewType\x12\x37\n\x04info\x18\x03 \x01(\x0b\x32\x1c.tecton_proto.args.BasicInfoB\x05\x92M\x02\x10\x01R\x04info\x12\x46\n\x07version\x18\x1d \x01(\x0e\x32%.tecton_proto.common.FrameworkVersionB\x05\x92M\x02\x08\x05R\x07version\x12.\n\x0fprevent_destroy\x18  \x01(\x08\x42\x05\x92M\x02\x08\x01R\x0epreventDestroy\x12G\n\x08\x65ntities\x18\x04 \x03(\x0b\x32$.tecton_proto.args.EntityKeyOverrideB\x05\x92M\x02\x08\x06R\x08\x65ntities\x12M\n\rtemporal_args\x18\x17 \x01(\x0b\x32\x1f.tecton_proto.args.TemporalArgsB\x05\x92M\x02\x10\x01H\x00R\x0ctemporalArgs\x12i\n\x17temporal_aggregate_args\x18\x18 \x01(\x0b\x32(.tecton_proto.args.TemporalAggregateArgsB\x05\x92M\x02\x10\x01H\x00R\x15temporalAggregateArgs\x12|\n\x1ematerialized_feature_view_args\x18\x1c \x01(\x0b\x32..tecton_proto.args.MaterializedFeatureViewArgsB\x05\x92M\x02\x10\x01H\x00R\x1bmaterializedFeatureViewArgs\x12N\n\x0eon_demand_args\x18\x19 \x01(\x0b\x32\x1f.tecton_proto.args.OnDemandArgsB\x05\x92M\x02\x10\x01H\x00R\x0conDemandArgs\x12Z\n\x12\x66\x65\x61ture_table_args\x18\x1a \x01(\x0b\x32#.tecton_proto.args.FeatureTableArgsB\x05\x92M\x02\x10\x01H\x00R\x10\x66\x65\x61tureTableArgs\x12\x30\n\x14online_serving_index\x18\x05 \x03(\tR\x12onlineServingIndex\x12,\n\x0eonline_enabled\x18\x0e \x01(\x08\x42\x05\x92M\x02\x08\x01R\ronlineEnabled\x12.\n\x0foffline_enabled\x18\x0f \x01(\x08\x42\x05\x92M\x02\x08\x01R\x0eofflineEnabled\x12>\n\x08pipeline\x18\x06 \x01(\x0b\x32\x1b.tecton_proto.args.PipelineB\x05\x92M\x02\x08\x06R\x08pipeline\x12N\n\x12\x66orced_view_schema\x18\x1e \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x10\x66orcedViewSchema\x12^\n\x1a\x66orced_materialized_schema\x18\x1f \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x18\x66orcedMaterializedSchemaB\x0b\n\ttype_argsJ\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\t\x10\nJ\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x0c\x10\rJ\x04\x08\r\x10\x0eJ\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13J\x04\x08\x13\x10\x14J\x04\x08\x14\x10\x15J\x04\x08\x15\x10\x16J\x04\x08\x16\x10\x17J\x04\x08\x1b\x10\x1c\"f\n\x11\x45ntityKeyOverride\x12\x34\n\tentity_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x08\x65ntityId\x12\x1b\n\tjoin_keys\x18\x02 \x03(\tR\x08joinKeys\"K\n\x0e\x42\x61\x63kfillConfig\x12\x39\n\x04mode\x18\x01 \x01(\x0e\x32%.tecton_proto.args.BackfillConfigModeR\x04mode\"\xce\x01\n\x0cOutputStream\x12)\n\x10include_features\x18\x01 \x01(\x08R\x0fincludeFeatures\x12\x44\n\x07kinesis\x18\x02 \x01(\x0b\x32(.tecton_proto.args.KinesisDataSourceArgsH\x00R\x07kinesis\x12>\n\x05kafka\x18\x03 \x01(\x0b\x32&.tecton_proto.args.KafkaDataSourceArgsH\x00R\x05kafkaB\r\n\x0bstream_sink\"\xb9\x08\n\x0cTemporalArgs\x12#\n\rtimestamp_key\x18\x01 \x01(\tR\x0ctimestampKey\x12\x46\n\x11schedule_interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x10scheduleInterval\x12O\n\x12\x66\x65\x61ture_start_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\x92M\x02\x08\x01R\x10\x66\x65\x61tureStartTime\x12^\n\x1emax_batch_aggregation_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1bmaxBatchAggregationInterval\x12\x41\n\x0bserving_ttl\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x92M\x02\x08\x06R\nservingTtl\x12S\n\x0eoffline_config\x18\x06 \x01(\x0b\x32,.tecton_proto.args.OfflineFeatureStoreConfigR\rofflineConfig\x12U\n\x15\x62\x61tch_materialization\x18\x07 \x01(\x0b\x32 .tecton_proto.args.ClusterConfigR\x14\x62\x61tchMaterialization\x12]\n\x19streaming_materialization\x18\x08 \x01(\x0b\x32 .tecton_proto.args.ClusterConfigR\x18streamingMaterialization\x12J\n\nmonitoring\x18\t \x01(\x0b\x32#.tecton_proto.args.MonitoringConfigB\x05\x92M\x02\x08\x01R\nmonitoring\x12M\n\x10\x64\x61ta_source_type\x18\n \x01(\x0e\x32#.tecton_proto.common.DataSourceTypeR\x0e\x64\x61taSourceType\x12Q\n\x0f\x62\x61\x63kfill_config\x18\x0b \x01(\x0b\x32!.tecton_proto.args.BackfillConfigB\x05\x92M\x02\x08\x03R\x0e\x62\x61\x63kfillConfig\x12T\n\x13online_store_config\x18\x0c \x01(\x0b\x32$.tecton_proto.args.OnlineStoreConfigR\x11onlineStoreConfig\x12\x33\n\x15incremental_backfills\x18\r \x01(\x08R\x14incrementalBackfills\x12\x44\n\routput_stream\x18\x0e \x01(\x0b\x32\x1f.tecton_proto.args.OutputStreamR\x0coutputStream\"\xe9\x08\n\x15TemporalAggregateArgs\x12k\n!aggregation_slide_period_duration\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x92M\x02\x08\x05R\x1e\x61ggregationSlidePeriodDuration\x12\x38\n\x18\x61ggregation_slide_period\x18\x02 \x01(\tR\x16\x61ggregationSlidePeriod\x12I\n\x0c\x61ggregations\x18\x03 \x03(\x0b\x32%.tecton_proto.args.FeatureAggregationR\x0c\x61ggregations\x12#\n\rtimestamp_key\x18\x04 \x01(\tR\x0ctimestampKey\x12\x46\n\x11schedule_interval\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x10scheduleInterval\x12O\n\x12\x66\x65\x61ture_start_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\x92M\x02\x08\x01R\x10\x66\x65\x61tureStartTime\x12^\n\x1emax_batch_aggregation_interval\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1bmaxBatchAggregationInterval\x12S\n\x0eoffline_config\x18\x08 \x01(\x0b\x32,.tecton_proto.args.OfflineFeatureStoreConfigR\rofflineConfig\x12U\n\x15\x62\x61tch_materialization\x18\t \x01(\x0b\x32 .tecton_proto.args.ClusterConfigR\x14\x62\x61tchMaterialization\x12]\n\x19streaming_materialization\x18\n \x01(\x0b\x32 .tecton_proto.args.ClusterConfigR\x18streamingMaterialization\x12J\n\nmonitoring\x18\x0b \x01(\x0b\x32#.tecton_proto.args.MonitoringConfigB\x05\x92M\x02\x08\x01R\nmonitoring\x12M\n\x10\x64\x61ta_source_type\x18\x0c \x01(\x0e\x32#.tecton_proto.common.DataSourceTypeR\x0e\x64\x61taSourceType\x12T\n\x13online_store_config\x18\r \x01(\x0b\x32$.tecton_proto.args.OnlineStoreConfigR\x11onlineStoreConfig\x12\x44\n\routput_stream\x18\x0e \x01(\x0b\x32\x1f.tecton_proto.args.OutputStreamR\x0coutputStream\"\xc1\n\n\x1bMaterializedFeatureViewArgs\x12\'\n\x0ftimestamp_field\x18\x01 \x01(\tR\x0etimestampField\x12@\n\x0e\x62\x61tch_schedule\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\rbatchSchedule\x12O\n\x12\x66\x65\x61ture_start_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x05\x92M\x02\x08\x01R\x10\x66\x65\x61tureStartTime\x12^\n\x1emax_batch_aggregation_interval\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x1bmaxBatchAggregationInterval\x12\x41\n\x0bserving_ttl\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x92M\x02\x08\x06R\nservingTtl\x12Q\n\roffline_store\x18\x06 \x01(\x0b\x32,.tecton_proto.args.OfflineFeatureStoreConfigR\x0cofflineStore\x12\x45\n\rbatch_compute\x18\x07 \x01(\x0b\x32 .tecton_proto.args.ClusterConfigR\x0c\x62\x61tchCompute\x12G\n\x0estream_compute\x18\x08 \x01(\x0b\x32 .tecton_proto.args.ClusterConfigR\rstreamCompute\x12O\n\nmonitoring\x18\t \x01(\x0b\x32#.tecton_proto.args.MonitoringConfigB\n\x92M\x02\x08\x01\x92M\x02\x10\x01R\nmonitoring\x12M\n\x10\x64\x61ta_source_type\x18\n \x01(\x0e\x32#.tecton_proto.common.DataSourceTypeR\x0e\x64\x61taSourceType\x12G\n\x0conline_store\x18\x0b \x01(\x0b\x32$.tecton_proto.args.OnlineStoreConfigR\x0bonlineStore\x12\x33\n\x15incremental_backfills\x18\x0c \x01(\x08R\x14incrementalBackfills\x12L\n\x14\x61ggregation_interval\x18\r \x01(\x0b\x32\x19.google.protobuf.DurationR\x13\x61ggregationInterval\x12]\n\x16stream_processing_mode\x18\x0f \x01(\x0e\x32\'.tecton_proto.args.StreamProcessingModeR\x14streamProcessingMode\x12I\n\x0c\x61ggregations\x18\x0e \x03(\x0b\x32%.tecton_proto.args.FeatureAggregationR\x0c\x61ggregations\x12\x44\n\routput_stream\x18\x10 \x01(\x0b\x32\x1f.tecton_proto.args.OutputStreamR\x0coutputStream\x12O\n\rbatch_trigger\x18\x11 \x01(\x0e\x32#.tecton_proto.args.BatchTriggerTypeB\x05\x92M\x02\x08\x01R\x0c\x62\x61tchTrigger\x12\x33\n\x06schema\x18\x12 \x01(\x0b\x32\x1b.tecton_proto.common.SchemaR\x06schema\"\x9d\x01\n\x0cOnDemandArgs\x12L\n\routput_schema\x18\x01 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaB\x05\x82}\x02\x10\x03R\x0coutputSchema\x12?\n\x06schema\x18\x02 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaB\x05\x82}\x02\x08\x05R\x06schema\"\xf3\x05\n\x10\x46\x65\x61tureTableArgs\x12L\n\routput_schema\x18\x01 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaB\x05\x82}\x02\x10\x03R\x0coutputSchema\x12?\n\x06schema\x18\x06 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaB\x05\x82}\x02\x08\x05R\x06schema\x12\x41\n\x0bserving_ttl\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x92M\x02\x08\x06R\nservingTtl\x12Z\n\x0eoffline_config\x18\x03 \x01(\x0b\x32,.tecton_proto.args.OfflineFeatureStoreConfigB\x05\x82}\x02\x10\x03R\rofflineConfig\x12X\n\roffline_store\x18\x07 \x01(\x0b\x32,.tecton_proto.args.OfflineFeatureStoreConfigB\x05\x82}\x02\x08\x05R\x0cofflineStore\x12[\n\x13online_store_config\x18\x04 \x01(\x0b\x32$.tecton_proto.args.OnlineStoreConfigB\x05\x82}\x02\x10\x03R\x11onlineStoreConfig\x12N\n\x0conline_store\x18\x08 \x01(\x0b\x32$.tecton_proto.args.OnlineStoreConfigB\x05\x82}\x02\x08\x05R\x0bonlineStore\x12\\\n\x15\x62\x61tch_materialization\x18\x05 \x01(\x0b\x32 .tecton_proto.args.ClusterConfigB\x05\x82}\x02\x10\x03R\x14\x62\x61tchMaterialization\x12L\n\rbatch_compute\x18\t \x01(\x0b\x32 .tecton_proto.args.ClusterConfigB\x05\x82}\x02\x08\x05R\x0c\x62\x61tchCompute\"\xec\x03\n\x12\x46\x65\x61tureAggregation\x12\x16\n\x06\x63olumn\x18\x01 \x01(\tR\x06\x63olumn\x12\x1a\n\x08\x66unction\x18\x02 \x01(\tR\x08\x66unction\x12\x62\n\x0f\x66unction_params\x18\x05 \x03(\x0b\x32\x39.tecton_proto.args.FeatureAggregation.FunctionParamsEntryR\x0e\x66unctionParams\x12\x43\n\x0ctime_windows\x18\x03 \x03(\x0b\x32\x19.google.protobuf.DurationB\x05\x82}\x02\x10\x03R\x0btimeWindows\x12\x34\n\x10time_window_strs\x18\x04 \x03(\tB\n\x82}\x02\x10\x03\x92M\x02\x08\x05R\x0etimeWindowStrs\x12\x41\n\x0btime_window\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x82}\x02\x08\x05R\ntimeWindow\x12\x1e\n\x04name\x18\x07 \x01(\tB\n\x82}\x02\x08\x05\x92M\x02 \x01R\x04name\x1a`\n\x13\x46unctionParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.tecton_proto.args.ParamValueR\x05value:\x02\x38\x01\"8\n\nParamValue\x12!\n\x0bint64_value\x18\x01 \x01(\x03H\x00R\nint64ValueB\x07\n\x05value\"\xe9\x04\n\rClusterConfig\x12\\\n\x10\x65xisting_cluster\x18\x01 \x01(\x0b\x32(.tecton_proto.args.ExistingClusterConfigB\x05\x92M\x02\x08\x01H\x00R\x0f\x65xistingCluster\x12S\n\x0enew_databricks\x18\x02 \x01(\x0b\x32#.tecton_proto.args.NewClusterConfigB\x05\x92M\x02\x08\x01H\x00R\rnewDatabricks\x12\x45\n\x07new_emr\x18\x03 \x01(\x0b\x32#.tecton_proto.args.NewClusterConfigB\x05\x92M\x02\x08\x01H\x00R\x06newEmr\x12^\n\x0fimplicit_config\x18\x04 \x01(\x0b\x32\'.tecton_proto.args.DefaultClusterConfigB\n\x92M\x02\x08\x01\x92M\x02\x18\x05H\x00R\x0eimplicitConfig\x12V\n\x0fjson_databricks\x18\x05 \x01(\x0b\x32$.tecton_proto.args.JsonClusterConfigB\x05\x92M\x02\x08\x01H\x00R\x0ejsonDatabricks\x12H\n\x08json_emr\x18\x06 \x01(\x0b\x32$.tecton_proto.args.JsonClusterConfigB\x05\x92M\x02\x08\x01H\x00R\x07jsonEmr\x12R\n\rjson_dataproc\x18\x07 \x01(\x0b\x32$.tecton_proto.args.JsonClusterConfigB\x05\x92M\x02\x08\x01H\x00R\x0cjsonDataprocB\x08\n\x06\x63onfig\"@\n\x11JsonClusterConfig\x12+\n\x04json\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructR\x04json\"G\n\x15\x45xistingClusterConfig\x12.\n\x13\x65xisting_cluster_id\x18\x01 \x01(\tR\x11\x65xistingClusterId\"\x9f\x03\n\x10NewClusterConfig\x12#\n\rinstance_type\x18\x01 \x01(\tR\x0cinstanceType\x12\x33\n\x15instance_availability\x18\x06 \x01(\tR\x14instanceAvailability\x12*\n\x11number_of_workers\x18\x02 \x01(\x05R\x0fnumberOfWorkers\x12\x32\n\x16root_volume_size_in_gb\x18\x03 \x01(\x05R\x12rootVolumeSizeInGb\x12\x34\n\x16\x65xtra_pip_dependencies\x18\x04 \x03(\tR\x14\x65xtraPipDependencies\x12\x41\n\x0cspark_config\x18\x05 \x01(\x0b\x32\x1e.tecton_proto.args.SparkConfigR\x0bsparkConfig\x12&\n\x0f\x66irst_on_demand\x18\x07 \x01(\x05R\rfirstOnDemand\x12\x30\n\x14pinned_spark_version\x18\x08 \x01(\tR\x12pinnedSparkVersion\"\x8a\x01\n\x14\x44\x65\x66\x61ultClusterConfig\x12?\n\x18\x64\x61tabricks_spark_version\x18\x01 \x01(\tB\x05\x92M\x02\x18\x05R\x16\x64\x61tabricksSparkVersion\x12\x31\n\x11\x65mr_spark_version\x18\x02 \x01(\tB\x05\x92M\x02\x18\x05R\x0f\x65mrSparkVersion\"\x83\x03\n\x0bSparkConfig\x12.\n\x13spark_driver_memory\x18\x01 \x01(\tR\x11sparkDriverMemory\x12\x32\n\x15spark_executor_memory\x18\x02 \x01(\tR\x13sparkExecutorMemory\x12?\n\x1cspark_driver_memory_overhead\x18\x03 \x01(\tR\x19sparkDriverMemoryOverhead\x12\x43\n\x1espark_executor_memory_overhead\x18\x04 \x01(\tR\x1bsparkExecutorMemoryOverhead\x12L\n\nspark_conf\x18\x05 \x03(\x0b\x32-.tecton_proto.args.SparkConfig.SparkConfEntryR\tsparkConf\x1a<\n\x0eSparkConfEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xa0\x01\n\x11OnlineStoreConfig\x12@\n\x06\x64ynamo\x18\x01 \x01(\x0b\x32&.tecton_proto.args.DynamoDbOnlineStoreH\x00R\x06\x64ynamo\x12;\n\x05redis\x18\x02 \x01(\x0b\x32#.tecton_proto.args.RedisOnlineStoreH\x00R\x05redisB\x0c\n\nstore_type\"\xa1\x02\n\x13\x44ynamoDbOnlineStore\x12\x33\n\x16\x63ross_account_role_arn\x18\x01 \x01(\tR\x13\x63rossAccountRoleArn\x12\x39\n\x19\x63ross_account_external_id\x18\x02 \x01(\tR\x16\x63rossAccountExternalId\x12L\n#cross_account_intermediate_role_arn\x18\x05 \x01(\tR\x1f\x63rossAccountIntermediateRoleArn\x12\x18\n\x07\x65nabled\x18\x03 \x01(\x08R\x07\x65nabled\x12\x32\n\x15\x64\x62\x66s_credentials_path\x18\x04 \x01(\tR\x13\x64\x62\x66sCredentialsPath\"\x94\x02\n\x10RedisOnlineStore\x12\x30\n\x10primary_endpoint\x18\x02 \x01(\tB\x05\x92M\x02\x08\x06R\x0fprimaryEndpoint\x12=\n\x14\x61uthentication_token\x18\x04 \x01(\tB\n\x92M\x02\x08\x01\x92M\x02\x18\x06R\x13\x61uthenticationToken\x12+\n\x0btls_enabled\x18\x06 \x01(\x08\x42\n\x92M\x02\x08\x01\x92M\x02\x18\x05R\ntlsEnabled\x12\x1f\n\x07\x65nabled\x18\x05 \x01(\x08\x42\x05\x92M\x02\x18\x05R\x07\x65nabled\x12/\n\x13operations_endpoint\x18\x08 \x01(\tR\x12operationsEndpointJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04J\x04\x08\x07\x10\x08\"\xdb\x01\n\x19OfflineFeatureStoreConfig\x12<\n\x07parquet\x18\x01 \x01(\x0b\x32 .tecton_proto.args.ParquetConfigH\x00R\x07parquet\x12\x36\n\x05\x64\x65lta\x18\x02 \x01(\x0b\x32\x1e.tecton_proto.args.DeltaConfigH\x00R\x05\x64\x65lta\x12:\n\x15subdirectory_override\x18\x03 \x01(\tB\x05\x92M\x02\x08\x01R\x14subdirectoryOverrideB\x0c\n\nstore_type\"\x0f\n\rParquetConfig\"X\n\x0b\x44\x65ltaConfig\x12I\n\x13time_partition_size\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11timePartitionSize\"\x99\x02\n\x10MonitoringConfig\x12+\n\x11monitor_freshness\x18\x01 \x01(\x08R\x10monitorFreshness\x12^\n\x1a\x65xpected_feature_freshness\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x82}\x02\x10\x03R\x18\x65xpectedFeatureFreshness\x12O\n\x12\x65xpected_freshness\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x05\x82}\x02\x08\x05R\x11\x65xpectedFreshness\x12\'\n\x0b\x61lert_email\x18\x03 \x01(\tB\x06\xf2\xe2\x02\x02\x08\x01R\nalertEmail*\xe9\x01\n\x0f\x46\x65\x61tureViewType\x12\x1d\n\x19\x46\x45\x41TURE_VIEW_TYPE_UNKNOWN\x10\x00\x12\x1e\n\x1a\x46\x45\x41TURE_VIEW_TYPE_TEMPORAL\x10\x01\x12(\n$FEATURE_VIEW_TYPE_TEMPORAL_AGGREGATE\x10\x02\x12\x1f\n\x1b\x46\x45\x41TURE_VIEW_TYPE_ON_DEMAND\x10\x03\x12#\n\x1f\x46\x45\x41TURE_VIEW_TYPE_FEATURE_TABLE\x10\x04\x12\'\n#FEATURE_VIEW_TYPE_FWV5_FEATURE_VIEW\x10\x05*\xbb\x01\n\x12\x42\x61\x63kfillConfigMode\x12 \n\x1c\x42\x41\x43KFILL_CONFIG_MODE_UNKNOWN\x10\x00\x12?\n;BACKFILL_CONFIG_MODE_SINGLE_BATCH_SCHEDULE_INTERVAL_PER_JOB\x10\x01\x12\x42\n>BACKFILL_CONFIG_MODE_MULTIPLE_BATCH_SCHEDULE_INTERVALS_PER_JOB\x10\x02*\x8b\x01\n\x14StreamProcessingMode\x12\"\n\x1eSTREAM_PROCESSING_MODE_UNKNOWN\x10\x00\x12(\n$STREAM_PROCESSING_MODE_TIME_INTERVAL\x10\x01\x12%\n!STREAM_PROCESSING_MODE_CONTINUOUS\x10\x02*\xa4\x01\n\x10\x42\x61tchTriggerType\x12\x1e\n\x1a\x42\x41TCH_TRIGGER_TYPE_UNKNOWN\x10\x00\x12 \n\x1c\x42\x41TCH_TRIGGER_TYPE_SCHEDULED\x10\x01\x12\x1d\n\x19\x42\x41TCH_TRIGGER_TYPE_MANUAL\x10\x02\x12/\n+BATCH_TRIGGER_TYPE_NO_BATCH_MATERIALIZATION\x10\x03\x42\x13\n\x0f\x63om.tecton.argsP\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.args.feature_view_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.argsP\001'
  _FEATUREVIEWARGS.fields_by_name['info']._options = None
  _FEATUREVIEWARGS.fields_by_name['info']._serialized_options = b'\222M\002\020\001'
  _FEATUREVIEWARGS.fields_by_name['version']._options = None
  _FEATUREVIEWARGS.fields_by_name['version']._serialized_options = b'\222M\002\010\005'
  _FEATUREVIEWARGS.fields_by_name['prevent_destroy']._options = None
  _FEATUREVIEWARGS.fields_by_name['prevent_destroy']._serialized_options = b'\222M\002\010\001'
  _FEATUREVIEWARGS.fields_by_name['entities']._options = None
  _FEATUREVIEWARGS.fields_by_name['entities']._serialized_options = b'\222M\002\010\006'
  _FEATUREVIEWARGS.fields_by_name['temporal_args']._options = None
  _FEATUREVIEWARGS.fields_by_name['temporal_args']._serialized_options = b'\222M\002\020\001'
  _FEATUREVIEWARGS.fields_by_name['temporal_aggregate_args']._options = None
  _FEATUREVIEWARGS.fields_by_name['temporal_aggregate_args']._serialized_options = b'\222M\002\020\001'
  _FEATUREVIEWARGS.fields_by_name['materialized_feature_view_args']._options = None
  _FEATUREVIEWARGS.fields_by_name['materialized_feature_view_args']._serialized_options = b'\222M\002\020\001'
  _FEATUREVIEWARGS.fields_by_name['on_demand_args']._options = None
  _FEATUREVIEWARGS.fields_by_name['on_demand_args']._serialized_options = b'\222M\002\020\001'
  _FEATUREVIEWARGS.fields_by_name['feature_table_args']._options = None
  _FEATUREVIEWARGS.fields_by_name['feature_table_args']._serialized_options = b'\222M\002\020\001'
  _FEATUREVIEWARGS.fields_by_name['online_enabled']._options = None
  _FEATUREVIEWARGS.fields_by_name['online_enabled']._serialized_options = b'\222M\002\010\001'
  _FEATUREVIEWARGS.fields_by_name['offline_enabled']._options = None
  _FEATUREVIEWARGS.fields_by_name['offline_enabled']._serialized_options = b'\222M\002\010\001'
  _FEATUREVIEWARGS.fields_by_name['pipeline']._options = None
  _FEATUREVIEWARGS.fields_by_name['pipeline']._serialized_options = b'\222M\002\010\006'
  _TEMPORALARGS.fields_by_name['feature_start_time']._options = None
  _TEMPORALARGS.fields_by_name['feature_start_time']._serialized_options = b'\222M\002\010\001'
  _TEMPORALARGS.fields_by_name['serving_ttl']._options = None
  _TEMPORALARGS.fields_by_name['serving_ttl']._serialized_options = b'\222M\002\010\006'
  _TEMPORALARGS.fields_by_name['monitoring']._options = None
  _TEMPORALARGS.fields_by_name['monitoring']._serialized_options = b'\222M\002\010\001'
  _TEMPORALARGS.fields_by_name['backfill_config']._options = None
  _TEMPORALARGS.fields_by_name['backfill_config']._serialized_options = b'\222M\002\010\003'
  _TEMPORALAGGREGATEARGS.fields_by_name['aggregation_slide_period_duration']._options = None
  _TEMPORALAGGREGATEARGS.fields_by_name['aggregation_slide_period_duration']._serialized_options = b'\222M\002\010\005'
  _TEMPORALAGGREGATEARGS.fields_by_name['feature_start_time']._options = None
  _TEMPORALAGGREGATEARGS.fields_by_name['feature_start_time']._serialized_options = b'\222M\002\010\001'
  _TEMPORALAGGREGATEARGS.fields_by_name['monitoring']._options = None
  _TEMPORALAGGREGATEARGS.fields_by_name['monitoring']._serialized_options = b'\222M\002\010\001'
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['feature_start_time']._options = None
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['feature_start_time']._serialized_options = b'\222M\002\010\001'
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['serving_ttl']._options = None
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['serving_ttl']._serialized_options = b'\222M\002\010\006'
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['monitoring']._options = None
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['monitoring']._serialized_options = b'\222M\002\010\001\222M\002\020\001'
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['batch_trigger']._options = None
  _MATERIALIZEDFEATUREVIEWARGS.fields_by_name['batch_trigger']._serialized_options = b'\222M\002\010\001'
  _ONDEMANDARGS.fields_by_name['output_schema']._options = None
  _ONDEMANDARGS.fields_by_name['output_schema']._serialized_options = b'\202}\002\020\003'
  _ONDEMANDARGS.fields_by_name['schema']._options = None
  _ONDEMANDARGS.fields_by_name['schema']._serialized_options = b'\202}\002\010\005'
  _FEATURETABLEARGS.fields_by_name['output_schema']._options = None
  _FEATURETABLEARGS.fields_by_name['output_schema']._serialized_options = b'\202}\002\020\003'
  _FEATURETABLEARGS.fields_by_name['schema']._options = None
  _FEATURETABLEARGS.fields_by_name['schema']._serialized_options = b'\202}\002\010\005'
  _FEATURETABLEARGS.fields_by_name['serving_ttl']._options = None
  _FEATURETABLEARGS.fields_by_name['serving_ttl']._serialized_options = b'\222M\002\010\006'
  _FEATURETABLEARGS.fields_by_name['offline_config']._options = None
  _FEATURETABLEARGS.fields_by_name['offline_config']._serialized_options = b'\202}\002\020\003'
  _FEATURETABLEARGS.fields_by_name['offline_store']._options = None
  _FEATURETABLEARGS.fields_by_name['offline_store']._serialized_options = b'\202}\002\010\005'
  _FEATURETABLEARGS.fields_by_name['online_store_config']._options = None
  _FEATURETABLEARGS.fields_by_name['online_store_config']._serialized_options = b'\202}\002\020\003'
  _FEATURETABLEARGS.fields_by_name['online_store']._options = None
  _FEATURETABLEARGS.fields_by_name['online_store']._serialized_options = b'\202}\002\010\005'
  _FEATURETABLEARGS.fields_by_name['batch_materialization']._options = None
  _FEATURETABLEARGS.fields_by_name['batch_materialization']._serialized_options = b'\202}\002\020\003'
  _FEATURETABLEARGS.fields_by_name['batch_compute']._options = None
  _FEATURETABLEARGS.fields_by_name['batch_compute']._serialized_options = b'\202}\002\010\005'
  _FEATUREAGGREGATION_FUNCTIONPARAMSENTRY._options = None
  _FEATUREAGGREGATION_FUNCTIONPARAMSENTRY._serialized_options = b'8\001'
  _FEATUREAGGREGATION.fields_by_name['time_windows']._options = None
  _FEATUREAGGREGATION.fields_by_name['time_windows']._serialized_options = b'\202}\002\020\003'
  _FEATUREAGGREGATION.fields_by_name['time_window_strs']._options = None
  _FEATUREAGGREGATION.fields_by_name['time_window_strs']._serialized_options = b'\202}\002\020\003\222M\002\010\005'
  _FEATUREAGGREGATION.fields_by_name['time_window']._options = None
  _FEATUREAGGREGATION.fields_by_name['time_window']._serialized_options = b'\202}\002\010\005'
  _FEATUREAGGREGATION.fields_by_name['name']._options = None
  _FEATUREAGGREGATION.fields_by_name['name']._serialized_options = b'\202}\002\010\005\222M\002 \001'
  _CLUSTERCONFIG.fields_by_name['existing_cluster']._options = None
  _CLUSTERCONFIG.fields_by_name['existing_cluster']._serialized_options = b'\222M\002\010\001'
  _CLUSTERCONFIG.fields_by_name['new_databricks']._options = None
  _CLUSTERCONFIG.fields_by_name['new_databricks']._serialized_options = b'\222M\002\010\001'
  _CLUSTERCONFIG.fields_by_name['new_emr']._options = None
  _CLUSTERCONFIG.fields_by_name['new_emr']._serialized_options = b'\222M\002\010\001'
  _CLUSTERCONFIG.fields_by_name['implicit_config']._options = None
  _CLUSTERCONFIG.fields_by_name['implicit_config']._serialized_options = b'\222M\002\010\001\222M\002\030\005'
  _CLUSTERCONFIG.fields_by_name['json_databricks']._options = None
  _CLUSTERCONFIG.fields_by_name['json_databricks']._serialized_options = b'\222M\002\010\001'
  _CLUSTERCONFIG.fields_by_name['json_emr']._options = None
  _CLUSTERCONFIG.fields_by_name['json_emr']._serialized_options = b'\222M\002\010\001'
  _CLUSTERCONFIG.fields_by_name['json_dataproc']._options = None
  _CLUSTERCONFIG.fields_by_name['json_dataproc']._serialized_options = b'\222M\002\010\001'
  _DEFAULTCLUSTERCONFIG.fields_by_name['databricks_spark_version']._options = None
  _DEFAULTCLUSTERCONFIG.fields_by_name['databricks_spark_version']._serialized_options = b'\222M\002\030\005'
  _DEFAULTCLUSTERCONFIG.fields_by_name['emr_spark_version']._options = None
  _DEFAULTCLUSTERCONFIG.fields_by_name['emr_spark_version']._serialized_options = b'\222M\002\030\005'
  _SPARKCONFIG_SPARKCONFENTRY._options = None
  _SPARKCONFIG_SPARKCONFENTRY._serialized_options = b'8\001'
  _REDISONLINESTORE.fields_by_name['primary_endpoint']._options = None
  _REDISONLINESTORE.fields_by_name['primary_endpoint']._serialized_options = b'\222M\002\010\006'
  _REDISONLINESTORE.fields_by_name['authentication_token']._options = None
  _REDISONLINESTORE.fields_by_name['authentication_token']._serialized_options = b'\222M\002\010\001\222M\002\030\006'
  _REDISONLINESTORE.fields_by_name['tls_enabled']._options = None
  _REDISONLINESTORE.fields_by_name['tls_enabled']._serialized_options = b'\222M\002\010\001\222M\002\030\005'
  _REDISONLINESTORE.fields_by_name['enabled']._options = None
  _REDISONLINESTORE.fields_by_name['enabled']._serialized_options = b'\222M\002\030\005'
  _OFFLINEFEATURESTORECONFIG.fields_by_name['subdirectory_override']._options = None
  _OFFLINEFEATURESTORECONFIG.fields_by_name['subdirectory_override']._serialized_options = b'\222M\002\010\001'
  _MONITORINGCONFIG.fields_by_name['expected_feature_freshness']._options = None
  _MONITORINGCONFIG.fields_by_name['expected_feature_freshness']._serialized_options = b'\202}\002\020\003'
  _MONITORINGCONFIG.fields_by_name['expected_freshness']._options = None
  _MONITORINGCONFIG.fields_by_name['expected_freshness']._serialized_options = b'\202}\002\010\005'
  _MONITORINGCONFIG.fields_by_name['alert_email']._options = None
  _MONITORINGCONFIG.fields_by_name['alert_email']._serialized_options = b'\362\342\002\002\010\001'
  _FEATUREVIEWTYPE._serialized_start=10449
  _FEATUREVIEWTYPE._serialized_end=10682
  _BACKFILLCONFIGMODE._serialized_start=10685
  _BACKFILLCONFIGMODE._serialized_end=10872
  _STREAMPROCESSINGMODE._serialized_start=10875
  _STREAMPROCESSINGMODE._serialized_end=11014
  _BATCHTRIGGERTYPE._serialized_start=11017
  _BATCHTRIGGERTYPE._serialized_end=11181
  _FEATUREVIEWARGS._serialized_start=583
  _FEATUREVIEWARGS._serialized_end=1966
  _ENTITYKEYOVERRIDE._serialized_start=1968
  _ENTITYKEYOVERRIDE._serialized_end=2070
  _BACKFILLCONFIG._serialized_start=2072
  _BACKFILLCONFIG._serialized_end=2147
  _OUTPUTSTREAM._serialized_start=2150
  _OUTPUTSTREAM._serialized_end=2356
  _TEMPORALARGS._serialized_start=2359
  _TEMPORALARGS._serialized_end=3440
  _TEMPORALAGGREGATEARGS._serialized_start=3443
  _TEMPORALAGGREGATEARGS._serialized_end=4572
  _MATERIALIZEDFEATUREVIEWARGS._serialized_start=4575
  _MATERIALIZEDFEATUREVIEWARGS._serialized_end=5920
  _ONDEMANDARGS._serialized_start=5923
  _ONDEMANDARGS._serialized_end=6080
  _FEATURETABLEARGS._serialized_start=6083
  _FEATURETABLEARGS._serialized_end=6838
  _FEATUREAGGREGATION._serialized_start=6841
  _FEATUREAGGREGATION._serialized_end=7333
  _FEATUREAGGREGATION_FUNCTIONPARAMSENTRY._serialized_start=7237
  _FEATUREAGGREGATION_FUNCTIONPARAMSENTRY._serialized_end=7333
  _PARAMVALUE._serialized_start=7335
  _PARAMVALUE._serialized_end=7391
  _CLUSTERCONFIG._serialized_start=7394
  _CLUSTERCONFIG._serialized_end=8011
  _JSONCLUSTERCONFIG._serialized_start=8013
  _JSONCLUSTERCONFIG._serialized_end=8077
  _EXISTINGCLUSTERCONFIG._serialized_start=8079
  _EXISTINGCLUSTERCONFIG._serialized_end=8150
  _NEWCLUSTERCONFIG._serialized_start=8153
  _NEWCLUSTERCONFIG._serialized_end=8568
  _DEFAULTCLUSTERCONFIG._serialized_start=8571
  _DEFAULTCLUSTERCONFIG._serialized_end=8709
  _SPARKCONFIG._serialized_start=8712
  _SPARKCONFIG._serialized_end=9099
  _SPARKCONFIG_SPARKCONFENTRY._serialized_start=9039
  _SPARKCONFIG_SPARKCONFENTRY._serialized_end=9099
  _ONLINESTORECONFIG._serialized_start=9102
  _ONLINESTORECONFIG._serialized_end=9262
  _DYNAMODBONLINESTORE._serialized_start=9265
  _DYNAMODBONLINESTORE._serialized_end=9554
  _REDISONLINESTORE._serialized_start=9557
  _REDISONLINESTORE._serialized_end=9833
  _OFFLINEFEATURESTORECONFIG._serialized_start=9836
  _OFFLINEFEATURESTORECONFIG._serialized_end=10055
  _PARQUETCONFIG._serialized_start=10057
  _PARQUETCONFIG._serialized_end=10072
  _DELTACONFIG._serialized_start=10074
  _DELTACONFIG._serialized_end=10162
  _MONITORINGCONFIG._serialized_start=10165
  _MONITORINGCONFIG._serialized_end=10446
# @@protoc_insertion_point(module_scope)
