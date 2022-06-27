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
    'GetStorageAccountResult',
    'AwaitableGetStorageAccountResult',
    'get_storage_account',
    'get_storage_account_output',
]

warnings.warn("""Version 2020-09-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetStorageAccountResult:
    """
    Represents a Storage Account on the  Data Box Edge/Gateway device.
    """
    def __init__(__self__, blob_endpoint=None, container_count=None, data_policy=None, description=None, id=None, name=None, storage_account_credential_id=None, storage_account_status=None, system_data=None, type=None):
        if blob_endpoint and not isinstance(blob_endpoint, str):
            raise TypeError("Expected argument 'blob_endpoint' to be a str")
        pulumi.set(__self__, "blob_endpoint", blob_endpoint)
        if container_count and not isinstance(container_count, int):
            raise TypeError("Expected argument 'container_count' to be a int")
        pulumi.set(__self__, "container_count", container_count)
        if data_policy and not isinstance(data_policy, str):
            raise TypeError("Expected argument 'data_policy' to be a str")
        pulumi.set(__self__, "data_policy", data_policy)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_account_credential_id and not isinstance(storage_account_credential_id, str):
            raise TypeError("Expected argument 'storage_account_credential_id' to be a str")
        pulumi.set(__self__, "storage_account_credential_id", storage_account_credential_id)
        if storage_account_status and not isinstance(storage_account_status, str):
            raise TypeError("Expected argument 'storage_account_status' to be a str")
        pulumi.set(__self__, "storage_account_status", storage_account_status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="blobEndpoint")
    def blob_endpoint(self) -> str:
        """
        BlobEndpoint of Storage Account
        """
        return pulumi.get(self, "blob_endpoint")

    @property
    @pulumi.getter(name="containerCount")
    def container_count(self) -> int:
        """
        The Container Count. Present only for Storage Accounts with DataPolicy set to Cloud.
        """
        return pulumi.get(self, "container_count")

    @property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> str:
        """
        Data policy of the storage Account.
        """
        return pulumi.get(self, "data_policy")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description for the storage Account.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> Optional[str]:
        """
        Storage Account Credential Id
        """
        return pulumi.get(self, "storage_account_credential_id")

    @property
    @pulumi.getter(name="storageAccountStatus")
    def storage_account_status(self) -> Optional[str]:
        """
        Current status of the storage account
        """
        return pulumi.get(self, "storage_account_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        StorageAccount object on ASE device
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetStorageAccountResult(GetStorageAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageAccountResult(
            blob_endpoint=self.blob_endpoint,
            container_count=self.container_count,
            data_policy=self.data_policy,
            description=self.description,
            id=self.id,
            name=self.name,
            storage_account_credential_id=self.storage_account_credential_id,
            storage_account_status=self.storage_account_status,
            system_data=self.system_data,
            type=self.type)


def get_storage_account(device_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        storage_account_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageAccountResult:
    """
    Represents a Storage Account on the  Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str storage_account_name: The storage account name.
    """
    pulumi.log.warn("""get_storage_account is deprecated: Version 2020-09-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['storageAccountName'] = storage_account_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20200901:getStorageAccount', __args__, opts=opts, typ=GetStorageAccountResult).value

    return AwaitableGetStorageAccountResult(
        blob_endpoint=__ret__.blob_endpoint,
        container_count=__ret__.container_count,
        data_policy=__ret__.data_policy,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        storage_account_credential_id=__ret__.storage_account_credential_id,
        storage_account_status=__ret__.storage_account_status,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_storage_account)
def get_storage_account_output(device_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               storage_account_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageAccountResult]:
    """
    Represents a Storage Account on the  Data Box Edge/Gateway device.


    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str storage_account_name: The storage account name.
    """
    pulumi.log.warn("""get_storage_account is deprecated: Version 2020-09-01 will be removed in v2 of the provider.""")
    ...
