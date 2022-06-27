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
    'GetSqlPoolResult',
    'AwaitableGetSqlPoolResult',
    'get_sql_pool',
    'get_sql_pool_output',
]

warnings.warn("""Version 2019-06-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetSqlPoolResult:
    """
    A SQL Analytics pool
    """
    def __init__(__self__, collation=None, create_mode=None, creation_date=None, id=None, location=None, max_size_bytes=None, name=None, provisioning_state=None, recoverable_database_id=None, restore_point_in_time=None, sku=None, source_database_id=None, status=None, tags=None, type=None):
        if collation and not isinstance(collation, str):
            raise TypeError("Expected argument 'collation' to be a str")
        pulumi.set(__self__, "collation", collation)
        if create_mode and not isinstance(create_mode, str):
            raise TypeError("Expected argument 'create_mode' to be a str")
        pulumi.set(__self__, "create_mode", create_mode)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_size_bytes and not isinstance(max_size_bytes, float):
            raise TypeError("Expected argument 'max_size_bytes' to be a float")
        pulumi.set(__self__, "max_size_bytes", max_size_bytes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if recoverable_database_id and not isinstance(recoverable_database_id, str):
            raise TypeError("Expected argument 'recoverable_database_id' to be a str")
        pulumi.set(__self__, "recoverable_database_id", recoverable_database_id)
        if restore_point_in_time and not isinstance(restore_point_in_time, str):
            raise TypeError("Expected argument 'restore_point_in_time' to be a str")
        pulumi.set(__self__, "restore_point_in_time", restore_point_in_time)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if source_database_id and not isinstance(source_database_id, str):
            raise TypeError("Expected argument 'source_database_id' to be a str")
        pulumi.set(__self__, "source_database_id", source_database_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def collation(self) -> Optional[str]:
        """
        Collation mode
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[str]:
        """
        Specifies the mode of sql pool creation.

        Default: regular sql pool creation.

        PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.

        Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.

        Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified.
        """
        return pulumi.get(self, "create_mode")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[str]:
        """
        Date the SQL pool was created
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> Optional[float]:
        """
        Maximum size in bytes
        """
        return pulumi.get(self, "max_size_bytes")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Resource state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="recoverableDatabaseId")
    def recoverable_database_id(self) -> Optional[str]:
        """
        Backup database to restore from
        """
        return pulumi.get(self, "recoverable_database_id")

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[str]:
        """
        Snapshot time to restore
        """
        return pulumi.get(self, "restore_point_in_time")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        SQL pool SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> Optional[str]:
        """
        Source database to create from
        """
        return pulumi.get(self, "source_database_id")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Resource status
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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSqlPoolResult(GetSqlPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlPoolResult(
            collation=self.collation,
            create_mode=self.create_mode,
            creation_date=self.creation_date,
            id=self.id,
            location=self.location,
            max_size_bytes=self.max_size_bytes,
            name=self.name,
            provisioning_state=self.provisioning_state,
            recoverable_database_id=self.recoverable_database_id,
            restore_point_in_time=self.restore_point_in_time,
            sku=self.sku,
            source_database_id=self.source_database_id,
            status=self.status,
            tags=self.tags,
            type=self.type)


def get_sql_pool(resource_group_name: Optional[str] = None,
                 sql_pool_name: Optional[str] = None,
                 workspace_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlPoolResult:
    """
    A SQL Analytics pool


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sql_pool_name: SQL pool name
    :param str workspace_name: The name of the workspace
    """
    pulumi.log.warn("""get_sql_pool is deprecated: Version 2019-06-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlPoolName'] = sql_pool_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20190601preview:getSqlPool', __args__, opts=opts, typ=GetSqlPoolResult).value

    return AwaitableGetSqlPoolResult(
        collation=__ret__.collation,
        create_mode=__ret__.create_mode,
        creation_date=__ret__.creation_date,
        id=__ret__.id,
        location=__ret__.location,
        max_size_bytes=__ret__.max_size_bytes,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        recoverable_database_id=__ret__.recoverable_database_id,
        restore_point_in_time=__ret__.restore_point_in_time,
        sku=__ret__.sku,
        source_database_id=__ret__.source_database_id,
        status=__ret__.status,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_sql_pool)
def get_sql_pool_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        sql_pool_name: Optional[pulumi.Input[str]] = None,
                        workspace_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlPoolResult]:
    """
    A SQL Analytics pool


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sql_pool_name: SQL pool name
    :param str workspace_name: The name of the workspace
    """
    pulumi.log.warn("""get_sql_pool is deprecated: Version 2019-06-01-preview will be removed in v2 of the provider.""")
    ...
