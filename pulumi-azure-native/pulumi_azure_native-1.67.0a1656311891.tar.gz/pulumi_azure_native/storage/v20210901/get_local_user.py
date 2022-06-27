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
    'GetLocalUserResult',
    'AwaitableGetLocalUserResult',
    'get_local_user',
    'get_local_user_output',
]

@pulumi.output_type
class GetLocalUserResult:
    """
    The local user associated with the storage accounts.
    """
    def __init__(__self__, has_shared_key=None, has_ssh_key=None, has_ssh_password=None, home_directory=None, id=None, name=None, permission_scopes=None, sid=None, ssh_authorized_keys=None, system_data=None, type=None):
        if has_shared_key and not isinstance(has_shared_key, bool):
            raise TypeError("Expected argument 'has_shared_key' to be a bool")
        pulumi.set(__self__, "has_shared_key", has_shared_key)
        if has_ssh_key and not isinstance(has_ssh_key, bool):
            raise TypeError("Expected argument 'has_ssh_key' to be a bool")
        pulumi.set(__self__, "has_ssh_key", has_ssh_key)
        if has_ssh_password and not isinstance(has_ssh_password, bool):
            raise TypeError("Expected argument 'has_ssh_password' to be a bool")
        pulumi.set(__self__, "has_ssh_password", has_ssh_password)
        if home_directory and not isinstance(home_directory, str):
            raise TypeError("Expected argument 'home_directory' to be a str")
        pulumi.set(__self__, "home_directory", home_directory)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permission_scopes and not isinstance(permission_scopes, list):
            raise TypeError("Expected argument 'permission_scopes' to be a list")
        pulumi.set(__self__, "permission_scopes", permission_scopes)
        if sid and not isinstance(sid, str):
            raise TypeError("Expected argument 'sid' to be a str")
        pulumi.set(__self__, "sid", sid)
        if ssh_authorized_keys and not isinstance(ssh_authorized_keys, list):
            raise TypeError("Expected argument 'ssh_authorized_keys' to be a list")
        pulumi.set(__self__, "ssh_authorized_keys", ssh_authorized_keys)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="hasSharedKey")
    def has_shared_key(self) -> Optional[bool]:
        """
        Indicates whether shared key exists. Set it to false to remove existing shared key.
        """
        return pulumi.get(self, "has_shared_key")

    @property
    @pulumi.getter(name="hasSshKey")
    def has_ssh_key(self) -> Optional[bool]:
        """
        Indicates whether ssh key exists. Set it to false to remove existing SSH key.
        """
        return pulumi.get(self, "has_ssh_key")

    @property
    @pulumi.getter(name="hasSshPassword")
    def has_ssh_password(self) -> Optional[bool]:
        """
        Indicates whether ssh password exists. Set it to false to remove existing SSH password.
        """
        return pulumi.get(self, "has_ssh_password")

    @property
    @pulumi.getter(name="homeDirectory")
    def home_directory(self) -> Optional[str]:
        """
        Optional, local user home directory.
        """
        return pulumi.get(self, "home_directory")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permissionScopes")
    def permission_scopes(self) -> Optional[Sequence['outputs.PermissionScopeResponse']]:
        """
        The permission scopes of the local user.
        """
        return pulumi.get(self, "permission_scopes")

    @property
    @pulumi.getter
    def sid(self) -> str:
        """
        A unique Security Identifier that is generated by the server.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="sshAuthorizedKeys")
    def ssh_authorized_keys(self) -> Optional[Sequence['outputs.SshPublicKeyResponse']]:
        """
        Optional, local user ssh authorized keys for SFTP.
        """
        return pulumi.get(self, "ssh_authorized_keys")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetLocalUserResult(GetLocalUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocalUserResult(
            has_shared_key=self.has_shared_key,
            has_ssh_key=self.has_ssh_key,
            has_ssh_password=self.has_ssh_password,
            home_directory=self.home_directory,
            id=self.id,
            name=self.name,
            permission_scopes=self.permission_scopes,
            sid=self.sid,
            ssh_authorized_keys=self.ssh_authorized_keys,
            system_data=self.system_data,
            type=self.type)


def get_local_user(account_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   username: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLocalUserResult:
    """
    The local user associated with the storage accounts.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str username: The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['username'] = username
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20210901:getLocalUser', __args__, opts=opts, typ=GetLocalUserResult).value

    return AwaitableGetLocalUserResult(
        has_shared_key=__ret__.has_shared_key,
        has_ssh_key=__ret__.has_ssh_key,
        has_ssh_password=__ret__.has_ssh_password,
        home_directory=__ret__.home_directory,
        id=__ret__.id,
        name=__ret__.name,
        permission_scopes=__ret__.permission_scopes,
        sid=__ret__.sid,
        ssh_authorized_keys=__ret__.ssh_authorized_keys,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_local_user)
def get_local_user_output(account_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          username: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLocalUserResult]:
    """
    The local user associated with the storage accounts.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str username: The name of local user. The username must contain lowercase letters and numbers only. It must be unique only within the storage account.
    """
    ...
