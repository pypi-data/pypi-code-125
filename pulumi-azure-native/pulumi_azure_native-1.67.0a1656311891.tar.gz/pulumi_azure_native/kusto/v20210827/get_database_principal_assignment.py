# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDatabasePrincipalAssignmentResult',
    'AwaitableGetDatabasePrincipalAssignmentResult',
    'get_database_principal_assignment',
    'get_database_principal_assignment_output',
]

@pulumi.output_type
class GetDatabasePrincipalAssignmentResult:
    """
    Class representing a database principal assignment.
    """
    def __init__(__self__, id=None, name=None, principal_id=None, principal_name=None, principal_type=None, provisioning_state=None, role=None, tenant_id=None, tenant_name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal_id and not isinstance(principal_id, str):
            raise TypeError("Expected argument 'principal_id' to be a str")
        pulumi.set(__self__, "principal_id", principal_id)
        if principal_name and not isinstance(principal_name, str):
            raise TypeError("Expected argument 'principal_name' to be a str")
        pulumi.set(__self__, "principal_name", principal_name)
        if principal_type and not isinstance(principal_type, str):
            raise TypeError("Expected argument 'principal_type' to be a str")
        pulumi.set(__self__, "principal_type", principal_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if role and not isinstance(role, str):
            raise TypeError("Expected argument 'role' to be a str")
        pulumi.set(__self__, "role", role)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if tenant_name and not isinstance(tenant_name, str):
            raise TypeError("Expected argument 'tenant_name' to be a str")
        pulumi.set(__self__, "tenant_name", tenant_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID assigned to the database principal. It can be a user email, application ID, or security group name.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> str:
        """
        The principal name
        """
        return pulumi.get(self, "principal_name")

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> str:
        """
        Principal type.
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def role(self) -> str:
        """
        Database principal role.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The tenant id of the principal
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> str:
        """
        The tenant name of the principal
        """
        return pulumi.get(self, "tenant_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDatabasePrincipalAssignmentResult(GetDatabasePrincipalAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabasePrincipalAssignmentResult(
            id=self.id,
            name=self.name,
            principal_id=self.principal_id,
            principal_name=self.principal_name,
            principal_type=self.principal_type,
            provisioning_state=self.provisioning_state,
            role=self.role,
            tenant_id=self.tenant_id,
            tenant_name=self.tenant_name,
            type=self.type)


def get_database_principal_assignment(cluster_name: Optional[str] = None,
                                      database_name: Optional[str] = None,
                                      principal_assignment_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabasePrincipalAssignmentResult:
    """
    Class representing a database principal assignment.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str principal_assignment_name: The name of the Kusto principalAssignment.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['databaseName'] = database_name
    __args__['principalAssignmentName'] = principal_assignment_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20210827:getDatabasePrincipalAssignment', __args__, opts=opts, typ=GetDatabasePrincipalAssignmentResult).value

    return AwaitableGetDatabasePrincipalAssignmentResult(
        id=__ret__.id,
        name=__ret__.name,
        principal_id=__ret__.principal_id,
        principal_name=__ret__.principal_name,
        principal_type=__ret__.principal_type,
        provisioning_state=__ret__.provisioning_state,
        role=__ret__.role,
        tenant_id=__ret__.tenant_id,
        tenant_name=__ret__.tenant_name,
        type=__ret__.type)


@_utilities.lift_output_func(get_database_principal_assignment)
def get_database_principal_assignment_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                             database_name: Optional[pulumi.Input[str]] = None,
                                             principal_assignment_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabasePrincipalAssignmentResult]:
    """
    Class representing a database principal assignment.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str principal_assignment_name: The name of the Kusto principalAssignment.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
