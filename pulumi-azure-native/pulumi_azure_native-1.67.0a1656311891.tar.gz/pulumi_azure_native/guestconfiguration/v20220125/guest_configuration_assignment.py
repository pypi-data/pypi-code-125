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

__all__ = ['GuestConfigurationAssignmentArgs', 'GuestConfigurationAssignment']

@pulumi.input_type
class GuestConfigurationAssignmentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 vm_name: pulumi.Input[str],
                 guest_configuration_assignment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['GuestConfigurationAssignmentPropertiesArgs']] = None):
        """
        The set of arguments for constructing a GuestConfigurationAssignment resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] vm_name: The name of the virtual machine.
        :param pulumi.Input[str] guest_configuration_assignment_name: Name of the guest configuration assignment.
        :param pulumi.Input[str] location: Region where the VM is located.
        :param pulumi.Input[str] name: Name of the guest configuration assignment.
        :param pulumi.Input['GuestConfigurationAssignmentPropertiesArgs'] properties: Properties of the Guest configuration assignment.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vm_name", vm_name)
        if guest_configuration_assignment_name is not None:
            pulumi.set(__self__, "guest_configuration_assignment_name", guest_configuration_assignment_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter(name="vmName")
    def vm_name(self) -> pulumi.Input[str]:
        """
        The name of the virtual machine.
        """
        return pulumi.get(self, "vm_name")

    @vm_name.setter
    def vm_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vm_name", value)

    @property
    @pulumi.getter(name="guestConfigurationAssignmentName")
    def guest_configuration_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the guest configuration assignment.
        """
        return pulumi.get(self, "guest_configuration_assignment_name")

    @guest_configuration_assignment_name.setter
    def guest_configuration_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guest_configuration_assignment_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Region where the VM is located.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the guest configuration assignment.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['GuestConfigurationAssignmentPropertiesArgs']]:
        """
        Properties of the Guest configuration assignment.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['GuestConfigurationAssignmentPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class GuestConfigurationAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 guest_configuration_assignment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['GuestConfigurationAssignmentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Guest configuration assignment is an association between a machine and guest configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] guest_configuration_assignment_name: Name of the guest configuration assignment.
        :param pulumi.Input[str] location: Region where the VM is located.
        :param pulumi.Input[str] name: Name of the guest configuration assignment.
        :param pulumi.Input[pulumi.InputType['GuestConfigurationAssignmentPropertiesArgs']] properties: Properties of the Guest configuration assignment.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] vm_name: The name of the virtual machine.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GuestConfigurationAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Guest configuration assignment is an association between a machine and guest configuration.

        :param str resource_name: The name of the resource.
        :param GuestConfigurationAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GuestConfigurationAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 guest_configuration_assignment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['GuestConfigurationAssignmentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = GuestConfigurationAssignmentArgs.__new__(GuestConfigurationAssignmentArgs)

            __props__.__dict__["guest_configuration_assignment_name"] = guest_configuration_assignment_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if vm_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_name'")
            __props__.__dict__["vm_name"] = vm_name
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:guestconfiguration:GuestConfigurationAssignment"), pulumi.Alias(type_="azure-native:guestconfiguration/v20180630preview:GuestConfigurationAssignment"), pulumi.Alias(type_="azure-native:guestconfiguration/v20181120:GuestConfigurationAssignment"), pulumi.Alias(type_="azure-native:guestconfiguration/v20200625:GuestConfigurationAssignment"), pulumi.Alias(type_="azure-native:guestconfiguration/v20210125:GuestConfigurationAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GuestConfigurationAssignment, __self__).__init__(
            'azure-native:guestconfiguration/v20220125:GuestConfigurationAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GuestConfigurationAssignment':
        """
        Get an existing GuestConfigurationAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GuestConfigurationAssignmentArgs.__new__(GuestConfigurationAssignmentArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return GuestConfigurationAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Region where the VM is located.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the guest configuration assignment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.GuestConfigurationAssignmentPropertiesResponse']:
        """
        Properties of the Guest configuration assignment.
        """
        return pulumi.get(self, "properties")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

