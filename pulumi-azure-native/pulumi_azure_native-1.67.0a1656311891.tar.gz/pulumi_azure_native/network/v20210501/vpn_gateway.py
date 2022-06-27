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

__all__ = ['VpnGatewayArgs', 'VpnGateway']

@pulumi.input_type
class VpnGatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 bgp_settings: Optional[pulumi.Input['BgpSettingsArgs']] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionArgs']]]] = None,
                 enable_bgp_route_translation_for_nat: Optional[pulumi.Input[bool]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_routing_preference_internet: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 nat_rules: Optional[pulumi.Input[Sequence[pulumi.Input['VpnGatewayNatRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input['SubResourceArgs']] = None,
                 vpn_gateway_scale_unit: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a VpnGateway resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VpnGateway.
        :param pulumi.Input['BgpSettingsArgs'] bgp_settings: Local network gateway's BGP speaker settings.
        :param pulumi.Input[Sequence[pulumi.Input['VpnConnectionArgs']]] connections: List of all vpn connections to the gateway.
        :param pulumi.Input[bool] enable_bgp_route_translation_for_nat: Enable BGP routes translation for NAT on this VpnGateway.
        :param pulumi.Input[str] gateway_name: The name of the gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[bool] is_routing_preference_internet: Enable Routing Preference property for the Public IP Interface of the VpnGateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['VpnGatewayNatRuleArgs']]] nat_rules: List of all the nat Rules associated with the gateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input['SubResourceArgs'] virtual_hub: The VirtualHub to which the gateway belongs.
        :param pulumi.Input[int] vpn_gateway_scale_unit: The scale unit for this vpn gateway.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if bgp_settings is not None:
            pulumi.set(__self__, "bgp_settings", bgp_settings)
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if enable_bgp_route_translation_for_nat is not None:
            pulumi.set(__self__, "enable_bgp_route_translation_for_nat", enable_bgp_route_translation_for_nat)
        if gateway_name is not None:
            pulumi.set(__self__, "gateway_name", gateway_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if is_routing_preference_internet is not None:
            pulumi.set(__self__, "is_routing_preference_internet", is_routing_preference_internet)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if nat_rules is not None:
            pulumi.set(__self__, "nat_rules", nat_rules)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_hub is not None:
            pulumi.set(__self__, "virtual_hub", virtual_hub)
        if vpn_gateway_scale_unit is not None:
            pulumi.set(__self__, "vpn_gateway_scale_unit", vpn_gateway_scale_unit)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the VpnGateway.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[pulumi.Input['BgpSettingsArgs']]:
        """
        Local network gateway's BGP speaker settings.
        """
        return pulumi.get(self, "bgp_settings")

    @bgp_settings.setter
    def bgp_settings(self, value: Optional[pulumi.Input['BgpSettingsArgs']]):
        pulumi.set(self, "bgp_settings", value)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionArgs']]]]:
        """
        List of all vpn connections to the gateway.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnConnectionArgs']]]]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter(name="enableBgpRouteTranslationForNat")
    def enable_bgp_route_translation_for_nat(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable BGP routes translation for NAT on this VpnGateway.
        """
        return pulumi.get(self, "enable_bgp_route_translation_for_nat")

    @enable_bgp_route_translation_for_nat.setter
    def enable_bgp_route_translation_for_nat(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_bgp_route_translation_for_nat", value)

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the gateway.
        """
        return pulumi.get(self, "gateway_name")

    @gateway_name.setter
    def gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_name", value)

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
    @pulumi.getter(name="isRoutingPreferenceInternet")
    def is_routing_preference_internet(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable Routing Preference property for the Public IP Interface of the VpnGateway.
        """
        return pulumi.get(self, "is_routing_preference_internet")

    @is_routing_preference_internet.setter
    def is_routing_preference_internet(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_routing_preference_internet", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="natRules")
    def nat_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VpnGatewayNatRuleArgs']]]]:
        """
        List of all the nat Rules associated with the gateway.
        """
        return pulumi.get(self, "nat_rules")

    @nat_rules.setter
    def nat_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VpnGatewayNatRuleArgs']]]]):
        pulumi.set(self, "nat_rules", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The VirtualHub to which the gateway belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @virtual_hub.setter
    def virtual_hub(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "virtual_hub", value)

    @property
    @pulumi.getter(name="vpnGatewayScaleUnit")
    def vpn_gateway_scale_unit(self) -> Optional[pulumi.Input[int]]:
        """
        The scale unit for this vpn gateway.
        """
        return pulumi.get(self, "vpn_gateway_scale_unit")

    @vpn_gateway_scale_unit.setter
    def vpn_gateway_scale_unit(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "vpn_gateway_scale_unit", value)


class VpnGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['BgpSettingsArgs']]] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionArgs']]]]] = None,
                 enable_bgp_route_translation_for_nat: Optional[pulumi.Input[bool]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_routing_preference_internet: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 nat_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnGatewayNatRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 vpn_gateway_scale_unit: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        VpnGateway Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BgpSettingsArgs']] bgp_settings: Local network gateway's BGP speaker settings.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionArgs']]]] connections: List of all vpn connections to the gateway.
        :param pulumi.Input[bool] enable_bgp_route_translation_for_nat: Enable BGP routes translation for NAT on this VpnGateway.
        :param pulumi.Input[str] gateway_name: The name of the gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[bool] is_routing_preference_internet: Enable Routing Preference property for the Public IP Interface of the VpnGateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnGatewayNatRuleArgs']]]] nat_rules: List of all the nat Rules associated with the gateway.
        :param pulumi.Input[str] resource_group_name: The resource group name of the VpnGateway.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] virtual_hub: The VirtualHub to which the gateway belongs.
        :param pulumi.Input[int] vpn_gateway_scale_unit: The scale unit for this vpn gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VpnGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VpnGateway Resource.

        :param str resource_name: The name of the resource.
        :param VpnGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VpnGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['BgpSettingsArgs']]] = None,
                 connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnConnectionArgs']]]]] = None,
                 enable_bgp_route_translation_for_nat: Optional[pulumi.Input[bool]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 is_routing_preference_internet: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 nat_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VpnGatewayNatRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_hub: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 vpn_gateway_scale_unit: Optional[pulumi.Input[int]] = None,
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
            __props__ = VpnGatewayArgs.__new__(VpnGatewayArgs)

            __props__.__dict__["bgp_settings"] = bgp_settings
            __props__.__dict__["connections"] = connections
            __props__.__dict__["enable_bgp_route_translation_for_nat"] = enable_bgp_route_translation_for_nat
            __props__.__dict__["gateway_name"] = gateway_name
            __props__.__dict__["id"] = id
            __props__.__dict__["is_routing_preference_internet"] = is_routing_preference_internet
            __props__.__dict__["location"] = location
            __props__.__dict__["nat_rules"] = nat_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_hub"] = virtual_hub
            __props__.__dict__["vpn_gateway_scale_unit"] = vpn_gateway_scale_unit
            __props__.__dict__["etag"] = None
            __props__.__dict__["ip_configurations"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20180401:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20180601:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20180701:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20180801:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20181001:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20181101:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20181201:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20190201:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20190401:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20190601:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20190701:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20190801:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20190901:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20191101:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20191201:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20200301:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20200401:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20200501:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20200601:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20200701:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20200801:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20201101:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20210201:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20210301:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20210801:VpnGateway"), pulumi.Alias(type_="azure-native:network/v20220101:VpnGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VpnGateway, __self__).__init__(
            'azure-native:network/v20210501:VpnGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VpnGateway':
        """
        Get an existing VpnGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VpnGatewayArgs.__new__(VpnGatewayArgs)

        __props__.__dict__["bgp_settings"] = None
        __props__.__dict__["connections"] = None
        __props__.__dict__["enable_bgp_route_translation_for_nat"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["ip_configurations"] = None
        __props__.__dict__["is_routing_preference_internet"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["nat_rules"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_hub"] = None
        __props__.__dict__["vpn_gateway_scale_unit"] = None
        return VpnGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> pulumi.Output[Optional['outputs.BgpSettingsResponse']]:
        """
        Local network gateway's BGP speaker settings.
        """
        return pulumi.get(self, "bgp_settings")

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output[Optional[Sequence['outputs.VpnConnectionResponse']]]:
        """
        List of all vpn connections to the gateway.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter(name="enableBgpRouteTranslationForNat")
    def enable_bgp_route_translation_for_nat(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable BGP routes translation for NAT on this VpnGateway.
        """
        return pulumi.get(self, "enable_bgp_route_translation_for_nat")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> pulumi.Output[Sequence['outputs.VpnGatewayIpConfigurationResponse']]:
        """
        List of all IPs configured on the gateway.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter(name="isRoutingPreferenceInternet")
    def is_routing_preference_internet(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable Routing Preference property for the Public IP Interface of the VpnGateway.
        """
        return pulumi.get(self, "is_routing_preference_internet")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="natRules")
    def nat_rules(self) -> pulumi.Output[Optional[Sequence['outputs.VpnGatewayNatRuleResponse']]]:
        """
        List of all the nat Rules associated with the gateway.
        """
        return pulumi.get(self, "nat_rules")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the VPN gateway resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The VirtualHub to which the gateway belongs.
        """
        return pulumi.get(self, "virtual_hub")

    @property
    @pulumi.getter(name="vpnGatewayScaleUnit")
    def vpn_gateway_scale_unit(self) -> pulumi.Output[Optional[int]]:
        """
        The scale unit for this vpn gateway.
        """
        return pulumi.get(self, "vpn_gateway_scale_unit")

