# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/auth/authorization_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from tecton_proto.auth import principal_pb2 as tecton__proto_dot_auth_dot_principal__pb2
from tecton_proto.auth import resource_pb2 as tecton__proto_dot_auth_dot_resource__pb2
from tecton_proto.auth import resource_role_assignments_pb2 as tecton__proto_dot_auth_dot_resource__role__assignments__pb2
from tecton_proto.auth import service_pb2 as tecton__proto_dot_auth_dot_service__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-tecton_proto/auth/authorization_service.proto\x12\x11tecton_proto.auth\x1a\x1cgoogle/api/annotations.proto\x1a!tecton_proto/auth/principal.proto\x1a tecton_proto/auth/resource.proto\x1a\x31tecton_proto/auth/resource_role_assignments.proto\x1a\x1ftecton_proto/auth/service.proto\"\x11\n\x0fGetRolesRequest\"K\n\x10GetRolesResponse\x12\x37\n\x05roles\x18\x01 \x03(\x0b\x32!.tecton_proto.auth.RoleDefinitionR\x05roles\"\x85\x03\n\x0eRoleDefinition\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12`\n\x1c\x61ssignable_on_resource_types\x18\x04 \x03(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x19\x61ssignableOnResourceTypes\x12\x63\n\x1d\x61ssignable_to_principal_types\x18\x05 \x03(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\x1a\x61ssignableToPrincipalTypes\x12I\n\x0bpermissions\x18\x06 \x03(\x0b\x32\'.tecton_proto.auth.PermissionDefinitionR\x0bpermissions\x12\x1b\n\tlegacy_id\x18\x07 \x01(\tR\x08legacyId\"m\n\x14PermissionDefinition\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12#\n\ris_authorized\x18\x03 \x01(\x08R\x0cisAuthorized\"\x84\x02\n\x17GetAssignedRolesRequest\x12G\n\x0eprincipal_type\x18\x01 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x02 \x01(\tR\x0bprincipalId\x12\x44\n\rresource_type\x18\x03 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12!\n\x0cresource_ids\x18\x04 \x03(\tR\x0bresourceIds\x12\x14\n\x05roles\x18\x05 \x03(\tR\x05roles\"k\n\x18GetAssignedRolesResponse\x12O\n\x0b\x61ssignments\x18\x01 \x03(\x0b\x32-.tecton_proto.auth.ResourceAndRoleAssignmentsR\x0b\x61ssignments\"\xc5\x01\n\x16GetIsAuthorizedRequest\x12G\n\x0eprincipal_type\x18\x01 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x02 \x01(\tR\x0bprincipalId\x12?\n\x0bpermissions\x18\x03 \x03(\x0b\x32\x1d.tecton_proto.auth.PermissionR\x0bpermissions\"Z\n\x17GetIsAuthorizedResponse\x12?\n\x0bpermissions\x18\x01 \x03(\x0b\x32\x1d.tecton_proto.auth.PermissionR\x0bpermissions\"U\n\x12\x41ssignRolesRequest\x12?\n\x0b\x61ssignments\x18\x01 \x03(\x0b\x32\x1d.tecton_proto.auth.AssignmentR\x0b\x61ssignments\"\x15\n\x13\x41ssignRolesResponse\"W\n\x14UnassignRolesRequest\x12?\n\x0b\x61ssignments\x18\x01 \x03(\x0b\x32\x1d.tecton_proto.auth.AssignmentR\x0b\x61ssignments\"\x17\n\x15UnassignRolesResponse\"\xf3\x01\n\nAssignment\x12\x44\n\rresource_type\x18\x01 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12\x12\n\x04role\x18\x03 \x01(\tR\x04role\x12G\n\x0eprincipal_type\x18\x04 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x05 \x01(\tR\x0bprincipalId\"\x80\x02\n\x15\x41ssignRolesPutRequest\x12\x44\n\rresource_type\x18\x01 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12G\n\x0eprincipal_type\x18\x03 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x04 \x01(\tR\x0bprincipalId\x12\x14\n\x05roles\x18\x05 \x03(\tR\x05roles\"\x18\n\x16\x41ssignRolesPutResponse\"\xe9\x01\n\x1dGetAuthorizedResourcesRequest\x12G\n\x0eprincipal_type\x18\x01 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x02 \x01(\tR\x0bprincipalId\x12\x44\n\rresource_type\x18\x03 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12\x16\n\x06\x61\x63tion\x18\x04 \x01(\tR\x06\x61\x63tion\"{\n\x1eGetAuthorizedResourcesResponse\x12Y\n\x14\x61uthorized_resources\x18\x01 \x03(\x0b\x32&.tecton_proto.auth.AuthorizedResourcesR\x13\x61uthorizedResources\"P\n\x13\x41uthorizedResources\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x18\n\x07\x61\x63tions\x18\x02 \x03(\tR\x07\x61\x63tions\"\xe6\x01\n\x1cGetAssignedPrincipalsRequest\x12\x44\n\rresource_type\x18\x01 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12\x14\n\x05roles\x18\x03 \x03(\tR\x05roles\x12I\n\x0fprincipal_types\x18\x04 \x03(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\x0eprincipalTypes\"e\n\x1dGetAssignedPrincipalsResponse\x12\x44\n\x0b\x61ssignments\x18\x01 \x03(\x0b\x32\".tecton_proto.auth.AssignmentBasicR\x0b\x61ssignments\"\xc2\x01\n\x0f\x41ssignmentBasic\x12?\n\tprincipal\x18\x01 \x01(\x0b\x32!.tecton_proto.auth.PrincipalBasicR\tprincipal\x12\x14\n\x05roles\x18\x02 \x03(\tR\x05roles\x12X\n\x10role_assignments\x18\x03 \x03(\x0b\x32-.tecton_proto.auth.ResourceAndRoleAssignmentsR\x0froleAssignments\"\xee\x01\n\x18GetAppPermissionsRequest\x12G\n\x0eprincipal_type\x18\x01 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x02 \x01(\tR\x0bprincipalId\x12\x66\n\x19resource_type_permissions\x18\x05 \x03(\x0b\x32*.tecton_proto.auth.ResourceTypePermissionsR\x17resourceTypePermissions\"y\n\x17ResourceTypePermissions\x12\x44\n\rresource_type\x18\x01 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12\x18\n\x07\x61\x63tions\x18\x02 \x03(\tR\x07\x61\x63tions\"\x93\x01\n\x19GetAppPermissionsResponse\x12v\n\x1fresource_type_permission_values\x18\x01 \x03(\x0b\x32/.tecton_proto.auth.ResourceTypePermissionValuesR\x1cresourceTypePermissionValues\"\xb5\x01\n\x1cResourceTypePermissionValues\x12\x44\n\rresource_type\x18\x01 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12O\n\x11permission_values\x18\x02 \x03(\x0b\x32\".tecton_proto.auth.PermissionValueR\x10permissionValues\"\x8b\x01\n\nPermission\x12\x44\n\rresource_type\x18\x01 \x01(\x0e\x32\x1f.tecton_proto.auth.ResourceTypeR\x0cresourceType\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12\x16\n\x06\x61\x63tion\x18\x03 \x01(\tR\x06\x61\x63tion\"N\n\x0fPermissionValue\x12\x16\n\x06\x61\x63tion\x18\x01 \x01(\tR\x06\x61\x63tion\x12#\n\ris_authorized\x18\x02 \x01(\x08R\x0cisAuthorized\"\x97\x02\n\x1eGetWorkspacePermissionsRequest\x12G\n\x0eprincipal_type\x18\x01 \x01(\x0e\x32 .tecton_proto.auth.PrincipalTypeR\rprincipalType\x12!\n\x0cprincipal_id\x18\x02 \x01(\tR\x0bprincipalId\x12!\n\x0cworkspace_id\x18\x03 \x01(\tR\x0bworkspaceId\x12\x66\n\x19resource_type_permissions\x18\x04 \x03(\x0b\x32*.tecton_proto.auth.ResourceTypePermissionsR\x17resourceTypePermissions\"\x99\x01\n\x1fGetWorkspacePermissionsResponse\x12v\n\x1fresource_type_permission_values\x18\x01 \x03(\x0b\x32/.tecton_proto.auth.ResourceTypePermissionValuesR\x1cresourceTypePermissionValues2\xe5\r\n\x14\x41uthorizationService\x12\x8b\x01\n\x08GetRoles\x12\".tecton_proto.auth.GetRolesRequest\x1a#.tecton_proto.auth.GetRolesResponse\"6\x82\xd3\xe4\x93\x02(\"#/v1/authorization-service/get-roles:\x01*\xa2\xbc\xe6\xc0\x05\x02\x10\x01\x12\xac\x01\n\x10GetAssignedRoles\x12*.tecton_proto.auth.GetAssignedRolesRequest\x1a+.tecton_proto.auth.GetAssignedRolesResponse\"?\x82\xd3\xe4\x93\x02\x31\",/v1/authorization-service/get-assigned-roles:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\x97\x01\n\x0b\x41ssignRoles\x12%.tecton_proto.auth.AssignRolesRequest\x1a&.tecton_proto.auth.AssignRolesResponse\"9\x82\xd3\xe4\x93\x02+\"&/v1/authorization-service/assign-roles:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\x9f\x01\n\rUnassignRoles\x12\'.tecton_proto.auth.UnassignRolesRequest\x1a(.tecton_proto.auth.UnassignRolesResponse\";\x82\xd3\xe4\x93\x02-\"(/v1/authorization-service/unassign-roles:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\xa0\x01\n\x0e\x41ssignRolesPut\x12(.tecton_proto.auth.AssignRolesPutRequest\x1a).tecton_proto.auth.AssignRolesPutResponse\"9\x82\xd3\xe4\x93\x02+\x1a&/v1/authorization-service/assign-roles:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\xc4\x01\n\x16GetAuthorizedResources\x12\x30.tecton_proto.auth.GetAuthorizedResourcesRequest\x1a\x31.tecton_proto.auth.GetAuthorizedResourcesResponse\"E\x82\xd3\xe4\x93\x02\x37\"2/v1/authorization-service/get-authorized-resources:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\xc0\x01\n\x15GetAssignedPrincipals\x12/.tecton_proto.auth.GetAssignedPrincipalsRequest\x1a\x30.tecton_proto.auth.GetAssignedPrincipalsResponse\"D\x82\xd3\xe4\x93\x02\x36\"1/v1/authorization-service/get-assigned-principals:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\xb0\x01\n\x11GetAppPermissions\x12+.tecton_proto.auth.GetAppPermissionsRequest\x1a,.tecton_proto.auth.GetAppPermissionsResponse\"@\x82\xd3\xe4\x93\x02\x32\"-/v1/authorization-service/get-app-permissions:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\xc8\x01\n\x17GetWorkspacePermissions\x12\x31.tecton_proto.auth.GetWorkspacePermissionsRequest\x1a\x32.tecton_proto.auth.GetWorkspacePermissionsResponse\"F\x82\xd3\xe4\x93\x02\x38\"3/v1/authorization-service/get-workspace-permissions:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x12\xa8\x01\n\x0fGetIsAuthorized\x12).tecton_proto.auth.GetIsAuthorizedRequest\x1a*.tecton_proto.auth.GetIsAuthorizedResponse\">\x82\xd3\xe4\x93\x02\x30\"+/v1/authorization-service/get-is-authorized:\x01*\xa2\xbc\xe6\xc0\x05\x02@\x01\x42V\n\x0f\x63om.tecton.authB\x19\x41uthorizationServiceProtoP\x01Z&github.com/tecton-ai/tecton_proto/auth')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tecton_proto.auth.authorization_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.tecton.authB\031AuthorizationServiceProtoP\001Z&github.com/tecton-ai/tecton_proto/auth'
  _AUTHORIZATIONSERVICE.methods_by_name['GetRoles']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetRoles']._serialized_options = b'\202\323\344\223\002(\"#/v1/authorization-service/get-roles:\001*\242\274\346\300\005\002\020\001'
  _AUTHORIZATIONSERVICE.methods_by_name['GetAssignedRoles']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetAssignedRoles']._serialized_options = b'\202\323\344\223\0021\",/v1/authorization-service/get-assigned-roles:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['AssignRoles']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['AssignRoles']._serialized_options = b'\202\323\344\223\002+\"&/v1/authorization-service/assign-roles:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['UnassignRoles']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['UnassignRoles']._serialized_options = b'\202\323\344\223\002-\"(/v1/authorization-service/unassign-roles:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['AssignRolesPut']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['AssignRolesPut']._serialized_options = b'\202\323\344\223\002+\032&/v1/authorization-service/assign-roles:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['GetAuthorizedResources']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetAuthorizedResources']._serialized_options = b'\202\323\344\223\0027\"2/v1/authorization-service/get-authorized-resources:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['GetAssignedPrincipals']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetAssignedPrincipals']._serialized_options = b'\202\323\344\223\0026\"1/v1/authorization-service/get-assigned-principals:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['GetAppPermissions']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetAppPermissions']._serialized_options = b'\202\323\344\223\0022\"-/v1/authorization-service/get-app-permissions:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['GetWorkspacePermissions']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetWorkspacePermissions']._serialized_options = b'\202\323\344\223\0028\"3/v1/authorization-service/get-workspace-permissions:\001*\242\274\346\300\005\002@\001'
  _AUTHORIZATIONSERVICE.methods_by_name['GetIsAuthorized']._options = None
  _AUTHORIZATIONSERVICE.methods_by_name['GetIsAuthorized']._serialized_options = b'\202\323\344\223\0020\"+/v1/authorization-service/get-is-authorized:\001*\242\274\346\300\005\002@\001'
  _GETROLESREQUEST._serialized_start=251
  _GETROLESREQUEST._serialized_end=268
  _GETROLESRESPONSE._serialized_start=270
  _GETROLESRESPONSE._serialized_end=345
  _ROLEDEFINITION._serialized_start=348
  _ROLEDEFINITION._serialized_end=737
  _PERMISSIONDEFINITION._serialized_start=739
  _PERMISSIONDEFINITION._serialized_end=848
  _GETASSIGNEDROLESREQUEST._serialized_start=851
  _GETASSIGNEDROLESREQUEST._serialized_end=1111
  _GETASSIGNEDROLESRESPONSE._serialized_start=1113
  _GETASSIGNEDROLESRESPONSE._serialized_end=1220
  _GETISAUTHORIZEDREQUEST._serialized_start=1223
  _GETISAUTHORIZEDREQUEST._serialized_end=1420
  _GETISAUTHORIZEDRESPONSE._serialized_start=1422
  _GETISAUTHORIZEDRESPONSE._serialized_end=1512
  _ASSIGNROLESREQUEST._serialized_start=1514
  _ASSIGNROLESREQUEST._serialized_end=1599
  _ASSIGNROLESRESPONSE._serialized_start=1601
  _ASSIGNROLESRESPONSE._serialized_end=1622
  _UNASSIGNROLESREQUEST._serialized_start=1624
  _UNASSIGNROLESREQUEST._serialized_end=1711
  _UNASSIGNROLESRESPONSE._serialized_start=1713
  _UNASSIGNROLESRESPONSE._serialized_end=1736
  _ASSIGNMENT._serialized_start=1739
  _ASSIGNMENT._serialized_end=1982
  _ASSIGNROLESPUTREQUEST._serialized_start=1985
  _ASSIGNROLESPUTREQUEST._serialized_end=2241
  _ASSIGNROLESPUTRESPONSE._serialized_start=2243
  _ASSIGNROLESPUTRESPONSE._serialized_end=2267
  _GETAUTHORIZEDRESOURCESREQUEST._serialized_start=2270
  _GETAUTHORIZEDRESOURCESREQUEST._serialized_end=2503
  _GETAUTHORIZEDRESOURCESRESPONSE._serialized_start=2505
  _GETAUTHORIZEDRESOURCESRESPONSE._serialized_end=2628
  _AUTHORIZEDRESOURCES._serialized_start=2630
  _AUTHORIZEDRESOURCES._serialized_end=2710
  _GETASSIGNEDPRINCIPALSREQUEST._serialized_start=2713
  _GETASSIGNEDPRINCIPALSREQUEST._serialized_end=2943
  _GETASSIGNEDPRINCIPALSRESPONSE._serialized_start=2945
  _GETASSIGNEDPRINCIPALSRESPONSE._serialized_end=3046
  _ASSIGNMENTBASIC._serialized_start=3049
  _ASSIGNMENTBASIC._serialized_end=3243
  _GETAPPPERMISSIONSREQUEST._serialized_start=3246
  _GETAPPPERMISSIONSREQUEST._serialized_end=3484
  _RESOURCETYPEPERMISSIONS._serialized_start=3486
  _RESOURCETYPEPERMISSIONS._serialized_end=3607
  _GETAPPPERMISSIONSRESPONSE._serialized_start=3610
  _GETAPPPERMISSIONSRESPONSE._serialized_end=3757
  _RESOURCETYPEPERMISSIONVALUES._serialized_start=3760
  _RESOURCETYPEPERMISSIONVALUES._serialized_end=3941
  _PERMISSION._serialized_start=3944
  _PERMISSION._serialized_end=4083
  _PERMISSIONVALUE._serialized_start=4085
  _PERMISSIONVALUE._serialized_end=4163
  _GETWORKSPACEPERMISSIONSREQUEST._serialized_start=4166
  _GETWORKSPACEPERMISSIONSREQUEST._serialized_end=4445
  _GETWORKSPACEPERMISSIONSRESPONSE._serialized_start=4448
  _GETWORKSPACEPERMISSIONSRESPONSE._serialized_end=4601
  _AUTHORIZATIONSERVICE._serialized_start=4604
  _AUTHORIZATIONSERVICE._serialized_end=6369
# @@protoc_insertion_point(module_scope)
