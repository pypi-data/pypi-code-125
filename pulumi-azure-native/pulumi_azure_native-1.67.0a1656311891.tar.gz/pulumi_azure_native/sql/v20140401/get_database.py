# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    Represents a database.
    """
    def __init__(__self__, collation=None, containment_state=None, creation_date=None, current_service_objective_id=None, database_id=None, default_secondary_location=None, earliest_restore_date=None, edition=None, elastic_pool_name=None, failover_group_id=None, id=None, kind=None, location=None, max_size_bytes=None, name=None, read_scale=None, recommended_index=None, requested_service_objective_id=None, requested_service_objective_name=None, service_level_objective=None, service_tier_advisors=None, status=None, tags=None, transparent_data_encryption=None, type=None, zone_redundant=None):
        if collation and not isinstance(collation, str):
            raise TypeError("Expected argument 'collation' to be a str")
        pulumi.set(__self__, "collation", collation)
        if containment_state and not isinstance(containment_state, float):
            raise TypeError("Expected argument 'containment_state' to be a float")
        pulumi.set(__self__, "containment_state", containment_state)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if current_service_objective_id and not isinstance(current_service_objective_id, str):
            raise TypeError("Expected argument 'current_service_objective_id' to be a str")
        pulumi.set(__self__, "current_service_objective_id", current_service_objective_id)
        if database_id and not isinstance(database_id, str):
            raise TypeError("Expected argument 'database_id' to be a str")
        pulumi.set(__self__, "database_id", database_id)
        if default_secondary_location and not isinstance(default_secondary_location, str):
            raise TypeError("Expected argument 'default_secondary_location' to be a str")
        pulumi.set(__self__, "default_secondary_location", default_secondary_location)
        if earliest_restore_date and not isinstance(earliest_restore_date, str):
            raise TypeError("Expected argument 'earliest_restore_date' to be a str")
        pulumi.set(__self__, "earliest_restore_date", earliest_restore_date)
        if edition and not isinstance(edition, str):
            raise TypeError("Expected argument 'edition' to be a str")
        pulumi.set(__self__, "edition", edition)
        if elastic_pool_name and not isinstance(elastic_pool_name, str):
            raise TypeError("Expected argument 'elastic_pool_name' to be a str")
        pulumi.set(__self__, "elastic_pool_name", elastic_pool_name)
        if failover_group_id and not isinstance(failover_group_id, str):
            raise TypeError("Expected argument 'failover_group_id' to be a str")
        pulumi.set(__self__, "failover_group_id", failover_group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_size_bytes and not isinstance(max_size_bytes, str):
            raise TypeError("Expected argument 'max_size_bytes' to be a str")
        pulumi.set(__self__, "max_size_bytes", max_size_bytes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if read_scale and not isinstance(read_scale, str):
            raise TypeError("Expected argument 'read_scale' to be a str")
        pulumi.set(__self__, "read_scale", read_scale)
        if recommended_index and not isinstance(recommended_index, list):
            raise TypeError("Expected argument 'recommended_index' to be a list")
        pulumi.set(__self__, "recommended_index", recommended_index)
        if requested_service_objective_id and not isinstance(requested_service_objective_id, str):
            raise TypeError("Expected argument 'requested_service_objective_id' to be a str")
        pulumi.set(__self__, "requested_service_objective_id", requested_service_objective_id)
        if requested_service_objective_name and not isinstance(requested_service_objective_name, str):
            raise TypeError("Expected argument 'requested_service_objective_name' to be a str")
        pulumi.set(__self__, "requested_service_objective_name", requested_service_objective_name)
        if service_level_objective and not isinstance(service_level_objective, str):
            raise TypeError("Expected argument 'service_level_objective' to be a str")
        pulumi.set(__self__, "service_level_objective", service_level_objective)
        if service_tier_advisors and not isinstance(service_tier_advisors, list):
            raise TypeError("Expected argument 'service_tier_advisors' to be a list")
        pulumi.set(__self__, "service_tier_advisors", service_tier_advisors)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if transparent_data_encryption and not isinstance(transparent_data_encryption, list):
            raise TypeError("Expected argument 'transparent_data_encryption' to be a list")
        pulumi.set(__self__, "transparent_data_encryption", transparent_data_encryption)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter
    def collation(self) -> Optional[str]:
        """
        The collation of the database. If createMode is not Default, this value is ignored.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="containmentState")
    def containment_state(self) -> float:
        """
        The containment state of the database.
        """
        return pulumi.get(self, "containment_state")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of the database (ISO8601 format).
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="currentServiceObjectiveId")
    def current_service_objective_id(self) -> str:
        """
        The current service level objective ID of the database. This is the ID of the service level objective that is currently active.
        """
        return pulumi.get(self, "current_service_objective_id")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> str:
        """
        The ID of the database.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter(name="defaultSecondaryLocation")
    def default_secondary_location(self) -> str:
        """
        The default secondary region for this database.
        """
        return pulumi.get(self, "default_secondary_location")

    @property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> str:
        """
        This records the earliest start date and time that restore is available for this database (ISO8601 format).
        """
        return pulumi.get(self, "earliest_restore_date")

    @property
    @pulumi.getter
    def edition(self) -> Optional[str]:
        """
        The edition of the database. The DatabaseEditions enumeration contains all the valid editions. If createMode is NonReadableSecondary or OnlineSecondary, this value is ignored.
        
        The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands:
        
        ```azurecli
        az sql db list-editions -l <location> -o table
        ````
        
        ```powershell
        Get-AzSqlServerServiceObjective -Location <location>
        ````
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter(name="elasticPoolName")
    def elastic_pool_name(self) -> Optional[str]:
        """
        The name of the elastic pool the database is in. If elasticPoolName and requestedServiceObjectiveName are both updated, the value of requestedServiceObjectiveName is ignored. Not supported for DataWarehouse edition.
        """
        return pulumi.get(self, "elastic_pool_name")

    @property
    @pulumi.getter(name="failoverGroupId")
    def failover_group_id(self) -> str:
        """
        The resource identifier of the failover group containing this database.
        """
        return pulumi.get(self, "failover_group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of database.  This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> Optional[str]:
        """
        The max size of the database expressed in bytes. If createMode is not Default, this value is ignored. To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities) referred to by operationId: "Capabilities_ListByLocation."
        """
        return pulumi.get(self, "max_size_bytes")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readScale")
    def read_scale(self) -> Optional[str]:
        """
        Conditional. If the database is a geo-secondary, readScale indicates whether read-only connections are allowed to this database or not. Not supported for DataWarehouse edition.
        """
        return pulumi.get(self, "read_scale")

    @property
    @pulumi.getter(name="recommendedIndex")
    def recommended_index(self) -> Sequence['outputs.RecommendedIndexResponse']:
        """
        The recommended indices for this database.
        """
        return pulumi.get(self, "recommended_index")

    @property
    @pulumi.getter(name="requestedServiceObjectiveId")
    def requested_service_objective_id(self) -> Optional[str]:
        """
        The configured service level objective ID of the database. This is the service level objective that is in the process of being applied to the database. Once successfully updated, it will match the value of currentServiceObjectiveId property. If requestedServiceObjectiveId and requestedServiceObjectiveName are both updated, the value of requestedServiceObjectiveId overrides the value of requestedServiceObjectiveName.
        
        The list of SKUs may vary by region and support offer. To determine the service objective ids that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API.
        """
        return pulumi.get(self, "requested_service_objective_id")

    @property
    @pulumi.getter(name="requestedServiceObjectiveName")
    def requested_service_objective_name(self) -> Optional[str]:
        """
        The name of the configured service level objective of the database. This is the service level objective that is in the process of being applied to the database. Once successfully updated, it will match the value of serviceLevelObjective property. 
        
        The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or one of the following commands:
        
        ```azurecli
        az sql db list-editions -l <location> -o table
        ````
        
        ```powershell
        Get-AzSqlServerServiceObjective -Location <location>
        ````
        """
        return pulumi.get(self, "requested_service_objective_name")

    @property
    @pulumi.getter(name="serviceLevelObjective")
    def service_level_objective(self) -> str:
        """
        The current service level objective of the database.
        """
        return pulumi.get(self, "service_level_objective")

    @property
    @pulumi.getter(name="serviceTierAdvisors")
    def service_tier_advisors(self) -> Sequence['outputs.ServiceTierAdvisorResponse']:
        """
        The list of service tier advisors for this database. Expanded property
        """
        return pulumi.get(self, "service_tier_advisors")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the database.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="transparentDataEncryption")
    def transparent_data_encryption(self) -> Sequence['outputs.TransparentDataEncryptionResponse']:
        """
        The transparent data encryption info for this database.
        """
        return pulumi.get(self, "transparent_data_encryption")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Whether or not this database is zone redundant, which means the replicas of this database will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            collation=self.collation,
            containment_state=self.containment_state,
            creation_date=self.creation_date,
            current_service_objective_id=self.current_service_objective_id,
            database_id=self.database_id,
            default_secondary_location=self.default_secondary_location,
            earliest_restore_date=self.earliest_restore_date,
            edition=self.edition,
            elastic_pool_name=self.elastic_pool_name,
            failover_group_id=self.failover_group_id,
            id=self.id,
            kind=self.kind,
            location=self.location,
            max_size_bytes=self.max_size_bytes,
            name=self.name,
            read_scale=self.read_scale,
            recommended_index=self.recommended_index,
            requested_service_objective_id=self.requested_service_objective_id,
            requested_service_objective_name=self.requested_service_objective_name,
            service_level_objective=self.service_level_objective,
            service_tier_advisors=self.service_tier_advisors,
            status=self.status,
            tags=self.tags,
            transparent_data_encryption=self.transparent_data_encryption,
            type=self.type,
            zone_redundant=self.zone_redundant)


def get_database(database_name: Optional[str] = None,
                 expand: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 server_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    Represents a database.


    :param str database_name: The name of the database to be retrieved.
    :param str expand: A comma separated list of child objects to expand in the response. Possible properties: serviceTierAdvisors, transparentDataEncryption.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20140401:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        collation=__ret__.collation,
        containment_state=__ret__.containment_state,
        creation_date=__ret__.creation_date,
        current_service_objective_id=__ret__.current_service_objective_id,
        database_id=__ret__.database_id,
        default_secondary_location=__ret__.default_secondary_location,
        earliest_restore_date=__ret__.earliest_restore_date,
        edition=__ret__.edition,
        elastic_pool_name=__ret__.elastic_pool_name,
        failover_group_id=__ret__.failover_group_id,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        max_size_bytes=__ret__.max_size_bytes,
        name=__ret__.name,
        read_scale=__ret__.read_scale,
        recommended_index=__ret__.recommended_index,
        requested_service_objective_id=__ret__.requested_service_objective_id,
        requested_service_objective_name=__ret__.requested_service_objective_name,
        service_level_objective=__ret__.service_level_objective,
        service_tier_advisors=__ret__.service_tier_advisors,
        status=__ret__.status,
        tags=__ret__.tags,
        transparent_data_encryption=__ret__.transparent_data_encryption,
        type=__ret__.type,
        zone_redundant=__ret__.zone_redundant)


@_utilities.lift_output_func(get_database)
def get_database_output(database_name: Optional[pulumi.Input[str]] = None,
                        expand: Optional[pulumi.Input[Optional[str]]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        server_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    Represents a database.


    :param str database_name: The name of the database to be retrieved.
    :param str expand: A comma separated list of child objects to expand in the response. Possible properties: serviceTierAdvisors, transparentDataEncryption.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
