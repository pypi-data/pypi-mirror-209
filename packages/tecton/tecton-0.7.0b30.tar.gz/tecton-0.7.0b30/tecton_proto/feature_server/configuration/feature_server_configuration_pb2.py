# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/feature_server/configuration/feature_server_configuration.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tecton_proto.args import pipeline_pb2 as tecton__proto_dot_args_dot_pipeline__pb2
from tecton_proto.auth import acl_pb2 as tecton__proto_dot_auth_dot_acl__pb2
from tecton_proto.common import aggregation_function_pb2 as tecton__proto_dot_common_dot_aggregation__function__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2
from tecton_proto.data import feature_service_pb2 as tecton__proto_dot_data_dot_feature__service__pb2
from tecton_proto.data import feature_view_pb2 as tecton__proto_dot_data_dot_feature__view__pb2
from tecton_proto.data import tecton_api_key_pb2 as tecton__proto_dot_data_dot_tecton__api__key__pb2
from tecton_proto.data import transformation_pb2 as tecton__proto_dot_data_dot_transformation__pb2
from tecton_proto.common import data_type_pb2 as tecton__proto_dot_common_dot_data__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLtecton_proto/feature_server/configuration/feature_server_configuration.proto\x12)tecton_proto.feature_server.configuration\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a tecton_proto/args/pipeline.proto\x1a\x1btecton_proto/auth/acl.proto\x1a.tecton_proto/common/aggregation_function.proto\x1a\x1ctecton_proto/common/id.proto\x1a\'tecton_proto/data/feature_service.proto\x1a$tecton_proto/data/feature_view.proto\x1a&tecton_proto/data/tecton_api_key.proto\x1a&tecton_proto/data/transformation.proto\x1a#tecton_proto/common/data_type.proto\"\xeb\x01\n\x0c\x46\x65\x61turesPlan\x12[\n\x0c\x66\x65\x61ture_plan\x18\x01 \x01(\x0b\x32\x36.tecton_proto.feature_server.configuration.FeaturePlanH\x00R\x0b\x66\x65\x61turePlan\x12x\n\x17on_demand_features_plan\x18\x02 \x01(\x0b\x32?.tecton_proto.feature_server.configuration.OnDemandFeaturesPlanH\x00R\x14onDemandFeaturesPlanB\x04\n\x02\x66p\"\xec\x01\n\x06\x43olumn\x12:\n\tdata_type\x18\x05 \x01(\x0b\x32\x1d.tecton_proto.common.DataTypeR\x08\x64\x61taType\x12\x35\n\x17\x66\x65\x61ture_view_space_name\x18\x02 \x01(\tR\x14\x66\x65\x61tureViewSpaceName\x12;\n\x1a\x66\x65\x61ture_service_space_name\x18\x03 \x01(\tR\x17\x66\x65\x61tureServiceSpaceName\x12,\n\x12\x66\x65\x61ture_view_index\x18\x04 \x01(\x05R\x10\x66\x65\x61tureViewIndexJ\x04\x08\x01\x10\x02\"\xab\x0b\n\x0b\x46\x65\x61turePlan\x12V\n\routput_column\x18\x04 \x01(\x0b\x32\x31.tecton_proto.feature_server.configuration.ColumnR\x0coutputColumn\x12V\n\rinput_columns\x18\x01 \x03(\x0b\x32\x31.tecton_proto.feature_server.configuration.ColumnR\x0cinputColumns\x12[\n\x14\x61ggregation_function\x18\x03 \x01(\x0e\x32(.tecton_proto.common.AggregationFunctionR\x13\x61ggregationFunction\x12n\n\x1b\x61ggregation_function_params\x18\x06 \x01(\x0b\x32..tecton_proto.common.AggregationFunctionParamsR\x19\x61ggregationFunctionParams\x12H\n\x12\x61ggregation_window\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11\x61ggregationWindow\x12N\n\tjoin_keys\x18\x07 \x03(\x0b\x32\x31.tecton_proto.feature_server.configuration.ColumnR\x08joinKeys\x12_\n\x12wildcard_join_keys\x18\x08 \x03(\x0b\x32\x31.tecton_proto.feature_server.configuration.ColumnR\x10wildcardJoinKeys\x12\x1d\n\ntable_name\x18\t \x01(\tR\ttableName\x12|\n\x19\x64\x61ta_table_timestamp_type\x18\x0f \x01(\x0e\x32\x41.tecton_proto.feature_server.configuration.DataTableTimestampTypeR\x16\x64\x61taTableTimestampType\x12\x82\x01\n\x1bstatus_table_timestamp_type\x18\x10 \x01(\x0e\x32\x43.tecton_proto.feature_server.configuration.StatusTableTimestampTypeR\x18statusTableTimestampType\x12#\n\rtimestamp_key\x18\x0c \x01(\tR\x0ctimestampKey\x12<\n\x0cslide_period\x18\r \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bslidePeriod\x12:\n\x0bserving_ttl\x18\x0e \x01(\x0b\x32\x19.google.protobuf.DurationR\nservingTtl\x12\x30\n\x14refresh_status_table\x18\x11 \x01(\x08R\x12refreshStatusTable\x12*\n\x11\x66\x65\x61ture_view_name\x18\x15 \x01(\tR\x0f\x66\x65\x61tureViewName\x12&\n\x0f\x66\x65\x61ture_view_id\x18\x17 \x01(\tR\rfeatureViewId\x12?\n\x1c\x66\x65\x61ture_store_format_version\x18\x12 \x01(\x05R\x19\x66\x65\x61tureStoreFormatVersion\x12T\n\x13online_store_params\x18\x13 \x01(\x0b\x32$.tecton_proto.data.OnlineStoreParamsR\x11onlineStoreParams\x12.\n\x12\x64\x65letionTimeWindow\x18\x16 \x01(\x03R\x12\x64\x65letionTimeWindowJ\x04\x08\x02\x10\x03J\x04\x08\n\x10\x0bJ\x04\x08\x0b\x10\x0cJ\x04\x08\x14\x10\x15\"g\n\x11\x46\x65\x61tureVectorPlan\x12R\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x36.tecton_proto.feature_server.configuration.FeaturePlanR\x08\x66\x65\x61tures\"\xc1\x05\n\x14OnDemandFeaturesPlan\x12l\n\x19\x61rgs_from_request_context\x18\x02 \x03(\x0b\x32\x31.tecton_proto.feature_server.configuration.ColumnR\x16\x61rgsFromRequestContext\x12K\n\x07outputs\x18\x03 \x03(\x0b\x32\x31.tecton_proto.feature_server.configuration.ColumnR\x07outputs\x12\x83\x01\n\x12\x66\x65\x61ture_set_inputs\x18\x05 \x03(\x0b\x32U.tecton_proto.feature_server.configuration.OnDemandFeaturesPlan.FeatureSetInputsEntryR\x10\x66\x65\x61tureSetInputs\x12\x37\n\x08pipeline\x18\x06 \x01(\x0b\x32\x1b.tecton_proto.args.PipelineR\x08pipeline\x12K\n\x0ftransformations\x18\x07 \x03(\x0b\x32!.tecton_proto.data.TransformationR\x0ftransformations\x12*\n\x11\x66\x65\x61ture_view_name\x18\x08 \x01(\tR\x0f\x66\x65\x61tureViewName\x12&\n\x0f\x66\x65\x61ture_view_id\x18\t \x01(\tR\rfeatureViewId\x1a\x81\x01\n\x15\x46\x65\x61tureSetInputsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12R\n\x05value\x18\x02 \x01(\x0b\x32<.tecton_proto.feature_server.configuration.FeatureVectorPlanR\x05value:\x02\x38\x01J\x04\x08\x01\x10\x02J\x04\x08\x04\x10\x05\"\x81\x01\n\rLoggingConfig\x12\x1f\n\x0bsample_rate\x18\x01 \x01(\x02R\nsampleRate\x12.\n\x13log_effective_times\x18\x02 \x01(\x08R\x11logEffectiveTimes\x12\x1f\n\x0b\x61vro_schema\x18\x03 \x01(\tR\navroSchema\"\x8d\x05\n\x12\x46\x65\x61tureServicePlan\x12\x45\n\x12\x66\x65\x61ture_service_id\x18\x04 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x10\x66\x65\x61tureServiceId\x12?\n\x0f\x66\x65\x61ture_view_id\x18\n \x01(\x0b\x32\x17.tecton_proto.common.IdR\rfeatureViewId\x12\x30\n\x14\x66\x65\x61ture_service_name\x18\x02 \x01(\tR\x12\x66\x65\x61tureServiceName\x12*\n\x11\x66\x65\x61ture_view_name\x18\t \x01(\tR\x0f\x66\x65\x61tureViewName\x12%\n\x0eworkspace_name\x18\x08 \x01(\tR\rworkspaceName\x12^\n\x0e\x66\x65\x61tures_plans\x18\r \x03(\x0b\x32\x37.tecton_proto.feature_server.configuration.FeaturesPlanR\rfeaturesPlans\x12N\n\x11join_key_template\x18\x05 \x01(\x0b\x32\".tecton_proto.data.JoinKeyTemplateR\x0fjoinKeyTemplate\x12\x41\n\x10\x66\x65\x61ture_view_ids\x18\x06 \x03(\x0b\x32\x17.tecton_proto.common.IdR\x0e\x66\x65\x61tureViewIds\x12_\n\x0elogging_config\x18\x0c \x01(\x0b\x32\x38.tecton_proto.feature_server.configuration.LoggingConfigR\rloggingConfigJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04J\x04\x08\x07\x10\x08J\x04\x08\x0b\x10\x0c\"\x80\x04\n\x11GlobalTableConfig\x12?\n\x0f\x66\x65\x61ture_view_id\x18\x04 \x01(\x0b\x32\x17.tecton_proto.common.IdR\rfeatureViewId\x12<\n\x0cslide_period\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bslidePeriod\x12\x12\n\x04size\x18\x03 \x01(\x05R\x04size\x12\x82\x01\n\x1bstatus_table_timestamp_type\x18\x06 \x01(\x0e\x32\x43.tecton_proto.feature_server.configuration.StatusTableTimestampTypeR\x18statusTableTimestampType\x12\x30\n\x14refresh_status_table\x18\x07 \x01(\x08R\x12refreshStatusTable\x12?\n\x1c\x66\x65\x61ture_store_format_version\x18\x08 \x01(\x05R\x19\x66\x65\x61tureStoreFormatVersion\x12T\n\x13online_store_params\x18\t \x01(\x0b\x32$.tecton_proto.data.OnlineStoreParamsR\x11onlineStoreParamsJ\x04\x08\x01\x10\x02J\x04\x08\x05\x10\x06\"\x87\x01\n\x12\x46\x65\x61tureServiceAcls\x12\x45\n\x12\x66\x65\x61ture_service_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x10\x66\x65\x61tureServiceId\x12*\n\x04\x61\x63ls\x18\x02 \x03(\x0b\x32\x16.tecton_proto.auth.AclR\x04\x61\x63ls\"b\n\rWorkspaceAcls\x12%\n\x0eworkspace_name\x18\x01 \x01(\tR\rworkspaceName\x12*\n\x04\x61\x63ls\x18\x02 \x03(\x0b\x32\x16.tecton_proto.auth.AclR\x04\x61\x63ls\"\xf5\x06\n\x1a\x46\x65\x61tureServerConfiguration\x12?\n\rcomputed_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x63omputedTime\x12h\n\x10\x66\x65\x61ture_services\x18\x01 \x03(\x0b\x32=.tecton_proto.feature_server.configuration.FeatureServicePlanR\x0f\x66\x65\x61tureServices\x12\xa0\x01\n\x1bglobal_table_config_by_name\x18\x03 \x03(\x0b\x32\x62.tecton_proto.feature_server.configuration.FeatureServerConfiguration.GlobalTableConfigByNameEntryR\x17globalTableConfigByName\x12O\n\x13\x61uthorized_api_keys\x18\x04 \x03(\x0b\x32\x1f.tecton_proto.data.TectonApiKeyR\x11\x61uthorizedApiKeys\x12o\n\x14\x66\x65\x61ture_service_acls\x18\x05 \x03(\x0b\x32=.tecton_proto.feature_server.configuration.FeatureServiceAclsR\x12\x66\x65\x61tureServiceAcls\x12_\n\x0eworkspace_acls\x18\x06 \x03(\x0b\x32\x38.tecton_proto.feature_server.configuration.WorkspaceAclsR\rworkspaceAcls\x12[\n\x17\x61ll_online_store_params\x18\x07 \x03(\x0b\x32$.tecton_proto.data.OnlineStoreParamsR\x14\x61llOnlineStoreParams\x1a\x88\x01\n\x1cGlobalTableConfigByNameEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12R\n\x05value\x18\x02 \x01(\x0b\x32<.tecton_proto.feature_server.configuration.GlobalTableConfigR\x05value:\x02\x38\x01*\x90\x01\n\x16\x44\x61taTableTimestampType\x12%\n!DATA_TABLE_TIMESTAMP_TYPE_UNKNOWN\x10\x00\x12&\n\"DATA_TABLE_TIMESTAMP_TYPE_SORT_KEY\x10\x01\x12\'\n#DATA_TABLE_TIMESTAMP_TYPE_ATTRIBUTE\x10\x02*\x98\x01\n\x18StatusTableTimestampType\x12\'\n#STATUS_TABLE_TIMESTAMP_TYPE_UNKNOWN\x10\x00\x12(\n$STATUS_TABLE_TIMESTAMP_TYPE_SORT_KEY\x10\x01\x12)\n%STATUS_TABLE_TIMESTAMP_TYPE_ATTRIBUTE\x10\x02\x42l\n(com.tecton.feature_service.configurationP\x01Z>github.com/tecton-ai/tecton_proto/feature_server/configuration')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.feature_server.configuration.feature_server_configuration_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.tecton.feature_service.configurationP\001Z>github.com/tecton-ai/tecton_proto/feature_server/configuration'
  _ONDEMANDFEATURESPLAN_FEATURESETINPUTSENTRY._options = None
  _ONDEMANDFEATURESPLAN_FEATURESETINPUTSENTRY._serialized_options = b'8\001'
  _FEATURESERVERCONFIGURATION_GLOBALTABLECONFIGBYNAMEENTRY._options = None
  _FEATURESERVERCONFIGURATION_GLOBALTABLECONFIGBYNAMEENTRY._serialized_options = b'8\001'
  _DATATABLETIMESTAMPTYPE._serialized_start=5699
  _DATATABLETIMESTAMPTYPE._serialized_end=5843
  _STATUSTABLETIMESTAMPTYPE._serialized_start=5846
  _STATUSTABLETIMESTAMPTYPE._serialized_end=5998
  _FEATURESPLAN._serialized_start=526
  _FEATURESPLAN._serialized_end=761
  _COLUMN._serialized_start=764
  _COLUMN._serialized_end=1000
  _FEATUREPLAN._serialized_start=1003
  _FEATUREPLAN._serialized_end=2454
  _FEATUREVECTORPLAN._serialized_start=2456
  _FEATUREVECTORPLAN._serialized_end=2559
  _ONDEMANDFEATURESPLAN._serialized_start=2562
  _ONDEMANDFEATURESPLAN._serialized_end=3267
  _ONDEMANDFEATURESPLAN_FEATURESETINPUTSENTRY._serialized_start=3126
  _ONDEMANDFEATURESPLAN_FEATURESETINPUTSENTRY._serialized_end=3255
  _LOGGINGCONFIG._serialized_start=3270
  _LOGGINGCONFIG._serialized_end=3399
  _FEATURESERVICEPLAN._serialized_start=3402
  _FEATURESERVICEPLAN._serialized_end=4055
  _GLOBALTABLECONFIG._serialized_start=4058
  _GLOBALTABLECONFIG._serialized_end=4570
  _FEATURESERVICEACLS._serialized_start=4573
  _FEATURESERVICEACLS._serialized_end=4708
  _WORKSPACEACLS._serialized_start=4710
  _WORKSPACEACLS._serialized_end=4808
  _FEATURESERVERCONFIGURATION._serialized_start=4811
  _FEATURESERVERCONFIGURATION._serialized_end=5696
  _FEATURESERVERCONFIGURATION_GLOBALTABLECONFIGBYNAMEENTRY._serialized_start=5560
  _FEATURESERVERCONFIGURATION_GLOBALTABLECONFIGBYNAMEENTRY._serialized_end=5696
# @@protoc_insertion_point(module_scope)
