# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ExpressRouteCrossConnectionPeeringArgs', 'ExpressRouteCrossConnectionPeering']

@pulumi.input_type
class ExpressRouteCrossConnectionPeeringArgs:
    def __init__(__self__, *,
                 cross_connection_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 gateway_manager_etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ipv6_peering_config: Optional[pulumi.Input['Ipv6ExpressRouteCircuitPeeringConfigArgs']] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 microsoft_peering_config: Optional[pulumi.Input['ExpressRouteCircuitPeeringConfigArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_asn: Optional[pulumi.Input[float]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 peering_type: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringType']]] = None,
                 primary_peer_address_prefix: Optional[pulumi.Input[str]] = None,
                 secondary_peer_address_prefix: Optional[pulumi.Input[str]] = None,
                 shared_key: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringState']]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ExpressRouteCrossConnectionPeering resource.
        :param pulumi.Input[str] cross_connection_name: The name of the ExpressRouteCrossConnection.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] gateway_manager_etag: The GatewayManager Etag.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input['Ipv6ExpressRouteCircuitPeeringConfigArgs'] ipv6_peering_config: The IPv6 peering configuration.
        :param pulumi.Input[str] last_modified_by: Gets whether the provider or the customer last modified the peering.
        :param pulumi.Input['ExpressRouteCircuitPeeringConfigArgs'] microsoft_peering_config: The Microsoft peering configuration.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[float] peer_asn: The peer ASN.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[Union[str, 'ExpressRoutePeeringType']] peering_type: The peering type.
        :param pulumi.Input[str] primary_peer_address_prefix: The primary address prefix.
        :param pulumi.Input[str] secondary_peer_address_prefix: The secondary address prefix.
        :param pulumi.Input[str] shared_key: The shared key.
        :param pulumi.Input[Union[str, 'ExpressRoutePeeringState']] state: The peering state.
        :param pulumi.Input[int] vlan_id: The VLAN ID.
        """
        pulumi.set(__self__, "cross_connection_name", cross_connection_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if gateway_manager_etag is not None:
            pulumi.set(__self__, "gateway_manager_etag", gateway_manager_etag)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ipv6_peering_config is not None:
            pulumi.set(__self__, "ipv6_peering_config", ipv6_peering_config)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if microsoft_peering_config is not None:
            pulumi.set(__self__, "microsoft_peering_config", microsoft_peering_config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peer_asn is not None:
            pulumi.set(__self__, "peer_asn", peer_asn)
        if peering_name is not None:
            pulumi.set(__self__, "peering_name", peering_name)
        if peering_type is not None:
            pulumi.set(__self__, "peering_type", peering_type)
        if primary_peer_address_prefix is not None:
            pulumi.set(__self__, "primary_peer_address_prefix", primary_peer_address_prefix)
        if secondary_peer_address_prefix is not None:
            pulumi.set(__self__, "secondary_peer_address_prefix", secondary_peer_address_prefix)
        if shared_key is not None:
            pulumi.set(__self__, "shared_key", shared_key)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if vlan_id is not None:
            pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter(name="crossConnectionName")
    def cross_connection_name(self) -> pulumi.Input[str]:
        """
        The name of the ExpressRouteCrossConnection.
        """
        return pulumi.get(self, "cross_connection_name")

    @cross_connection_name.setter
    def cross_connection_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cross_connection_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="gatewayManagerEtag")
    def gateway_manager_etag(self) -> Optional[pulumi.Input[str]]:
        """
        The GatewayManager Etag.
        """
        return pulumi.get(self, "gateway_manager_etag")

    @gateway_manager_etag.setter
    def gateway_manager_etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_manager_etag", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="ipv6PeeringConfig")
    def ipv6_peering_config(self) -> Optional[pulumi.Input['Ipv6ExpressRouteCircuitPeeringConfigArgs']]:
        """
        The IPv6 peering configuration.
        """
        return pulumi.get(self, "ipv6_peering_config")

    @ipv6_peering_config.setter
    def ipv6_peering_config(self, value: Optional[pulumi.Input['Ipv6ExpressRouteCircuitPeeringConfigArgs']]):
        pulumi.set(self, "ipv6_peering_config", value)

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[pulumi.Input[str]]:
        """
        Gets whether the provider or the customer last modified the peering.
        """
        return pulumi.get(self, "last_modified_by")

    @last_modified_by.setter
    def last_modified_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_modified_by", value)

    @property
    @pulumi.getter(name="microsoftPeeringConfig")
    def microsoft_peering_config(self) -> Optional[pulumi.Input['ExpressRouteCircuitPeeringConfigArgs']]:
        """
        The Microsoft peering configuration.
        """
        return pulumi.get(self, "microsoft_peering_config")

    @microsoft_peering_config.setter
    def microsoft_peering_config(self, value: Optional[pulumi.Input['ExpressRouteCircuitPeeringConfigArgs']]):
        pulumi.set(self, "microsoft_peering_config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peerASN")
    def peer_asn(self) -> Optional[pulumi.Input[float]]:
        """
        The peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @peer_asn.setter
    def peer_asn(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "peer_asn", value)

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_name", value)

    @property
    @pulumi.getter(name="peeringType")
    def peering_type(self) -> Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringType']]]:
        """
        The peering type.
        """
        return pulumi.get(self, "peering_type")

    @peering_type.setter
    def peering_type(self, value: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringType']]]):
        pulumi.set(self, "peering_type", value)

    @property
    @pulumi.getter(name="primaryPeerAddressPrefix")
    def primary_peer_address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The primary address prefix.
        """
        return pulumi.get(self, "primary_peer_address_prefix")

    @primary_peer_address_prefix.setter
    def primary_peer_address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_peer_address_prefix", value)

    @property
    @pulumi.getter(name="secondaryPeerAddressPrefix")
    def secondary_peer_address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The secondary address prefix.
        """
        return pulumi.get(self, "secondary_peer_address_prefix")

    @secondary_peer_address_prefix.setter
    def secondary_peer_address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secondary_peer_address_prefix", value)

    @property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> Optional[pulumi.Input[str]]:
        """
        The shared key.
        """
        return pulumi.get(self, "shared_key")

    @shared_key.setter
    def shared_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_key", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringState']]]:
        """
        The peering state.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringState']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> Optional[pulumi.Input[int]]:
        """
        The VLAN ID.
        """
        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vlan_id", value)


class ExpressRouteCrossConnectionPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cross_connection_name: Optional[pulumi.Input[str]] = None,
                 gateway_manager_etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ipv6_peering_config: Optional[pulumi.Input[pulumi.InputType['Ipv6ExpressRouteCircuitPeeringConfigArgs']]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 microsoft_peering_config: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_asn: Optional[pulumi.Input[float]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 peering_type: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringType']]] = None,
                 primary_peer_address_prefix: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secondary_peer_address_prefix: Optional[pulumi.Input[str]] = None,
                 shared_key: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringState']]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Peering in an ExpressRoute Cross Connection resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cross_connection_name: The name of the ExpressRouteCrossConnection.
        :param pulumi.Input[str] gateway_manager_etag: The GatewayManager Etag.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[pulumi.InputType['Ipv6ExpressRouteCircuitPeeringConfigArgs']] ipv6_peering_config: The IPv6 peering configuration.
        :param pulumi.Input[str] last_modified_by: Gets whether the provider or the customer last modified the peering.
        :param pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringConfigArgs']] microsoft_peering_config: The Microsoft peering configuration.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[float] peer_asn: The peer ASN.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[Union[str, 'ExpressRoutePeeringType']] peering_type: The peering type.
        :param pulumi.Input[str] primary_peer_address_prefix: The primary address prefix.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] secondary_peer_address_prefix: The secondary address prefix.
        :param pulumi.Input[str] shared_key: The shared key.
        :param pulumi.Input[Union[str, 'ExpressRoutePeeringState']] state: The peering state.
        :param pulumi.Input[int] vlan_id: The VLAN ID.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteCrossConnectionPeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Peering in an ExpressRoute Cross Connection resource.

        :param str resource_name: The name of the resource.
        :param ExpressRouteCrossConnectionPeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteCrossConnectionPeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cross_connection_name: Optional[pulumi.Input[str]] = None,
                 gateway_manager_etag: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 ipv6_peering_config: Optional[pulumi.Input[pulumi.InputType['Ipv6ExpressRouteCircuitPeeringConfigArgs']]] = None,
                 last_modified_by: Optional[pulumi.Input[str]] = None,
                 microsoft_peering_config: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringConfigArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_asn: Optional[pulumi.Input[float]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 peering_type: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringType']]] = None,
                 primary_peer_address_prefix: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 secondary_peer_address_prefix: Optional[pulumi.Input[str]] = None,
                 shared_key: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ExpressRoutePeeringState']]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExpressRouteCrossConnectionPeeringArgs.__new__(ExpressRouteCrossConnectionPeeringArgs)

            if cross_connection_name is None and not opts.urn:
                raise TypeError("Missing required property 'cross_connection_name'")
            __props__.__dict__["cross_connection_name"] = cross_connection_name
            __props__.__dict__["gateway_manager_etag"] = gateway_manager_etag
            __props__.__dict__["id"] = id
            __props__.__dict__["ipv6_peering_config"] = ipv6_peering_config
            __props__.__dict__["last_modified_by"] = last_modified_by
            __props__.__dict__["microsoft_peering_config"] = microsoft_peering_config
            __props__.__dict__["name"] = name
            __props__.__dict__["peer_asn"] = peer_asn
            __props__.__dict__["peering_name"] = peering_name
            __props__.__dict__["peering_type"] = peering_type
            __props__.__dict__["primary_peer_address_prefix"] = primary_peer_address_prefix
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["secondary_peer_address_prefix"] = secondary_peer_address_prefix
            __props__.__dict__["shared_key"] = shared_key
            __props__.__dict__["state"] = state
            __props__.__dict__["vlan_id"] = vlan_id
            __props__.__dict__["azure_asn"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["primary_azure_port"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["secondary_azure_port"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20180201:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20180401:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20180601:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20180701:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20190201:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20190701:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20191201:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20210801:ExpressRouteCrossConnectionPeering"), pulumi.Alias(type_="azure-native:network/v20220101:ExpressRouteCrossConnectionPeering")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteCrossConnectionPeering, __self__).__init__(
            'azure-native:network/v20181001:ExpressRouteCrossConnectionPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteCrossConnectionPeering':
        """
        Get an existing ExpressRouteCrossConnectionPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteCrossConnectionPeeringArgs.__new__(ExpressRouteCrossConnectionPeeringArgs)

        __props__.__dict__["azure_asn"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["gateway_manager_etag"] = None
        __props__.__dict__["ipv6_peering_config"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["microsoft_peering_config"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_asn"] = None
        __props__.__dict__["peering_type"] = None
        __props__.__dict__["primary_azure_port"] = None
        __props__.__dict__["primary_peer_address_prefix"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["secondary_azure_port"] = None
        __props__.__dict__["secondary_peer_address_prefix"] = None
        __props__.__dict__["shared_key"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["vlan_id"] = None
        return ExpressRouteCrossConnectionPeering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureASN")
    def azure_asn(self) -> pulumi.Output[int]:
        """
        The Azure ASN.
        """
        return pulumi.get(self, "azure_asn")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="gatewayManagerEtag")
    def gateway_manager_etag(self) -> pulumi.Output[Optional[str]]:
        """
        The GatewayManager Etag.
        """
        return pulumi.get(self, "gateway_manager_etag")

    @property
    @pulumi.getter(name="ipv6PeeringConfig")
    def ipv6_peering_config(self) -> pulumi.Output[Optional['outputs.Ipv6ExpressRouteCircuitPeeringConfigResponse']]:
        """
        The IPv6 peering configuration.
        """
        return pulumi.get(self, "ipv6_peering_config")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[Optional[str]]:
        """
        Gets whether the provider or the customer last modified the peering.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="microsoftPeeringConfig")
    def microsoft_peering_config(self) -> pulumi.Output[Optional['outputs.ExpressRouteCircuitPeeringConfigResponse']]:
        """
        The Microsoft peering configuration.
        """
        return pulumi.get(self, "microsoft_peering_config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerASN")
    def peer_asn(self) -> pulumi.Output[Optional[float]]:
        """
        The peer ASN.
        """
        return pulumi.get(self, "peer_asn")

    @property
    @pulumi.getter(name="peeringType")
    def peering_type(self) -> pulumi.Output[Optional[str]]:
        """
        The peering type.
        """
        return pulumi.get(self, "peering_type")

    @property
    @pulumi.getter(name="primaryAzurePort")
    def primary_azure_port(self) -> pulumi.Output[str]:
        """
        The primary port.
        """
        return pulumi.get(self, "primary_azure_port")

    @property
    @pulumi.getter(name="primaryPeerAddressPrefix")
    def primary_peer_address_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The primary address prefix.
        """
        return pulumi.get(self, "primary_peer_address_prefix")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state of the public IP resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="secondaryAzurePort")
    def secondary_azure_port(self) -> pulumi.Output[str]:
        """
        The secondary port.
        """
        return pulumi.get(self, "secondary_azure_port")

    @property
    @pulumi.getter(name="secondaryPeerAddressPrefix")
    def secondary_peer_address_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The secondary address prefix.
        """
        return pulumi.get(self, "secondary_peer_address_prefix")

    @property
    @pulumi.getter(name="sharedKey")
    def shared_key(self) -> pulumi.Output[Optional[str]]:
        """
        The shared key.
        """
        return pulumi.get(self, "shared_key")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        The peering state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[Optional[int]]:
        """
        The VLAN ID.
        """
        return pulumi.get(self, "vlan_id")

