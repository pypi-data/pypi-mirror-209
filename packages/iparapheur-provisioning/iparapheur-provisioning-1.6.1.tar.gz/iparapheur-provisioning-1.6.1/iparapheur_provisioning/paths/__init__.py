# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from iparapheur_provisioning.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_PROVISIONING_V1_ADMIN_USER_USER_ID = "/api/provisioning/v1/admin/user/{userId}"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID = "/api/provisioning/v1/admin/tenant/{tenantId}"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_USER_USER_ID = "/api/provisioning/v1/admin/tenant/{tenantId}/user/{userId}"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID_SUBTYPE_SUBTYPE_ID = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}/subtype/{subtypeId}"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK_DESK_ID = "/api/provisioning/v1/admin/tenant/{tenantId}/desk/{deskId}"
    API_PROVISIONING_V1_ADMIN_TENANT = "/api/provisioning/v1/admin/tenant"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_USER = "/api/provisioning/v1/admin/tenant/{tenantId}/user"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID_SUBTYPE = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}/subtype"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_DESK = "/api/provisioning/v1/admin/tenant/{tenantId}/desk"
    API_PROVISIONING_V1_ADMIN_USER = "/api/provisioning/v1/admin/user"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY = "/api/provisioning/v1/admin/tenant/{tenantId}/typology"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID_SUBTYPE_SUBTYPE_ID_METADATA = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}/subtype/{subtypeId}/metadata"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID_SUBTYPE_SUBTYPE_ID_LAYER = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}/subtype/{subtypeId}/layer"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID_SUBTYPE_SUBTYPE_ID_FILTERABLE_BY_DESKS = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}/subtype/{subtypeId}/filterableByDesks"
    API_PROVISIONING_V1_ADMIN_TENANT_TENANT_ID_TYPOLOGY_TYPE_TYPE_ID_SUBTYPE_SUBTYPE_ID_CREATION_PERMITTED_DESKS = "/api/provisioning/v1/admin/tenant/{tenantId}/typology/type/{typeId}/subtype/{subtypeId}/creationPermittedDesks"
