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
    'GetPeeringResult',
    'AwaitableGetPeeringResult',
    'get_peering',
    'get_peering_output',
]

warnings.warn("""Version 2019-09-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetPeeringResult:
    """
    Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.
    """
    def __init__(__self__, direct=None, exchange=None, id=None, kind=None, location=None, name=None, peering_location=None, provisioning_state=None, sku=None, tags=None, type=None):
        if direct and not isinstance(direct, dict):
            raise TypeError("Expected argument 'direct' to be a dict")
        pulumi.set(__self__, "direct", direct)
        if exchange and not isinstance(exchange, dict):
            raise TypeError("Expected argument 'exchange' to be a dict")
        pulumi.set(__self__, "exchange", exchange)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peering_location and not isinstance(peering_location, str):
            raise TypeError("Expected argument 'peering_location' to be a str")
        pulumi.set(__self__, "peering_location", peering_location)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def direct(self) -> Optional['outputs.PeeringPropertiesDirectResponse']:
        """
        The properties that define a direct peering.
        """
        return pulumi.get(self, "direct")

    @property
    @pulumi.getter
    def exchange(self) -> Optional['outputs.PeeringPropertiesExchangeResponse']:
        """
        The properties that define an exchange peering.
        """
        return pulumi.get(self, "exchange")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the peering.
        """
        return pulumi.get(self, "kind")

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
    @pulumi.getter(name="peeringLocation")
    def peering_location(self) -> Optional[str]:
        """
        The location of the peering.
        """
        return pulumi.get(self, "peering_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.PeeringSkuResponse':
        """
        The SKU that defines the tier and kind of the peering.
        """
        return pulumi.get(self, "sku")

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


class AwaitableGetPeeringResult(GetPeeringResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPeeringResult(
            direct=self.direct,
            exchange=self.exchange,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            peering_location=self.peering_location,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_peering(peering_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPeeringResult:
    """
    Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.


    :param str peering_name: The name of the peering.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_peering is deprecated: Version 2019-09-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['peeringName'] = peering_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:peering/v20190901preview:getPeering', __args__, opts=opts, typ=GetPeeringResult).value

    return AwaitableGetPeeringResult(
        direct=__ret__.direct,
        exchange=__ret__.exchange,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        peering_location=__ret__.peering_location,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_peering)
def get_peering_output(peering_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPeeringResult]:
    """
    Peering is a logical representation of a set of connections to the Microsoft Cloud Edge at a location.


    :param str peering_name: The name of the peering.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_peering is deprecated: Version 2019-09-01-preview will be removed in v2 of the provider.""")
    ...
