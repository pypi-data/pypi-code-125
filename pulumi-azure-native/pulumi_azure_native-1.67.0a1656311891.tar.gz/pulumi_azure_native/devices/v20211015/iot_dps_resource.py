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

__all__ = ['IotDpsResourceArgs', 'IotDpsResource']

@pulumi.input_type
class IotDpsResourceArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['IotDpsPropertiesDescriptionArgs'],
                 resource_group_name: pulumi.Input[str],
                 sku: pulumi.Input['IotDpsSkuInfoArgs'],
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_service_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a IotDpsResource resource.
        :param pulumi.Input['IotDpsPropertiesDescriptionArgs'] properties: Service specific properties for a provisioning service
        :param pulumi.Input[str] resource_group_name: Resource group identifier.
        :param pulumi.Input['IotDpsSkuInfoArgs'] sku: Sku info for a provisioning Service.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] provisioning_service_name: Name of provisioning service to create or update.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sku", sku)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_service_name is not None:
            pulumi.set(__self__, "provisioning_service_name", provisioning_service_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['IotDpsPropertiesDescriptionArgs']:
        """
        Service specific properties for a provisioning service
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['IotDpsPropertiesDescriptionArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Resource group identifier.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['IotDpsSkuInfoArgs']:
        """
        Sku info for a provisioning Service.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['IotDpsSkuInfoArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="provisioningServiceName")
    def provisioning_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of provisioning service to create or update.
        """
        return pulumi.get(self, "provisioning_service_name")

    @provisioning_service_name.setter
    def provisioning_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_service_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class IotDpsResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['IotDpsPropertiesDescriptionArgs']]] = None,
                 provisioning_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['IotDpsSkuInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The description of the provisioning service.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[pulumi.InputType['IotDpsPropertiesDescriptionArgs']] properties: Service specific properties for a provisioning service
        :param pulumi.Input[str] provisioning_service_name: Name of provisioning service to create or update.
        :param pulumi.Input[str] resource_group_name: Resource group identifier.
        :param pulumi.Input[pulumi.InputType['IotDpsSkuInfoArgs']] sku: Sku info for a provisioning Service.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IotDpsResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The description of the provisioning service.

        :param str resource_name: The name of the resource.
        :param IotDpsResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IotDpsResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['IotDpsPropertiesDescriptionArgs']]] = None,
                 provisioning_service_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['IotDpsSkuInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = IotDpsResourceArgs.__new__(IotDpsResourceArgs)

            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            __props__.__dict__["provisioning_service_name"] = provisioning_service_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devices:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20170821preview:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20171115:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20180122:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20200101:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20200301:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20200901preview:IotDpsResource"), pulumi.Alias(type_="azure-native:devices/v20220205:IotDpsResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IotDpsResource, __self__).__init__(
            'azure-native:devices/v20211015:IotDpsResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IotDpsResource':
        """
        Get an existing IotDpsResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IotDpsResourceArgs.__new__(IotDpsResourceArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return IotDpsResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.IotDpsPropertiesDescriptionResponse']:
        """
        Service specific properties for a provisioning service
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output['outputs.IotDpsSkuInfoResponse']:
        """
        Sku info for a provisioning Service.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

