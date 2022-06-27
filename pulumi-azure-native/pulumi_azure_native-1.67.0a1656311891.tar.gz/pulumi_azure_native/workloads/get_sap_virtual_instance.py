# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSAPVirtualInstanceResult',
    'AwaitableGetSAPVirtualInstanceResult',
    'get_sap_virtual_instance',
    'get_sap_virtual_instance_output',
]

@pulumi.output_type
class GetSAPVirtualInstanceResult:
    """
    Define the Virtual Instance for SAP.
    """
    def __init__(__self__, configuration=None, environment=None, errors=None, health=None, id=None, identity=None, location=None, managed_resource_group_configuration=None, name=None, provisioning_state=None, sap_product=None, state=None, status=None, system_data=None, tags=None, type=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if environment and not isinstance(environment, str):
            raise TypeError("Expected argument 'environment' to be a str")
        pulumi.set(__self__, "environment", environment)
        if errors and not isinstance(errors, dict):
            raise TypeError("Expected argument 'errors' to be a dict")
        pulumi.set(__self__, "errors", errors)
        if health and not isinstance(health, str):
            raise TypeError("Expected argument 'health' to be a str")
        pulumi.set(__self__, "health", health)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration and not isinstance(managed_resource_group_configuration, dict):
            raise TypeError("Expected argument 'managed_resource_group_configuration' to be a dict")
        pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sap_product and not isinstance(sap_product, str):
            raise TypeError("Expected argument 'sap_product' to be a str")
        pulumi.set(__self__, "sap_product", sap_product)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def configuration(self) -> Any:
        """
        Defines if an existing SAP system is being registered or a new SAP system is being created
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def environment(self) -> str:
        """
        Defines the environment type - Production/Non Production.
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def errors(self) -> 'outputs.SAPVirtualInstanceErrorResponse':
        """
        Defines the Virtual Instance for SAP errors.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def health(self) -> str:
        """
        Defines the SAP Instance health.
        """
        return pulumi.get(self, "health")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.UserAssignedServiceIdentityResponse']:
        """
        Managed service identity (user assigned identities)
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional['outputs.ManagedRGConfigurationResponse']:
        """
        Managed resource group configuration
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Defines the provisioning states.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sapProduct")
    def sap_product(self) -> str:
        """
        Defines the SAP Product type.
        """
        return pulumi.get(self, "sap_product")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Defines the Virtual Instance for SAP state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Defines the SAP Instance status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

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


class AwaitableGetSAPVirtualInstanceResult(GetSAPVirtualInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAPVirtualInstanceResult(
            configuration=self.configuration,
            environment=self.environment,
            errors=self.errors,
            health=self.health,
            id=self.id,
            identity=self.identity,
            location=self.location,
            managed_resource_group_configuration=self.managed_resource_group_configuration,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sap_product=self.sap_product,
            state=self.state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_sap_virtual_instance(resource_group_name: Optional[str] = None,
                             sap_virtual_instance_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAPVirtualInstanceResult:
    """
    Define the Virtual Instance for SAP.
    API Version: 2021-12-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_virtual_instance_name: The name of the Virtual Instances for SAP.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sapVirtualInstanceName'] = sap_virtual_instance_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:workloads:getSAPVirtualInstance', __args__, opts=opts, typ=GetSAPVirtualInstanceResult).value

    return AwaitableGetSAPVirtualInstanceResult(
        configuration=__ret__.configuration,
        environment=__ret__.environment,
        errors=__ret__.errors,
        health=__ret__.health,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        managed_resource_group_configuration=__ret__.managed_resource_group_configuration,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        sap_product=__ret__.sap_product,
        state=__ret__.state,
        status=__ret__.status,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_sap_virtual_instance)
def get_sap_virtual_instance_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                    sap_virtual_instance_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAPVirtualInstanceResult]:
    """
    Define the Virtual Instance for SAP.
    API Version: 2021-12-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_virtual_instance_name: The name of the Virtual Instances for SAP.
    """
    ...
