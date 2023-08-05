import logging
from typing import List
from typing import Optional
from typing import Union

from tecton._internals import errors
from tecton._internals import metadata_service
from tecton._internals.display import Displayable
from tecton._internals.sdk_decorators import documented_by
from tecton._internals.sdk_decorators import sdk_public_method
from tecton._internals.utils import format_freshness_table
from tecton._internals.utils import get_all_freshness
from tecton._internals.utils import is_live_workspace
from tecton.framework import data_source as framework_data_source
from tecton.framework import entity as framework_entity
from tecton.framework import feature_service as framework_feature_service
from tecton.framework import feature_view as framework_feature_view
from tecton.framework import transformation as framework_transformation
from tecton.framework.dataset import Dataset
from tecton_core import specs
from tecton_core.fco_container import FcoContainer
from tecton_core.feature_definition_wrapper import FrameworkVersion
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllEntitiesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllFeatureServicesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllSavedFeatureDataFramesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllTransformationsRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetAllVirtualDataSourcesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetEntityRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetFeatureServiceRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetFeatureViewRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetSavedFeatureDataFrameRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetTransformationRequest
from tecton_proto.metadataservice.metadata_service_pb2 import GetVirtualDataSourceRequest
from tecton_proto.metadataservice.metadata_service_pb2 import ListWorkspacesRequest
from tecton_proto.metadataservice.metadata_service_pb2 import QueryFeatureViewsRequest


logger = logging.getLogger(__name__)


class Workspace:
    """
    Workspace class.

    This class represents a Workspace. The Workspace class is used to fetch Tecton Objects, which are stored in a Workspace.

    Examples of using the Workspace methods for accessing Tecton first class objects:

    .. code-block:: python

        import tecton


        workspace = tecton.get_workspace("my_workspace")

        # For a specified workspace, list high-level registered Objects
        print(f" Entities            : {workspace.list_entities()}")
        print(f" Feature Data Sources: {workspace.list_data_sources()}")
        print(f" Feature Views       : {workspace.list_feature_views()}")
        print(f" Feature Services    : {workspace.list_feature_services()}")
        print(f" Transformations     : {workspace.list_transformations()}")
        print(f" Feature Tables      : {workspace.list_feature_tables()}")
        print(f" List of Workspaces  : {tecton.list_workspaces()}")

    .. code-block:: Text

        The output:

        Entities            : ['ad', 'auction', 'content', 'ContentKeyword', 'ads_user', 'fraud_user']
        Feature Data Sources: ['ad_impressions_stream', 'ad_impressions_batch', 'transactions_stream', 'transactions_batch',
                                'users_batch', 'credit_scores_batch']
        Feature Views       : ['user_has_great_credit', 'user_age', 'transaction_amount_is_high',
                               'transaction_amount_is_higher_than_average', 'transaction_bucketing', 'user_ctr_7d_2',
                               ...
                               'user_ad_impression_counts', 'content_keyword_click_counts']
        Feature Services    : ['ad_ctr_feature_service', 'fraud_detection_feature_service',
                                'fraud_detection_feature_service:v2', 'minimal_fs', 'continuous_feature_service']
        Transformations     : ['content_keyword_click_counts', 'user_ad_impression_counts', 'user_click_counts',
                               'user_impression_counts', 'user_ctr_7d', 'user_ctr_7d_2', 'user_distinct_ad_count_7d',
                               ...
                               'weekend_transaction_count_n_days', 'user_has_good_credit_sql']
        Feature Tables      : ['user_login_counts', 'user_page_click_feature_table']
        List of Workspaces  : ['jsd_tecton_wksp, 'kafka_streaming_staging, 'kafka_streaming_production',
                               ...
                               'on_demand_streaming_aggregation_pipeline']

    """

    def __init__(self, workspace: str, _is_live: Optional[bool] = None, _validate: bool = True):
        """
        Fetch an existing :class:`tecton.Workspace` by name.

        :param workspace: Workspace name.
        """
        self.workspace = workspace

        if _is_live is None:
            self.is_live = is_live_workspace(self.workspace)
        else:
            self.is_live = _is_live

        if _validate:
            self._validate()

    def _validate(self):
        request = ListWorkspacesRequest()
        response = metadata_service.instance().ListWorkspaces(request)

        workspace_from_resp = None
        for ws in response.workspaces:
            if ws.name == self.workspace:
                workspace_from_resp = ws
                break

        if workspace_from_resp is None:
            raise errors.NONEXISTENT_WORKSPACE(self.workspace, response.workspaces)

        if ws.capabilities.materializable != self.is_live:
            raise errors.INCORRECT_MATERIALIZATION_ENABLED_FLAG(self.is_live, ws.capabilities.materializable)

    @classmethod
    @sdk_public_method
    # TODO(TEC-13678): consolidate with tecton.list_workspaces() and remove this
    def get_all(self) -> List["Workspace"]:
        """Deprecated. Use tecton.list_workspaces() instead. Returns a list of all registered Workspaces.

        :return: A list of Workspace objects.
        """
        logger.warn("get_all() is deprecated. Use tecton.list_workspaces() instead.")
        request = ListWorkspacesRequest()
        response = metadata_service.instance().ListWorkspaces(request)
        workspaces = [
            Workspace(ws.name, _is_live=ws.capabilities.materializable, _validate=False) for ws in response.workspaces
        ]

        # Return live workspaces first (alphabetical), then development workspaces.
        return sorted(workspaces, key=lambda ws: (not ws.is_live, ws.workspace))

    def __repr__(self) -> str:
        capability_str = "Live" if self.is_live else "Development"
        return f"{self.workspace} ({capability_str})"

    @sdk_public_method
    def summary(self) -> Displayable:
        """Returns workspace metadata.

        :return: Displayable of metadata for this workspace. Use `to_dict()` for a parseable representation.
        """
        items = [
            ("Workspace Name", self.workspace),
            ("Workspace Type", "Live" if self.is_live else "Development"),
        ]
        return Displayable.from_properties(items=items)

    @classmethod
    @sdk_public_method
    def get(cls, name) -> "Workspace":
        """Returns a :class:`tecton.Workspace` instance for the workspace with the provided name.

        :param name: The name of the workspace to retrieve.
        """
        return Workspace(name)

    @sdk_public_method
    def get_feature_view(self, name: str) -> framework_feature_view.FeatureView:
        """Returns a Feature View that has been applied to a workspace.

        :param name: The name of the Feature View to retrieve.
        """
        request = GetFeatureViewRequest(version_specifier=name, workspace=self.workspace)
        response = metadata_service.instance().GetFeatureView(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        feature_view_spec = fco_container.get_single_root()

        if feature_view_spec is None:
            msg = f"Feature View '{name}' not found. Try running `workspace.list_feature_views()` to view all registered Feature Views."
            raise errors.TectonValidationError(msg)

        assert isinstance(feature_view_spec, specs.FeatureViewSpec)

        if isinstance(feature_view_spec, specs.FeatureTableSpec):
            msg = f"Feature View '{name}' not found. Did you mean workspace.get_feature_table('{name}')?"
            raise errors.TectonValidationError(msg)

        return framework_feature_view.feature_view_from_spec(feature_view_spec, fco_container)

    @sdk_public_method
    def get_feature_table(self, name: str) -> framework_feature_view.FeatureTable:
        """Returns a Feature Table that has been applied to a workspace.

        :param name: The name of the Feature Table to retrieve.
        """
        request = GetFeatureViewRequest(version_specifier=name, workspace=self.workspace)
        response = metadata_service.instance().GetFeatureView(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        feature_table_spec = fco_container.get_single_root()

        if feature_table_spec is None:
            msg = f"Feature Table '{name}' not found. Try running `workspace.list_feature_tables()` to view all registered Feature Tables."
            raise errors.TectonValidationError(msg)

        assert isinstance(feature_table_spec, specs.FeatureViewSpec)
        ft_proto = feature_table_spec.data_proto

        if not ft_proto.HasField("feature_table"):
            msg = f"Feature Table '{name}' not found. Did you mean workspace.get_feature_view('{name}')?"
            raise errors.TectonValidationError(msg)

        if ft_proto.fco_metadata.framework_version != FrameworkVersion.FWV5.value:
            raise errors.UNSUPPORTED_FRAMEWORK_VERSION

        return framework_feature_view.FeatureTable._from_spec(feature_table_spec, fco_container)

    @sdk_public_method
    def get_feature_service(self, name: str) -> framework_feature_service.FeatureService:
        """Returns a Feature Service that has been applied to a workspace.

        :param name: The name of the Feature Service to retrieve.
        """
        request = GetFeatureServiceRequest(service_reference=name, workspace=self.workspace)
        response = metadata_service.instance().GetFeatureService(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        feature_service_spec = fco_container.get_single_root()

        if feature_service_spec is None:
            msg = f"Feature Service '{name}' not found. Try running `workspace.list_feature_services()` to view all registered Feature Services."
            raise errors.TectonValidationError(msg)

        assert isinstance(feature_service_spec, specs.FeatureServiceSpec)

        return framework_feature_service.FeatureService._from_spec(feature_service_spec, fco_container)

    @sdk_public_method
    def get_data_source(
        self, name: str
    ) -> Union[
        framework_data_source.PushSource,
        framework_data_source.BatchSource,
        framework_data_source.StreamSource,
    ]:
        """Returns a Data Source that has been applied to a workspace.

        :param name: The name of the Data Source to retrieve.
        """
        request = GetVirtualDataSourceRequest(name=name, workspace=self.workspace)
        response = metadata_service.instance().GetVirtualDataSource(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        data_source_spec = fco_container.get_single_root()

        if data_source_spec is None:
            msg = f"Data Source '{name}' not found. Try running `workspace.list_data_sources()` to view all registered Data Sources."
            raise errors.TectonValidationError(msg)

        assert isinstance(data_source_spec, specs.DataSourceSpec)
        ds_proto = data_source_spec.data_proto

        if ds_proto.fco_metadata.framework_version != FrameworkVersion.FWV5.value:
            raise errors.UNSUPPORTED_FRAMEWORK_VERSION

        return framework_data_source.data_source_from_spec(data_source_spec)

    @sdk_public_method
    def get_entity(self, name: str) -> framework_entity.Entity:
        """Returns an Entity that has been applied to a workspace.

        :param name: The name of the Entity to retrieve.
        """

        request = GetEntityRequest(name=name, workspace=self.workspace)
        response = metadata_service.instance().GetEntity(request)

        fco_container = FcoContainer.from_proto(response.fco_container)
        entity_spec = fco_container.get_single_root()

        if entity_spec is None:
            msg = f"Entity '{name}' not found. Try running `workspace.list_entities()` to view all registered Entities."
            raise errors.TectonValidationError(msg)

        assert isinstance(entity_spec, specs.EntitySpec)

        return framework_entity.Entity._from_spec(entity_spec)

    @sdk_public_method
    def get_transformation(self, name: str) -> framework_transformation.Transformation:
        """Returns a Transformation that has been applied to a workspace.

        :param name: The name of the Transformation to retrieve.
        """
        request = GetTransformationRequest(name=name, workspace=self.workspace)
        response = metadata_service.instance().GetTransformation(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        transformation_spec = fco_container.get_single_root()

        if transformation_spec is None:
            msg = f"Transformation '{name}' not found. Try running `workspace.list_transformations()` to view all registered Transformations."
            raise errors.TectonValidationError(msg)

        assert isinstance(transformation_spec, specs.TransformationSpec)
        return framework_transformation.Transformation._from_spec(transformation_spec)

    @sdk_public_method
    def get_dataset(self, name: str) -> Dataset:
        """Returns a Dataset that has been saved to this workspace.

        :param name: The name of the Dataset to retrieve.
        """
        request = GetSavedFeatureDataFrameRequest(saved_feature_dataframe_name=name, workspace=self.workspace)
        response = metadata_service.instance().GetSavedFeatureDataFrame(request)

        return Dataset._from_proto(response.saved_feature_dataframe)

    @sdk_public_method
    def list_datasets(self) -> List[str]:
        """Returns a list of all saved Datasets within a workspace.

        :return: List of strings of dataset names"""
        request = GetAllSavedFeatureDataFramesRequest(workspace=self.workspace)
        response = metadata_service.instance().GetAllSavedFeatureDataFrames(request)
        return sorted([sfdf.info.name for sfdf in response.saved_feature_dataframes])

    @sdk_public_method
    def list_feature_views(self) -> List[str]:
        """Returns a list of all registered Feature Views within a workspace.

        :return: List of strings of feature view names"""
        request = QueryFeatureViewsRequest(workspace=self.workspace)
        response = metadata_service.instance().QueryFeatureViews(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        return sorted(
            [spec.name for spec in fco_container.get_root_fcos() if not isinstance(spec, specs.FeatureTableSpec)]
        )

    @sdk_public_method
    def list_feature_services(self) -> List[str]:
        """Returns a list of all registered Feature Services within a workspace.

        :return: List of strings of feature service names"""
        request = GetAllFeatureServicesRequest()
        request.workspace = self.workspace
        response = metadata_service.instance().GetAllFeatureServices(request)
        return sorted([proto.fco_metadata.name for proto in response.feature_services])

    @sdk_public_method
    def list_transformations(self) -> List[str]:
        """Returns a list of all registered Transformations within a workspace.

        :return: List of strings of transformation names"""
        request = GetAllTransformationsRequest(workspace=self.workspace)
        response = metadata_service.instance().GetAllTransformations(request)
        return sorted([proto.fco_metadata.name for proto in response.transformations])

    @sdk_public_method
    def list_entities(self) -> List[str]:
        """Returns a list of all registered Entities within a workspace.

        :return: List of strings of entity names"""
        request = GetAllEntitiesRequest(workspace=self.workspace)
        response = metadata_service.instance().GetAllEntities(request)
        return sorted([proto.fco_metadata.name for proto in response.entities])

    @sdk_public_method
    def list_data_sources(self) -> List[str]:
        """Returns a list of all registered Data Sources within a workspace.

        :return: List of strings of data source names"""
        request = GetAllVirtualDataSourcesRequest(workspace=self.workspace)
        response = metadata_service.instance().GetAllVirtualDataSources(request)
        return sorted([proto.fco_metadata.name for proto in response.virtual_data_sources])

    @sdk_public_method
    def list_feature_tables(self) -> List[str]:
        """Returns a list of all registered Feature Tables within a workspace.

        :return: List of strings of feature table names"""
        request = QueryFeatureViewsRequest(workspace=self.workspace)
        response = metadata_service.instance().QueryFeatureViews(request)
        fco_container = FcoContainer.from_proto(response.fco_container)
        return sorted([spec.name for spec in fco_container.get_root_fcos() if isinstance(spec, specs.FeatureTableSpec)])

    @sdk_public_method
    def get_feature_freshness(self) -> Union[Displayable, str]:
        """Returns feature freshness status for Feature Views and Tables.

        :return: Displayable containing freshness statuses for all features. Use `to_dict()` for a parseable representation.
        """
        freshness_statuses = get_all_freshness(self.workspace)

        if len(freshness_statuses) == 0:
            return "No Feature Views found in this workspace"
        return format_freshness_table(freshness_statuses)


@sdk_public_method
@documented_by(Workspace.get)
def get_workspace(name: str):
    return Workspace.get(name)


@sdk_public_method
# Deprecated methods - kept around so that there is a helpful error message. Can be cleaned up after the 0.6 cut.
def get_feature_service(name: str, workspace_name: Optional[str] = None):
    msg = 'get_feature_service must be called from a Workspace object. E.g. tecton.get_workspace("<workspace>").get_feature_service("<feature service>").'
    raise errors.TectonValidationError(msg)


@sdk_public_method
# Deprecated methods - kept around so that there is a helpful error message. Can be cleaned up after the 0.6 cut.
def get_feature_table(ft_reference: str, workspace_name: Optional[str] = None):
    msg = 'get_feature_table must be called from a Workspace object. E.g. tecton.get_workspace("<workspace>").get_feature_table("<feature table>").'
    raise errors.TectonValidationError(msg)


@sdk_public_method
# Deprecated methods - kept around so that there is a helpful error message. Can be cleaned up after the 0.6 cut.
def get_feature_view(fv_reference: str, workspace_name: Optional[str] = None):
    msg = 'get_feature_view must be called from a Workspace object. E.g. tecton.get_workspace("<workspace>").get_feature_view("<feature view>").'
    raise errors.TectonValidationError(msg)


@sdk_public_method
# Deprecated methods - kept around so that there is a helpful error message. Can be cleaned up after the 0.6 cut.
def get_entity(name: str, workspace_name: Optional[str] = None):
    msg = 'get_entity must be called from a Workspace object. E.g. tecton.get_workspace("<workspace>").get_entity("<entity>").'
    raise errors.TectonValidationError(msg)


@sdk_public_method
# Deprecated methods - kept around so that there is a helpful error message. Can be cleaned up after the 0.6 cut.
def get_transformation(name, workspace_name: Optional[str] = None):
    msg = 'get_transformation must be called from a Workspace object. E.g. tecton.get_workspace("<workspace>").get_transformation("<transformation>").'
    raise errors.TectonValidationError(msg)


@sdk_public_method
# Deprecated methods - kept around so that there is a helpful error message. Can be cleaned up after the 0.6 cut.
def get_data_source(name, workspace_name: Optional[str] = None):
    msg = 'get_data_source must be called from a Workspace object. E.g. tecton.get_workspace("<workspace>").get_data_source("<data source>").'
    raise errors.TectonValidationError(msg)
