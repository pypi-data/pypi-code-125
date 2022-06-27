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

__all__ = ['TagAtScopeArgs', 'TagAtScope']

@pulumi.input_type
class TagAtScopeArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['TagsArgs'],
                 scope: pulumi.Input[str]):
        """
        The set of arguments for constructing a TagAtScope resource.
        :param pulumi.Input['TagsArgs'] properties: The set of tags.
        :param pulumi.Input[str] scope: The resource scope.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "scope", scope)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['TagsArgs']:
        """
        The set of tags.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['TagsArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The resource scope.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)


class TagAtScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['TagsArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Wrapper resource for tags API requests and responses.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['TagsArgs']] properties: The set of tags.
        :param pulumi.Input[str] scope: The resource scope.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TagAtScopeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Wrapper resource for tags API requests and responses.

        :param str resource_name: The name of the resource.
        :param TagAtScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TagAtScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['TagsArgs']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
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
            __props__ = TagAtScopeArgs.__new__(TagAtScopeArgs)

            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:resources:TagAtScope"), pulumi.Alias(type_="azure-native:resources/v20191001:TagAtScope"), pulumi.Alias(type_="azure-native:resources/v20200601:TagAtScope"), pulumi.Alias(type_="azure-native:resources/v20201001:TagAtScope"), pulumi.Alias(type_="azure-native:resources/v20210101:TagAtScope"), pulumi.Alias(type_="azure-native:resources/v20210401:TagAtScope")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TagAtScope, __self__).__init__(
            'azure-native:resources/v20200801:TagAtScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TagAtScope':
        """
        Get an existing TagAtScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TagAtScopeArgs.__new__(TagAtScopeArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return TagAtScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the tags wrapper resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.TagsResponse']:
        """
        The set of tags.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the tags wrapper resource.
        """
        return pulumi.get(self, "type")

