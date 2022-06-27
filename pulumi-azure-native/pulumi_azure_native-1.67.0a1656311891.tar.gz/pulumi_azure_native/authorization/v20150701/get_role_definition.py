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
    'GetRoleDefinitionResult',
    'AwaitableGetRoleDefinitionResult',
    'get_role_definition',
    'get_role_definition_output',
]

warnings.warn("""Version 2015-07-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetRoleDefinitionResult:
    """
    Role definition.
    """
    def __init__(__self__, assignable_scopes=None, description=None, id=None, name=None, permissions=None, role_name=None, role_type=None, type=None):
        if assignable_scopes and not isinstance(assignable_scopes, list):
            raise TypeError("Expected argument 'assignable_scopes' to be a list")
        pulumi.set(__self__, "assignable_scopes", assignable_scopes)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permissions and not isinstance(permissions, list):
            raise TypeError("Expected argument 'permissions' to be a list")
        pulumi.set(__self__, "permissions", permissions)
        if role_name and not isinstance(role_name, str):
            raise TypeError("Expected argument 'role_name' to be a str")
        pulumi.set(__self__, "role_name", role_name)
        if role_type and not isinstance(role_type, str):
            raise TypeError("Expected argument 'role_type' to be a str")
        pulumi.set(__self__, "role_type", role_type)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Optional[Sequence[str]]:
        """
        Role definition assignable scopes.
        """
        return pulumi.get(self, "assignable_scopes")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The role definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The role definition ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The role definition name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> Optional[Sequence['outputs.PermissionResponse']]:
        """
        Role definition permissions.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[str]:
        """
        The role name.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[str]:
        """
        The role type.
        """
        return pulumi.get(self, "role_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The role definition type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRoleDefinitionResult(GetRoleDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleDefinitionResult(
            assignable_scopes=self.assignable_scopes,
            description=self.description,
            id=self.id,
            name=self.name,
            permissions=self.permissions,
            role_name=self.role_name,
            role_type=self.role_type,
            type=self.type)


def get_role_definition(role_definition_id: Optional[str] = None,
                        scope: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoleDefinitionResult:
    """
    Role definition.


    :param str role_definition_id: The ID of the role definition.
    :param str scope: The scope of the role definition.
    """
    pulumi.log.warn("""get_role_definition is deprecated: Version 2015-07-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['roleDefinitionId'] = role_definition_id
    __args__['scope'] = scope
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:authorization/v20150701:getRoleDefinition', __args__, opts=opts, typ=GetRoleDefinitionResult).value

    return AwaitableGetRoleDefinitionResult(
        assignable_scopes=__ret__.assignable_scopes,
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        permissions=__ret__.permissions,
        role_name=__ret__.role_name,
        role_type=__ret__.role_type,
        type=__ret__.type)


@_utilities.lift_output_func(get_role_definition)
def get_role_definition_output(role_definition_id: Optional[pulumi.Input[str]] = None,
                               scope: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoleDefinitionResult]:
    """
    Role definition.


    :param str role_definition_id: The ID of the role definition.
    :param str scope: The scope of the role definition.
    """
    pulumi.log.warn("""get_role_definition is deprecated: Version 2015-07-01 will be removed in v2 of the provider.""")
    ...
