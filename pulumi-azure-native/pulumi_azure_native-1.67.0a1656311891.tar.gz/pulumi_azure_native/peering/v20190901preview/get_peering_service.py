# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetPeeringServiceResult',
    'AwaitableGetPeeringServiceResult',
    'get_peering_service',
    'get_peering_service_output',
]

warnings.warn("""Version 2019-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetPeeringServiceResult:
    """
    Peering Service
    """
    def __init__(__self__, id=None, location=None, name=None, peering_service_location=None, peering_service_provider=None, provisioning_state=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peering_service_location and not isinstance(peering_service_location, str):
            raise TypeError("Expected argument 'peering_service_location' to be a str")
        pulumi.set(__self__, "peering_service_location", peering_service_location)
        if peering_service_provider and not isinstance(peering_service_provider, str):
            raise TypeError("Expected argument 'peering_service_provider' to be a str")
        pulumi.set(__self__, "peering_service_provider", peering_service_provider)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringServiceLocation")
    def peering_service_location(self) -> Optional[str]:
        """
        The PeeringServiceLocation of the Customer.
        """
        return pulumi.get(self, "peering_service_location")

    @property
    @pulumi.getter(name="peeringServiceProvider")
    def peering_service_provider(self) -> Optional[str]:
        """
        The MAPS Provider Name.
        """
        return pulumi.get(self, "peering_service_provider")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPeeringServiceResult(GetPeeringServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPeeringServiceResult(
            id=self.id,
            location=self.location,
            name=self.name,
            peering_service_location=self.peering_service_location,
            peering_service_provider=self.peering_service_provider,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_peering_service(peering_service_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPeeringServiceResult:
    """
    Peering Service


    :param str peering_service_name: The name of the peering.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_peering_service is deprecated: Version 2019-09-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['peeringServiceName'] = peering_service_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:peering/v20190901preview:getPeeringService', __args__, opts=opts, typ=GetPeeringServiceResult).value

    return AwaitableGetPeeringServiceResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        peering_service_location=__ret__.peering_service_location,
        peering_service_provider=__ret__.peering_service_provider,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_peering_service)
def get_peering_service_output(peering_service_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPeeringServiceResult]:
    """
    Peering Service


    :param str peering_service_name: The name of the peering.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_peering_service is deprecated: Version 2019-09-01-preview will be removed in v2 of the provider.""")
    ...
