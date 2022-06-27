# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetIscsiServerResult',
    'AwaitableGetIscsiServerResult',
    'get_iscsi_server',
    'get_iscsi_server_output',
]

warnings.warn("""Version 2016-10-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetIscsiServerResult:
    """
    The iSCSI server.
    """
    def __init__(__self__, backup_schedule_group_id=None, chap_id=None, description=None, id=None, name=None, reverse_chap_id=None, storage_domain_id=None, type=None):
        if backup_schedule_group_id and not isinstance(backup_schedule_group_id, str):
            raise TypeError("Expected argument 'backup_schedule_group_id' to be a str")
        pulumi.set(__self__, "backup_schedule_group_id", backup_schedule_group_id)
        if chap_id and not isinstance(chap_id, str):
            raise TypeError("Expected argument 'chap_id' to be a str")
        pulumi.set(__self__, "chap_id", chap_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if reverse_chap_id and not isinstance(reverse_chap_id, str):
            raise TypeError("Expected argument 'reverse_chap_id' to be a str")
        pulumi.set(__self__, "reverse_chap_id", reverse_chap_id)
        if storage_domain_id and not isinstance(storage_domain_id, str):
            raise TypeError("Expected argument 'storage_domain_id' to be a str")
        pulumi.set(__self__, "storage_domain_id", storage_domain_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backupScheduleGroupId")
    def backup_schedule_group_id(self) -> str:
        """
        The backup policy id.
        """
        return pulumi.get(self, "backup_schedule_group_id")

    @property
    @pulumi.getter(name="chapId")
    def chap_id(self) -> Optional[str]:
        """
        The chap id.
        """
        return pulumi.get(self, "chap_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="reverseChapId")
    def reverse_chap_id(self) -> Optional[str]:
        """
        The reverse chap id.
        """
        return pulumi.get(self, "reverse_chap_id")

    @property
    @pulumi.getter(name="storageDomainId")
    def storage_domain_id(self) -> str:
        """
        The storage domain id.
        """
        return pulumi.get(self, "storage_domain_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIscsiServerResult(GetIscsiServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIscsiServerResult(
            backup_schedule_group_id=self.backup_schedule_group_id,
            chap_id=self.chap_id,
            description=self.description,
            id=self.id,
            name=self.name,
            reverse_chap_id=self.reverse_chap_id,
            storage_domain_id=self.storage_domain_id,
            type=self.type)


def get_iscsi_server(device_name: Optional[str] = None,
                     iscsi_server_name: Optional[str] = None,
                     manager_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIscsiServerResult:
    """
    The iSCSI server.


    :param str device_name: The device name.
    :param str iscsi_server_name: The iSCSI server name.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    pulumi.log.warn("""get_iscsi_server is deprecated: Version 2016-10-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['iscsiServerName'] = iscsi_server_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple/v20161001:getIscsiServer', __args__, opts=opts, typ=GetIscsiServerResult).value

    return AwaitableGetIscsiServerResult(
        backup_schedule_group_id=__ret__.backup_schedule_group_id,
        chap_id=__ret__.chap_id,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        reverse_chap_id=__ret__.reverse_chap_id,
        storage_domain_id=__ret__.storage_domain_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_iscsi_server)
def get_iscsi_server_output(device_name: Optional[pulumi.Input[str]] = None,
                            iscsi_server_name: Optional[pulumi.Input[str]] = None,
                            manager_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIscsiServerResult]:
    """
    The iSCSI server.


    :param str device_name: The device name.
    :param str iscsi_server_name: The iSCSI server name.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    pulumi.log.warn("""get_iscsi_server is deprecated: Version 2016-10-01 will be removed in v2 of the provider.""")
    ...
