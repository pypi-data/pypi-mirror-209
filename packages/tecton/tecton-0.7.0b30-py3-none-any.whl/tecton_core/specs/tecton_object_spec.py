from typing import Dict
from typing import Optional

import attrs
import pendulum
from typeguard import typechecked

from tecton_core import id_helper
from tecton_core.specs import utils
from tecton_proto.args import basic_info_pb2
from tecton_proto.common import framework_version_pb2
from tecton_proto.common import id_pb2
from tecton_proto.data import fco_metadata_pb2

__all__ = [
    "TectonObjectSpec",
]


@utils.frozen_strict
class TectonObjectMetadataSpec:
    """Spec for all basic Tecton object metadata that should be common to all Tecton objects."""

    name: str
    id: str

    description: Optional[str]
    tags: Dict[str, str]
    owner: Optional[str]
    created_at: Optional[pendulum.DateTime] = attrs.field(metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True})
    workspace: Optional[str] = attrs.field(metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True})

    framework_version: framework_version_pb2.FrameworkVersion.ValueType

    # True if this spec represents an object that was defined locally, as opposed to an "applied" object definition
    # retrieved from the backend.
    is_local_object: bool = attrs.field(metadata={utils.LOCAL_REMOTE_DIVERGENCE_ALLOWED: True})

    @property
    def id_proto(self) -> id_pb2.Id:
        return id_helper.IdHelper.from_string(self.id)

    @classmethod
    @typechecked
    def from_data_proto(cls, id: id_pb2.Id, fco_metadata: fco_metadata_pb2.FcoMetadata) -> "TectonObjectMetadataSpec":
        return cls(
            name=utils.get_field_or_none(fco_metadata, "name"),
            id=id_helper.IdHelper.to_string(id),
            description=utils.get_field_or_none(fco_metadata, "description"),
            tags=dict(fco_metadata.tags),
            owner=utils.get_field_or_none(fco_metadata, "owner"),
            created_at=utils.get_timestamp_field_or_none(fco_metadata, "created_at"),
            workspace=utils.get_field_or_none(fco_metadata, "workspace"),
            framework_version=utils.get_field_or_none(fco_metadata, "framework_version"),
            is_local_object=False,
        )

    @classmethod
    @typechecked
    def from_args_proto(cls, id: id_pb2.Id, basic_info: basic_info_pb2.BasicInfo) -> "TectonObjectMetadataSpec":
        return cls(
            name=utils.get_field_or_none(basic_info, "name"),
            id=id_helper.IdHelper.to_string(id),
            description=utils.get_field_or_none(basic_info, "description"),
            tags=dict(basic_info.tags),
            owner=utils.get_field_or_none(basic_info, "owner"),
            created_at=None,
            workspace=None,
            framework_version=framework_version_pb2.FrameworkVersion.FWV5,
            is_local_object=True,
        )


@utils.frozen_strict
class TectonObjectSpec:
    """Base class for all Tecton object (aka First Class Objects or FCO) specs.

    Specs provide a unified, frozen (i.e. immutable), and more useful abstraction over args and data protos for use
    within the Python SDK.

    See the RFC;
    https://www.notion.so/tecton/RFC-Unified-SDK-for-Notebook-Driven-Development-a377af9d320f46488ea238e51e2ce656
    """

    metadata: TectonObjectMetadataSpec

    @property
    def name(self) -> str:
        """Convenience accessor."""
        return self.metadata.name

    @property
    def id(self) -> str:
        """Convenience accessor."""
        return self.metadata.id

    @property
    def id_proto(self) -> id_pb2.Id:
        """Convenience accessor."""
        return self.metadata.id_proto

    @property
    def workspace(self) -> Optional[str]:
        """Convenience accessor."""
        return self.metadata.workspace

    @property
    def is_local_object(self) -> bool:
        """Convenience accessor."""
        return self.metadata.is_local_object
