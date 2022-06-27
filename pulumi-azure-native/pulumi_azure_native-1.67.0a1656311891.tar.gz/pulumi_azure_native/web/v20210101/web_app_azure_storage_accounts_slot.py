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

__all__ = ['WebAppAzureStorageAccountsSlotArgs', 'WebAppAzureStorageAccountsSlot']

@pulumi.input_type
class WebAppAzureStorageAccountsSlotArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 slot: pulumi.Input[str],
                 kind: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input['AzureStorageInfoValueArgs']]]] = None):
        """
        The set of arguments for constructing a WebAppAzureStorageAccountsSlot resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] slot: Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[Mapping[str, pulumi.Input['AzureStorageInfoValueArgs']]] properties: Azure storage accounts.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "slot", slot)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def slot(self) -> pulumi.Input[str]:
        """
        Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot.
        """
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: pulumi.Input[str]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['AzureStorageInfoValueArgs']]]]:
        """
        Azure storage accounts.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['AzureStorageInfoValueArgs']]]]):
        pulumi.set(self, "properties", value)


class WebAppAzureStorageAccountsSlot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['AzureStorageInfoValueArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        AzureStorageInfo dictionary resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['AzureStorageInfoValueArgs']]]] properties: Azure storage accounts.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] slot: Name of the deployment slot. If a slot is not specified, the API will update the Azure storage account configurations for the production slot.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppAzureStorageAccountsSlotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AzureStorageInfo dictionary resource.

        :param str resource_name: The name of the resource.
        :param WebAppAzureStorageAccountsSlotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppAzureStorageAccountsSlotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['AzureStorageInfoValueArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebAppAzureStorageAccountsSlotArgs.__new__(WebAppAzureStorageAccountsSlotArgs)

            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if slot is None and not opts.urn:
                raise TypeError("Missing required property 'slot'")
            __props__.__dict__["slot"] = slot
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20200901:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20210115:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20210201:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20210301:WebAppAzureStorageAccountsSlot"), pulumi.Alias(type_="azure-native:web/v20220301:WebAppAzureStorageAccountsSlot")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppAzureStorageAccountsSlot, __self__).__init__(
            'azure-native:web/v20210101:WebAppAzureStorageAccountsSlot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppAzureStorageAccountsSlot':
        """
        Get an existing WebAppAzureStorageAccountsSlot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppAzureStorageAccountsSlotArgs.__new__(WebAppAzureStorageAccountsSlotArgs)

        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return WebAppAzureStorageAccountsSlot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Mapping[str, 'outputs.AzureStorageInfoValueResponse']]:
        """
        Azure storage accounts.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

