# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['ArcAddonArgs', 'ArcAddon']

@pulumi.input_type
class ArcAddonArgs:
    def __init__(__self__, *,
                 device_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_location: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 role_name: pulumi.Input[str],
                 subscription_id: pulumi.Input[str],
                 addon_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ArcAddon resource.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[str] kind: Addon type.
               Expected value is 'ArcForKubernetes'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] resource_location: Arc resource location
        :param pulumi.Input[str] resource_name: Arc resource Name
        :param pulumi.Input[str] role_name: The role name.
        :param pulumi.Input[str] subscription_id: Arc resource subscription Id
        :param pulumi.Input[str] addon_name: The addon name.
        """
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "kind", 'ArcForKubernetes')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_location", resource_location)
        pulumi.set(__self__, "resource_name", resource_name)
        pulumi.set(__self__, "role_name", role_name)
        pulumi.set(__self__, "subscription_id", subscription_id)
        if addon_name is not None:
            pulumi.set(__self__, "addon_name", addon_name)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Addon type.
        Expected value is 'ArcForKubernetes'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

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
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> pulumi.Input[str]:
        """
        Arc resource location
        """
        return pulumi.get(self, "resource_location")

    @resource_location.setter
    def resource_location(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_location", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        Arc resource Name
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[str]:
        """
        The role name.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_name", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Input[str]:
        """
        Arc resource subscription Id
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> Optional[pulumi.Input[str]]:
        """
        The addon name.
        """
        return pulumi.get(self, "addon_name")

    @addon_name.setter
    def addon_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_name", value)


class ArcAddon(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_location: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Arc Addon.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] addon_name: The addon name.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[str] kind: Addon type.
               Expected value is 'ArcForKubernetes'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] resource_location: Arc resource location
        :param pulumi.Input[str] resource_name_: Arc resource Name
        :param pulumi.Input[str] role_name: The role name.
        :param pulumi.Input[str] subscription_id: Arc resource subscription Id
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ArcAddonArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Arc Addon.

        :param str resource_name: The name of the resource.
        :param ArcAddonArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ArcAddonArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_location: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ArcAddonArgs.__new__(ArcAddonArgs)

            __props__.__dict__["addon_name"] = addon_name
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'ArcForKubernetes'
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_location is None and not opts.urn:
                raise TypeError("Missing required property 'resource_location'")
            __props__.__dict__["resource_location"] = resource_location
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            if role_name is None and not opts.urn:
                raise TypeError("Missing required property 'role_name'")
            __props__.__dict__["role_name"] = role_name
            if subscription_id is None and not opts.urn:
                raise TypeError("Missing required property 'subscription_id'")
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["host_platform"] = None
            __props__.__dict__["host_platform_type"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databoxedge:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20200901:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210201:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210601:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210601preview:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20220301:ArcAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20220401preview:ArcAddon")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ArcAddon, __self__).__init__(
            'azure-native:databoxedge/v20200901preview:ArcAddon',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ArcAddon':
        """
        Get an existing ArcAddon resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ArcAddonArgs.__new__(ArcAddonArgs)

        __props__.__dict__["host_platform"] = None
        __props__.__dict__["host_platform_type"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_group_name"] = None
        __props__.__dict__["resource_location"] = None
        __props__.__dict__["resource_name"] = None
        __props__.__dict__["subscription_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return ArcAddon(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Output[str]:
        """
        Host OS supported by the Arc addon.
        """
        return pulumi.get(self, "host_platform")

    @property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> pulumi.Output[str]:
        """
        Platform where the runtime is hosted.
        """
        return pulumi.get(self, "host_platform_type")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Addon type.
        Expected value is 'ArcForKubernetes'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Addon Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Output[str]:
        """
        Arc resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> pulumi.Output[str]:
        """
        Arc resource location
        """
        return pulumi.get(self, "resource_location")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[str]:
        """
        Arc resource Name
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[str]:
        """
        Arc resource subscription Id
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Addon type
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Arc resource version
        """
        return pulumi.get(self, "version")

