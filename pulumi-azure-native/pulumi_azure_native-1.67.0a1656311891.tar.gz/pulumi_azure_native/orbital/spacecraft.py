# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['SpacecraftArgs', 'Spacecraft']

@pulumi.input_type
class SpacecraftArgs:
    def __init__(__self__, *,
                 norad_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 links: Optional[pulumi.Input[Sequence[pulumi.Input['SpacecraftLinkArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 spacecraft_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 title_line: Optional[pulumi.Input[str]] = None,
                 tle_line1: Optional[pulumi.Input[str]] = None,
                 tle_line2: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Spacecraft resource.
        :param pulumi.Input[str] norad_id: NORAD ID of the spacecraft.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['SpacecraftLinkArgs']]] links: Links of the Spacecraft
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] spacecraft_name: Spacecraft ID
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] title_line: Title line of Two Line Element (TLE).
        :param pulumi.Input[str] tle_line1: Line 1 of Two Line Element (TLE).
        :param pulumi.Input[str] tle_line2: Line 2 of Two Line Element (TLE).
        """
        pulumi.set(__self__, "norad_id", norad_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if links is not None:
            pulumi.set(__self__, "links", links)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if spacecraft_name is not None:
            pulumi.set(__self__, "spacecraft_name", spacecraft_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if title_line is not None:
            pulumi.set(__self__, "title_line", title_line)
        if tle_line1 is not None:
            pulumi.set(__self__, "tle_line1", tle_line1)
        if tle_line2 is not None:
            pulumi.set(__self__, "tle_line2", tle_line2)

    @property
    @pulumi.getter(name="noradId")
    def norad_id(self) -> pulumi.Input[str]:
        """
        NORAD ID of the spacecraft.
        """
        return pulumi.get(self, "norad_id")

    @norad_id.setter
    def norad_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "norad_id", value)

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
    @pulumi.getter
    def links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SpacecraftLinkArgs']]]]:
        """
        Links of the Spacecraft
        """
        return pulumi.get(self, "links")

    @links.setter
    def links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SpacecraftLinkArgs']]]]):
        pulumi.set(self, "links", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="spacecraftName")
    def spacecraft_name(self) -> Optional[pulumi.Input[str]]:
        """
        Spacecraft ID
        """
        return pulumi.get(self, "spacecraft_name")

    @spacecraft_name.setter
    def spacecraft_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spacecraft_name", value)

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
    @pulumi.getter(name="titleLine")
    def title_line(self) -> Optional[pulumi.Input[str]]:
        """
        Title line of Two Line Element (TLE).
        """
        return pulumi.get(self, "title_line")

    @title_line.setter
    def title_line(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title_line", value)

    @property
    @pulumi.getter(name="tleLine1")
    def tle_line1(self) -> Optional[pulumi.Input[str]]:
        """
        Line 1 of Two Line Element (TLE).
        """
        return pulumi.get(self, "tle_line1")

    @tle_line1.setter
    def tle_line1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tle_line1", value)

    @property
    @pulumi.getter(name="tleLine2")
    def tle_line2(self) -> Optional[pulumi.Input[str]]:
        """
        Line 2 of Two Line Element (TLE).
        """
        return pulumi.get(self, "tle_line2")

    @tle_line2.setter
    def tle_line2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tle_line2", value)


class Spacecraft(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpacecraftLinkArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 norad_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 spacecraft_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 title_line: Optional[pulumi.Input[str]] = None,
                 tle_line1: Optional[pulumi.Input[str]] = None,
                 tle_line2: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Customer creates a spacecraft resource to schedule a contact.
        API Version: 2021-04-04-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpacecraftLinkArgs']]]] links: Links of the Spacecraft
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] norad_id: NORAD ID of the spacecraft.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] spacecraft_name: Spacecraft ID
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] title_line: Title line of Two Line Element (TLE).
        :param pulumi.Input[str] tle_line1: Line 1 of Two Line Element (TLE).
        :param pulumi.Input[str] tle_line2: Line 2 of Two Line Element (TLE).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpacecraftArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Customer creates a spacecraft resource to schedule a contact.
        API Version: 2021-04-04-preview.

        :param str resource_name: The name of the resource.
        :param SpacecraftArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpacecraftArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 links: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SpacecraftLinkArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 norad_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 spacecraft_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 title_line: Optional[pulumi.Input[str]] = None,
                 tle_line1: Optional[pulumi.Input[str]] = None,
                 tle_line2: Optional[pulumi.Input[str]] = None,
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
            __props__ = SpacecraftArgs.__new__(SpacecraftArgs)

            __props__.__dict__["links"] = links
            __props__.__dict__["location"] = location
            if norad_id is None and not opts.urn:
                raise TypeError("Missing required property 'norad_id'")
            __props__.__dict__["norad_id"] = norad_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["spacecraft_name"] = spacecraft_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["title_line"] = title_line
            __props__.__dict__["tle_line1"] = tle_line1
            __props__.__dict__["tle_line2"] = tle_line2
            __props__.__dict__["authorization_status"] = None
            __props__.__dict__["authorization_status_extended"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:orbital/v20210404preview:Spacecraft"), pulumi.Alias(type_="azure-native:orbital/v20220301:Spacecraft")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Spacecraft, __self__).__init__(
            'azure-native:orbital:Spacecraft',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Spacecraft':
        """
        Get an existing Spacecraft resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SpacecraftArgs.__new__(SpacecraftArgs)

        __props__.__dict__["authorization_status"] = None
        __props__.__dict__["authorization_status_extended"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["links"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["norad_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title_line"] = None
        __props__.__dict__["tle_line1"] = None
        __props__.__dict__["tle_line2"] = None
        __props__.__dict__["type"] = None
        return Spacecraft(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationStatus")
    def authorization_status(self) -> pulumi.Output[str]:
        """
        Authorization status of spacecraft.
        """
        return pulumi.get(self, "authorization_status")

    @property
    @pulumi.getter(name="authorizationStatusExtended")
    def authorization_status_extended(self) -> pulumi.Output[str]:
        """
        Details of the authorization status.
        """
        return pulumi.get(self, "authorization_status_extended")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def links(self) -> pulumi.Output[Optional[Sequence['outputs.SpacecraftLinkResponse']]]:
        """
        Links of the Spacecraft
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noradId")
    def norad_id(self) -> pulumi.Output[str]:
        """
        NORAD ID of the spacecraft.
        """
        return pulumi.get(self, "norad_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="titleLine")
    def title_line(self) -> pulumi.Output[Optional[str]]:
        """
        Title line of Two Line Element (TLE).
        """
        return pulumi.get(self, "title_line")

    @property
    @pulumi.getter(name="tleLine1")
    def tle_line1(self) -> pulumi.Output[Optional[str]]:
        """
        Line 1 of Two Line Element (TLE).
        """
        return pulumi.get(self, "tle_line1")

    @property
    @pulumi.getter(name="tleLine2")
    def tle_line2(self) -> pulumi.Output[Optional[str]]:
        """
        Line 2 of Two Line Element (TLE).
        """
        return pulumi.get(self, "tle_line2")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

