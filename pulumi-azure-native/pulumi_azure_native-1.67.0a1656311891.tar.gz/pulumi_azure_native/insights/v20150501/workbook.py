# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['WorkbookArgs', 'Workbook']

@pulumi.input_type
class WorkbookArgs:
    def __init__(__self__, *,
                 category: pulumi.Input[str],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 serialized_data: pulumi.Input[str],
                 shared_type_kind: pulumi.Input[Union[str, 'SharedTypeKind']],
                 user_id: pulumi.Input[str],
                 workbook_id: pulumi.Input[str],
                 kind: Optional[pulumi.Input[Union[str, 'SharedTypeKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workbook resource.
        :param pulumi.Input[str] category: Workbook category, as defined by the user at creation time.
        :param pulumi.Input[str] name: The user-defined name of the workbook.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serialized_data: Configuration of this particular workbook. Configuration data is a string containing valid JSON
        :param pulumi.Input[Union[str, 'SharedTypeKind']] shared_type_kind: Enum indicating if this workbook definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        :param pulumi.Input[str] user_id: Unique user id of the specific user that owns this workbook.
        :param pulumi.Input[str] workbook_id: Internally assigned unique id of the workbook definition.
        :param pulumi.Input[Union[str, 'SharedTypeKind']] kind: The kind of workbook. Choices are user and shared.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_name: The name of the Application Insights component resource.
        :param pulumi.Input[str] source_resource_id: Optional resourceId for a source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] version: This instance's version of the data model. This can change as new features are added that can be marked workbook.
        """
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "serialized_data", serialized_data)
        if shared_type_kind is None:
            shared_type_kind = 'shared'
        pulumi.set(__self__, "shared_type_kind", shared_type_kind)
        pulumi.set(__self__, "user_id", user_id)
        pulumi.set(__self__, "workbook_id", workbook_id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Input[str]:
        """
        Workbook category, as defined by the user at creation time.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: pulumi.Input[str]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The user-defined name of the workbook.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serializedData")
    def serialized_data(self) -> pulumi.Input[str]:
        """
        Configuration of this particular workbook. Configuration data is a string containing valid JSON
        """
        return pulumi.get(self, "serialized_data")

    @serialized_data.setter
    def serialized_data(self, value: pulumi.Input[str]):
        pulumi.set(self, "serialized_data", value)

    @property
    @pulumi.getter(name="sharedTypeKind")
    def shared_type_kind(self) -> pulumi.Input[Union[str, 'SharedTypeKind']]:
        """
        Enum indicating if this workbook definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        """
        return pulumi.get(self, "shared_type_kind")

    @shared_type_kind.setter
    def shared_type_kind(self, value: pulumi.Input[Union[str, 'SharedTypeKind']]):
        pulumi.set(self, "shared_type_kind", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        Unique user id of the specific user that owns this workbook.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="workbookId")
    def workbook_id(self) -> pulumi.Input[str]:
        """
        Internally assigned unique id of the workbook definition.
        """
        return pulumi.get(self, "workbook_id")

    @workbook_id.setter
    def workbook_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workbook_id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'SharedTypeKind']]]:
        """
        The kind of workbook. Choices are user and shared.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'SharedTypeKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Application Insights component resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Optional resourceId for a source resource.
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        This instance's version of the data model. This can change as new features are added that can be marked workbook.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Workbook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'SharedTypeKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 serialized_data: Optional[pulumi.Input[str]] = None,
                 shared_type_kind: Optional[pulumi.Input[Union[str, 'SharedTypeKind']]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workbook_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Application Insights workbook definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: Workbook category, as defined by the user at creation time.
        :param pulumi.Input[Union[str, 'SharedTypeKind']] kind: The kind of workbook. Choices are user and shared.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: The user-defined name of the workbook.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the Application Insights component resource.
        :param pulumi.Input[str] serialized_data: Configuration of this particular workbook. Configuration data is a string containing valid JSON
        :param pulumi.Input[Union[str, 'SharedTypeKind']] shared_type_kind: Enum indicating if this workbook definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        :param pulumi.Input[str] source_resource_id: Optional resourceId for a source resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] user_id: Unique user id of the specific user that owns this workbook.
        :param pulumi.Input[str] version: This instance's version of the data model. This can change as new features are added that can be marked workbook.
        :param pulumi.Input[str] workbook_id: Internally assigned unique id of the workbook definition.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkbookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Application Insights workbook definition.

        :param str resource_name: The name of the resource.
        :param WorkbookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkbookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'SharedTypeKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 serialized_data: Optional[pulumi.Input[str]] = None,
                 shared_type_kind: Optional[pulumi.Input[Union[str, 'SharedTypeKind']]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workbook_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkbookArgs.__new__(WorkbookArgs)

            if category is None and not opts.urn:
                raise TypeError("Missing required property 'category'")
            __props__.__dict__["category"] = category
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            if serialized_data is None and not opts.urn:
                raise TypeError("Missing required property 'serialized_data'")
            __props__.__dict__["serialized_data"] = serialized_data
            if shared_type_kind is None:
                shared_type_kind = 'shared'
            if shared_type_kind is None and not opts.urn:
                raise TypeError("Missing required property 'shared_type_kind'")
            __props__.__dict__["shared_type_kind"] = shared_type_kind
            __props__.__dict__["source_resource_id"] = source_resource_id
            __props__.__dict__["tags"] = tags
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["version"] = version
            if workbook_id is None and not opts.urn:
                raise TypeError("Missing required property 'workbook_id'")
            __props__.__dict__["workbook_id"] = workbook_id
            __props__.__dict__["time_modified"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:Workbook"), pulumi.Alias(type_="azure-native:insights/v20180617preview:Workbook"), pulumi.Alias(type_="azure-native:insights/v20201020:Workbook"), pulumi.Alias(type_="azure-native:insights/v20210308:Workbook"), pulumi.Alias(type_="azure-native:insights/v20210801:Workbook"), pulumi.Alias(type_="azure-native:insights/v20220401:Workbook")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workbook, __self__).__init__(
            'azure-native:insights/v20150501:Workbook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workbook':
        """
        Get an existing Workbook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkbookArgs.__new__(WorkbookArgs)

        __props__.__dict__["category"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["serialized_data"] = None
        __props__.__dict__["shared_type_kind"] = None
        __props__.__dict__["source_resource_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_modified"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_id"] = None
        __props__.__dict__["version"] = None
        __props__.__dict__["workbook_id"] = None
        return Workbook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        Workbook category, as defined by the user at creation time.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of workbook. Choices are user and shared.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serializedData")
    def serialized_data(self) -> pulumi.Output[str]:
        """
        Configuration of this particular workbook. Configuration data is a string containing valid JSON
        """
        return pulumi.get(self, "serialized_data")

    @property
    @pulumi.getter(name="sharedTypeKind")
    def shared_type_kind(self) -> pulumi.Output[str]:
        """
        Enum indicating if this workbook definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        """
        return pulumi.get(self, "shared_type_kind")

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Optional resourceId for a source resource.
        """
        return pulumi.get(self, "source_resource_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> pulumi.Output[str]:
        """
        Date and time in UTC of the last modification that was made to this workbook definition.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        Unique user id of the specific user that owns this workbook.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        This instance's version of the data model. This can change as new features are added that can be marked workbook.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="workbookId")
    def workbook_id(self) -> pulumi.Output[str]:
        """
        Internally assigned unique id of the workbook definition.
        """
        return pulumi.get(self, "workbook_id")

