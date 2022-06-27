# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ExpressRouteConnectionArgs', 'ExpressRouteConnection']

@pulumi.input_type
class ExpressRouteConnectionArgs:
    def __init__(__self__, *,
                 express_route_circuit_peering: pulumi.Input['ExpressRouteCircuitPeeringIdArgs'],
                 express_route_gateway_name: pulumi.Input[str],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 enable_internet_security: Optional[pulumi.Input[bool]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 routing_weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a ExpressRouteConnection resource.
        :param pulumi.Input['ExpressRouteCircuitPeeringIdArgs'] express_route_circuit_peering: The ExpressRoute circuit peering.
        :param pulumi.Input[str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] authorization_key: Authorization key to establish the connection.
        :param pulumi.Input[str] connection_name: The name of the connection subresource.
        :param pulumi.Input[bool] enable_internet_security: Enable internet security.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] routing_weight: The routing weight associated to the connection.
        """
        pulumi.set(__self__, "express_route_circuit_peering", express_route_circuit_peering)
        pulumi.set(__self__, "express_route_gateway_name", express_route_gateway_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorization_key is not None:
            pulumi.set(__self__, "authorization_key", authorization_key)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if enable_internet_security is not None:
            pulumi.set(__self__, "enable_internet_security", enable_internet_security)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if routing_weight is not None:
            pulumi.set(__self__, "routing_weight", routing_weight)

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Input['ExpressRouteCircuitPeeringIdArgs']:
        """
        The ExpressRoute circuit peering.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @express_route_circuit_peering.setter
    def express_route_circuit_peering(self, value: pulumi.Input['ExpressRouteCircuitPeeringIdArgs']):
        pulumi.set(self, "express_route_circuit_peering", value)

    @property
    @pulumi.getter(name="expressRouteGatewayName")
    def express_route_gateway_name(self) -> pulumi.Input[str]:
        """
        The name of the ExpressRoute gateway.
        """
        return pulumi.get(self, "express_route_gateway_name")

    @express_route_gateway_name.setter
    def express_route_gateway_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "express_route_gateway_name", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization key to establish the connection.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the connection subresource.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable internet security.
        """
        return pulumi.get(self, "enable_internet_security")

    @enable_internet_security.setter
    def enable_internet_security(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_internet_security", value)

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
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> Optional[pulumi.Input[int]]:
        """
        The routing weight associated to the connection.
        """
        return pulumi.get(self, "routing_weight")

    @routing_weight.setter
    def routing_weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "routing_weight", value)


class ExpressRouteConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 enable_internet_security: Optional[pulumi.Input[bool]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringIdArgs']]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        ExpressRouteConnection resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_key: Authorization key to establish the connection.
        :param pulumi.Input[str] connection_name: The name of the connection subresource.
        :param pulumi.Input[bool] enable_internet_security: Enable internet security.
        :param pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringIdArgs']] express_route_circuit_peering: The ExpressRoute circuit peering.
        :param pulumi.Input[str] express_route_gateway_name: The name of the ExpressRoute gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[int] routing_weight: The routing weight associated to the connection.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ExpressRouteConnection resource.

        :param str resource_name: The name of the resource.
        :param ExpressRouteConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 enable_internet_security: Optional[pulumi.Input[bool]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringIdArgs']]] = None,
                 express_route_gateway_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_weight: Optional[pulumi.Input[int]] = None,
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
            __props__ = ExpressRouteConnectionArgs.__new__(ExpressRouteConnectionArgs)

            __props__.__dict__["authorization_key"] = authorization_key
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["enable_internet_security"] = enable_internet_security
            if express_route_circuit_peering is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_circuit_peering'")
            __props__.__dict__["express_route_circuit_peering"] = express_route_circuit_peering
            if express_route_gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_gateway_name'")
            __props__.__dict__["express_route_gateway_name"] = express_route_gateway_name
            __props__.__dict__["id"] = id
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routing_weight"] = routing_weight
            __props__.__dict__["provisioning_state"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20181001:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190701:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20210801:ExpressRouteConnection"), pulumi.Alias(type_="azure-native:network/v20220101:ExpressRouteConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteConnection, __self__).__init__(
            'azure-native:network/v20191201:ExpressRouteConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteConnection':
        """
        Get an existing ExpressRouteConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteConnectionArgs.__new__(ExpressRouteConnectionArgs)

        __props__.__dict__["authorization_key"] = None
        __props__.__dict__["enable_internet_security"] = None
        __props__.__dict__["express_route_circuit_peering"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["routing_weight"] = None
        return ExpressRouteConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[str]]:
        """
        Authorization key to establish the connection.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="enableInternetSecurity")
    def enable_internet_security(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable internet security.
        """
        return pulumi.get(self, "enable_internet_security")

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Output['outputs.ExpressRouteCircuitPeeringIdResponse']:
        """
        The ExpressRoute circuit peering.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the express route connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routingWeight")
    def routing_weight(self) -> pulumi.Output[Optional[int]]:
        """
        The routing weight associated to the connection.
        """
        return pulumi.get(self, "routing_weight")

