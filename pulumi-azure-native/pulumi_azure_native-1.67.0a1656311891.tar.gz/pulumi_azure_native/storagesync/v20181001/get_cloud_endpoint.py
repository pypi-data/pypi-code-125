# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetCloudEndpointResult',
    'AwaitableGetCloudEndpointResult',
    'get_cloud_endpoint',
    'get_cloud_endpoint_output',
]

warnings.warn("""Version 2018-10-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetCloudEndpointResult:
    """
    Cloud Endpoint object.
    """
    def __init__(__self__, backup_enabled=None, friendly_name=None, id=None, last_operation_name=None, last_workflow_id=None, name=None, partnership_id=None, provisioning_state=None, storage_account_resource_id=None, storage_account_share_name=None, storage_account_tenant_id=None, type=None):
        if backup_enabled and not isinstance(backup_enabled, str):
            raise TypeError("Expected argument 'backup_enabled' to be a str")
        pulumi.set(__self__, "backup_enabled", backup_enabled)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_operation_name and not isinstance(last_operation_name, str):
            raise TypeError("Expected argument 'last_operation_name' to be a str")
        pulumi.set(__self__, "last_operation_name", last_operation_name)
        if last_workflow_id and not isinstance(last_workflow_id, str):
            raise TypeError("Expected argument 'last_workflow_id' to be a str")
        pulumi.set(__self__, "last_workflow_id", last_workflow_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partnership_id and not isinstance(partnership_id, str):
            raise TypeError("Expected argument 'partnership_id' to be a str")
        pulumi.set(__self__, "partnership_id", partnership_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if storage_account_resource_id and not isinstance(storage_account_resource_id, str):
            raise TypeError("Expected argument 'storage_account_resource_id' to be a str")
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if storage_account_share_name and not isinstance(storage_account_share_name, str):
            raise TypeError("Expected argument 'storage_account_share_name' to be a str")
        pulumi.set(__self__, "storage_account_share_name", storage_account_share_name)
        if storage_account_tenant_id and not isinstance(storage_account_tenant_id, str):
            raise TypeError("Expected argument 'storage_account_tenant_id' to be a str")
        pulumi.set(__self__, "storage_account_tenant_id", storage_account_tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backupEnabled")
    def backup_enabled(self) -> str:
        """
        Backup Enabled
        """
        return pulumi.get(self, "backup_enabled")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly Name
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastOperationName")
    def last_operation_name(self) -> Optional[str]:
        """
        Resource Last Operation Name
        """
        return pulumi.get(self, "last_operation_name")

    @property
    @pulumi.getter(name="lastWorkflowId")
    def last_workflow_id(self) -> Optional[str]:
        """
        CloudEndpoint lastWorkflowId
        """
        return pulumi.get(self, "last_workflow_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnershipId")
    def partnership_id(self) -> Optional[str]:
        """
        Partnership Id
        """
        return pulumi.get(self, "partnership_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        CloudEndpoint Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> Optional[str]:
        """
        Storage Account Resource Id
        """
        return pulumi.get(self, "storage_account_resource_id")

    @property
    @pulumi.getter(name="storageAccountShareName")
    def storage_account_share_name(self) -> Optional[str]:
        """
        Storage Account Share name
        """
        return pulumi.get(self, "storage_account_share_name")

    @property
    @pulumi.getter(name="storageAccountTenantId")
    def storage_account_tenant_id(self) -> Optional[str]:
        """
        Storage Account Tenant Id
        """
        return pulumi.get(self, "storage_account_tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCloudEndpointResult(GetCloudEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCloudEndpointResult(
            backup_enabled=self.backup_enabled,
            friendly_name=self.friendly_name,
            id=self.id,
            last_operation_name=self.last_operation_name,
            last_workflow_id=self.last_workflow_id,
            name=self.name,
            partnership_id=self.partnership_id,
            provisioning_state=self.provisioning_state,
            storage_account_resource_id=self.storage_account_resource_id,
            storage_account_share_name=self.storage_account_share_name,
            storage_account_tenant_id=self.storage_account_tenant_id,
            type=self.type)


def get_cloud_endpoint(cloud_endpoint_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       storage_sync_service_name: Optional[str] = None,
                       sync_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCloudEndpointResult:
    """
    Cloud Endpoint object.


    :param str cloud_endpoint_name: Name of Cloud Endpoint object.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_sync_service_name: Name of Storage Sync Service resource.
    :param str sync_group_name: Name of Sync Group resource.
    """
    pulumi.log.warn("""get_cloud_endpoint is deprecated: Version 2018-10-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['cloudEndpointName'] = cloud_endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageSyncServiceName'] = storage_sync_service_name
    __args__['syncGroupName'] = sync_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storagesync/v20181001:getCloudEndpoint', __args__, opts=opts, typ=GetCloudEndpointResult).value

    return AwaitableGetCloudEndpointResult(
        backup_enabled=__ret__.backup_enabled,
        friendly_name=__ret__.friendly_name,
        id=__ret__.id,
        last_operation_name=__ret__.last_operation_name,
        last_workflow_id=__ret__.last_workflow_id,
        name=__ret__.name,
        partnership_id=__ret__.partnership_id,
        provisioning_state=__ret__.provisioning_state,
        storage_account_resource_id=__ret__.storage_account_resource_id,
        storage_account_share_name=__ret__.storage_account_share_name,
        storage_account_tenant_id=__ret__.storage_account_tenant_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_cloud_endpoint)
def get_cloud_endpoint_output(cloud_endpoint_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              storage_sync_service_name: Optional[pulumi.Input[str]] = None,
                              sync_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCloudEndpointResult]:
    """
    Cloud Endpoint object.


    :param str cloud_endpoint_name: Name of Cloud Endpoint object.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str storage_sync_service_name: Name of Storage Sync Service resource.
    :param str sync_group_name: Name of Sync Group resource.
    """
    pulumi.log.warn("""get_cloud_endpoint is deprecated: Version 2018-10-01 will be removed in v2 of the provider.""")
    ...
