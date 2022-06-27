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
    'GetVirtualRouterResult',
    'AwaitableGetVirtualRouterResult',
    'get_virtual_router',
    'get_virtual_router_output',
]

@pulumi.output_type
class GetVirtualRouterResult:
    """
    VirtualRouter Resource.
    """
    def __init__(__self__, etag=None, hosted_gateway=None, hosted_subnet=None, id=None, location=None, name=None, peerings=None, provisioning_state=None, tags=None, type=None, virtual_router_asn=None, virtual_router_ips=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if hosted_gateway and not isinstance(hosted_gateway, dict):
            raise TypeError("Expected argument 'hosted_gateway' to be a dict")
        pulumi.set(__self__, "hosted_gateway", hosted_gateway)
        if hosted_subnet and not isinstance(hosted_subnet, dict):
            raise TypeError("Expected argument 'hosted_subnet' to be a dict")
        pulumi.set(__self__, "hosted_subnet", hosted_subnet)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peerings and not isinstance(peerings, list):
            raise TypeError("Expected argument 'peerings' to be a list")
        pulumi.set(__self__, "peerings", peerings)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_router_asn and not isinstance(virtual_router_asn, float):
            raise TypeError("Expected argument 'virtual_router_asn' to be a float")
        pulumi.set(__self__, "virtual_router_asn", virtual_router_asn)
        if virtual_router_ips and not isinstance(virtual_router_ips, list):
            raise TypeError("Expected argument 'virtual_router_ips' to be a list")
        pulumi.set(__self__, "virtual_router_ips", virtual_router_ips)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="hostedGateway")
    def hosted_gateway(self) -> Optional['outputs.SubResourceResponse']:
        """
        The Gateway on which VirtualRouter is hosted.
        """
        return pulumi.get(self, "hosted_gateway")

    @property
    @pulumi.getter(name="hostedSubnet")
    def hosted_subnet(self) -> Optional['outputs.SubResourceResponse']:
        """
        The Subnet on which VirtualRouter is hosted.
        """
        return pulumi.get(self, "hosted_subnet")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def peerings(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to VirtualRouterPeerings.
        """
        return pulumi.get(self, "peerings")

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
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> Optional[float]:
        """
        VirtualRouter ASN.
        """
        return pulumi.get(self, "virtual_router_asn")

    @property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> Optional[Sequence[str]]:
        """
        VirtualRouter IPs.
        """
        return pulumi.get(self, "virtual_router_ips")


class AwaitableGetVirtualRouterResult(GetVirtualRouterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualRouterResult(
            etag=self.etag,
            hosted_gateway=self.hosted_gateway,
            hosted_subnet=self.hosted_subnet,
            id=self.id,
            location=self.location,
            name=self.name,
            peerings=self.peerings,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type,
            virtual_router_asn=self.virtual_router_asn,
            virtual_router_ips=self.virtual_router_ips)


def get_virtual_router(expand: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       virtual_router_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualRouterResult:
    """
    VirtualRouter Resource.


    :param str expand: Expands referenced resources.
    :param str resource_group_name: The name of the resource group.
    :param str virtual_router_name: The name of the Virtual Router.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualRouterName'] = virtual_router_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200501:getVirtualRouter', __args__, opts=opts, typ=GetVirtualRouterResult).value

    return AwaitableGetVirtualRouterResult(
        etag=__ret__.etag,
        hosted_gateway=__ret__.hosted_gateway,
        hosted_subnet=__ret__.hosted_subnet,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        peerings=__ret__.peerings,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_router_asn=__ret__.virtual_router_asn,
        virtual_router_ips=__ret__.virtual_router_ips)


@_utilities.lift_output_func(get_virtual_router)
def get_virtual_router_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              virtual_router_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualRouterResult]:
    """
    VirtualRouter Resource.


    :param str expand: Expands referenced resources.
    :param str resource_group_name: The name of the resource group.
    :param str virtual_router_name: The name of the Virtual Router.
    """
    ...
