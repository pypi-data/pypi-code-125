# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetServiceEndpointPolicyDefinitionResult',
    'AwaitableGetServiceEndpointPolicyDefinitionResult',
    'get_service_endpoint_policy_definition',
    'get_service_endpoint_policy_definition_output',
]

@pulumi.output_type
class GetServiceEndpointPolicyDefinitionResult:
    """
    Service Endpoint policy definitions.
    """
    def __init__(__self__, description=None, etag=None, id=None, name=None, provisioning_state=None, service=None, service_resources=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service and not isinstance(service, str):
            raise TypeError("Expected argument 'service' to be a str")
        pulumi.set(__self__, "service", service)
        if service_resources and not isinstance(service_resources, list):
            raise TypeError("Expected argument 'service_resources' to be a list")
        pulumi.set(__self__, "service_resources", service_resources)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for this rule. Restricted to 140 chars.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the service end point policy definition. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def service(self) -> Optional[str]:
        """
        service endpoint name.
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter(name="serviceResources")
    def service_resources(self) -> Optional[Sequence[str]]:
        """
        A list of service resources.
        """
        return pulumi.get(self, "service_resources")


class AwaitableGetServiceEndpointPolicyDefinitionResult(GetServiceEndpointPolicyDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceEndpointPolicyDefinitionResult(
            description=self.description,
            etag=self.etag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service=self.service,
            service_resources=self.service_resources)


def get_service_endpoint_policy_definition(resource_group_name: Optional[str] = None,
                                           service_endpoint_policy_definition_name: Optional[str] = None,
                                           service_endpoint_policy_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceEndpointPolicyDefinitionResult:
    """
    Service Endpoint policy definitions.


    :param str resource_group_name: The name of the resource group.
    :param str service_endpoint_policy_definition_name: The name of the service endpoint policy definition name.
    :param str service_endpoint_policy_name: The name of the service endpoint policy name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceEndpointPolicyDefinitionName'] = service_endpoint_policy_definition_name
    __args__['serviceEndpointPolicyName'] = service_endpoint_policy_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20181101:getServiceEndpointPolicyDefinition', __args__, opts=opts, typ=GetServiceEndpointPolicyDefinitionResult).value

    return AwaitableGetServiceEndpointPolicyDefinitionResult(
        description=__ret__.description,
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        service=__ret__.service,
        service_resources=__ret__.service_resources)


@_utilities.lift_output_func(get_service_endpoint_policy_definition)
def get_service_endpoint_policy_definition_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  service_endpoint_policy_definition_name: Optional[pulumi.Input[str]] = None,
                                                  service_endpoint_policy_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceEndpointPolicyDefinitionResult]:
    """
    Service Endpoint policy definitions.


    :param str resource_group_name: The name of the resource group.
    :param str service_endpoint_policy_definition_name: The name of the service endpoint policy definition name.
    :param str service_endpoint_policy_name: The name of the service endpoint policy name.
    """
    ...
