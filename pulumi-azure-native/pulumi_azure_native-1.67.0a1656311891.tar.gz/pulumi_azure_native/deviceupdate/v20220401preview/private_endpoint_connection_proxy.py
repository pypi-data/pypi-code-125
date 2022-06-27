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

__all__ = ['PrivateEndpointConnectionProxyArgs', 'PrivateEndpointConnectionProxy']

@pulumi.input_type
class PrivateEndpointConnectionProxyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 private_endpoint_connection_proxy_id: Optional[pulumi.Input[str]] = None,
                 remote_private_endpoint: Optional[pulumi.Input['RemotePrivateEndpointArgs']] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnectionProxy resource.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] private_endpoint_connection_proxy_id: The ID of the private endpoint connection proxy object.
        :param pulumi.Input['RemotePrivateEndpointArgs'] remote_private_endpoint: Remote private endpoint details.
        :param pulumi.Input[str] status: Operation status.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if private_endpoint_connection_proxy_id is not None:
            pulumi.set(__self__, "private_endpoint_connection_proxy_id", private_endpoint_connection_proxy_id)
        if remote_private_endpoint is not None:
            pulumi.set(__self__, "remote_private_endpoint", remote_private_endpoint)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="privateEndpointConnectionProxyId")
    def private_endpoint_connection_proxy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the private endpoint connection proxy object.
        """
        return pulumi.get(self, "private_endpoint_connection_proxy_id")

    @private_endpoint_connection_proxy_id.setter
    def private_endpoint_connection_proxy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_connection_proxy_id", value)

    @property
    @pulumi.getter(name="remotePrivateEndpoint")
    def remote_private_endpoint(self) -> Optional[pulumi.Input['RemotePrivateEndpointArgs']]:
        """
        Remote private endpoint details.
        """
        return pulumi.get(self, "remote_private_endpoint")

    @remote_private_endpoint.setter
    def remote_private_endpoint(self, value: Optional[pulumi.Input['RemotePrivateEndpointArgs']]):
        pulumi.set(self, "remote_private_endpoint", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Operation status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class PrivateEndpointConnectionProxy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_proxy_id: Optional[pulumi.Input[str]] = None,
                 remote_private_endpoint: Optional[pulumi.Input[pulumi.InputType['RemotePrivateEndpointArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Private endpoint connection proxy details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[str] private_endpoint_connection_proxy_id: The ID of the private endpoint connection proxy object.
        :param pulumi.Input[pulumi.InputType['RemotePrivateEndpointArgs']] remote_private_endpoint: Remote private endpoint details.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] status: Operation status.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointConnectionProxyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Private endpoint connection proxy details.

        :param str resource_name: The name of the resource.
        :param PrivateEndpointConnectionProxyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointConnectionProxyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_proxy_id: Optional[pulumi.Input[str]] = None,
                 remote_private_endpoint: Optional[pulumi.Input[pulumi.InputType['RemotePrivateEndpointArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
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
            __props__ = PrivateEndpointConnectionProxyArgs.__new__(PrivateEndpointConnectionProxyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["private_endpoint_connection_proxy_id"] = private_endpoint_connection_proxy_id
            __props__.__dict__["remote_private_endpoint"] = remote_private_endpoint
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:deviceupdate:PrivateEndpointConnectionProxy"), pulumi.Alias(type_="azure-native:deviceupdate/v20200301preview:PrivateEndpointConnectionProxy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnectionProxy, __self__).__init__(
            'azure-native:deviceupdate/v20220401preview:PrivateEndpointConnectionProxy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpointConnectionProxy':
        """
        Get an existing PrivateEndpointConnectionProxy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointConnectionProxyArgs.__new__(PrivateEndpointConnectionProxyArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["remote_private_endpoint"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnectionProxy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        ETag from NRP.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the private endpoint connection proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="remotePrivateEndpoint")
    def remote_private_endpoint(self) -> pulumi.Output[Optional['outputs.RemotePrivateEndpointResponse']]:
        """
        Remote private endpoint details.
        """
        return pulumi.get(self, "remote_private_endpoint")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Operation status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

