# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['ManagedPrivateEndpointArgs', 'ManagedPrivateEndpoint']

@pulumi.input_type
class ManagedPrivateEndpointArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 group_id: pulumi.Input[str],
                 private_link_resource_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 managed_private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 private_link_resource_region: Optional[pulumi.Input[str]] = None,
                 request_message: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedPrivateEndpoint resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] group_id: The groupId in which the managed private endpoint is created.
        :param pulumi.Input[str] private_link_resource_id: The ARM resource ID of the resource for which the managed private endpoint is created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[str] managed_private_endpoint_name: The name of the managed private endpoint.
        :param pulumi.Input[str] private_link_resource_region: The region of the resource to which the managed private endpoint is created.
        :param pulumi.Input[str] request_message: The user request message.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if managed_private_endpoint_name is not None:
            pulumi.set(__self__, "managed_private_endpoint_name", managed_private_endpoint_name)
        if private_link_resource_region is not None:
            pulumi.set(__self__, "private_link_resource_region", private_link_resource_region)
        if request_message is not None:
            pulumi.set(__self__, "request_message", request_message)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The groupId in which the managed private endpoint is created.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Input[str]:
        """
        The ARM resource ID of the resource for which the managed private endpoint is created.
        """
        return pulumi.get(self, "private_link_resource_id")

    @private_link_resource_id.setter
    def private_link_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_link_resource_id", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the Kusto cluster.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="managedPrivateEndpointName")
    def managed_private_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the managed private endpoint.
        """
        return pulumi.get(self, "managed_private_endpoint_name")

    @managed_private_endpoint_name.setter
    def managed_private_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_private_endpoint_name", value)

    @property
    @pulumi.getter(name="privateLinkResourceRegion")
    def private_link_resource_region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the resource to which the managed private endpoint is created.
        """
        return pulumi.get(self, "private_link_resource_region")

    @private_link_resource_region.setter
    def private_link_resource_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_resource_region", value)

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[str]]:
        """
        The user request message.
        """
        return pulumi.get(self, "request_message")

    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_message", value)


class ManagedPrivateEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 managed_private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 private_link_resource_region: Optional[pulumi.Input[str]] = None,
                 request_message: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a managed private endpoint.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] group_id: The groupId in which the managed private endpoint is created.
        :param pulumi.Input[str] managed_private_endpoint_name: The name of the managed private endpoint.
        :param pulumi.Input[str] private_link_resource_id: The ARM resource ID of the resource for which the managed private endpoint is created.
        :param pulumi.Input[str] private_link_resource_region: The region of the resource to which the managed private endpoint is created.
        :param pulumi.Input[str] request_message: The user request message.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedPrivateEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a managed private endpoint.

        :param str resource_name: The name of the resource.
        :param ManagedPrivateEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedPrivateEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 managed_private_endpoint_name: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 private_link_resource_region: Optional[pulumi.Input[str]] = None,
                 request_message: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagedPrivateEndpointArgs.__new__(ManagedPrivateEndpointArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["managed_private_endpoint_name"] = managed_private_endpoint_name
            if private_link_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'private_link_resource_id'")
            __props__.__dict__["private_link_resource_id"] = private_link_resource_id
            __props__.__dict__["private_link_resource_region"] = private_link_resource_region
            __props__.__dict__["request_message"] = request_message
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto:ManagedPrivateEndpoint"), pulumi.Alias(type_="azure-native:kusto/v20210827:ManagedPrivateEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedPrivateEndpoint, __self__).__init__(
            'azure-native:kusto/v20220201:ManagedPrivateEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedPrivateEndpoint':
        """
        Get an existing ManagedPrivateEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedPrivateEndpointArgs.__new__(ManagedPrivateEndpointArgs)

        __props__.__dict__["group_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_link_resource_id"] = None
        __props__.__dict__["private_link_resource_region"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["request_message"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ManagedPrivateEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The groupId in which the managed private endpoint is created.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Output[str]:
        """
        The ARM resource ID of the resource for which the managed private endpoint is created.
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="privateLinkResourceRegion")
    def private_link_resource_region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of the resource to which the managed private endpoint is created.
        """
        return pulumi.get(self, "private_link_resource_region")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> pulumi.Output[Optional[str]]:
        """
        The user request message.
        """
        return pulumi.get(self, "request_message")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

