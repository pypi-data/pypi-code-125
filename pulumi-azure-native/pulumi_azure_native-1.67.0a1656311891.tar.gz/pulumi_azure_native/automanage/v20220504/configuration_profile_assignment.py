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

__all__ = ['ConfigurationProfileAssignmentArgs', 'ConfigurationProfileAssignment']

@pulumi.input_type
class ConfigurationProfileAssignmentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 vm_name: pulumi.Input[str],
                 configuration_profile_assignment_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ConfigurationProfileAssignmentPropertiesArgs']] = None):
        """
        The set of arguments for constructing a ConfigurationProfileAssignment resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] vm_name: The name of the virtual machine.
        :param pulumi.Input[str] configuration_profile_assignment_name: Name of the configuration profile assignment. Only default is supported.
        :param pulumi.Input['ConfigurationProfileAssignmentPropertiesArgs'] properties: Properties of the configuration profile assignment.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vm_name", vm_name)
        if configuration_profile_assignment_name is not None:
            pulumi.set(__self__, "configuration_profile_assignment_name", configuration_profile_assignment_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter(name="configurationProfileAssignmentName")
    def configuration_profile_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the configuration profile assignment. Only default is supported.
        """
        return pulumi.get(self, "configuration_profile_assignment_name")

    @configuration_profile_assignment_name.setter
    def configuration_profile_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_profile_assignment_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ConfigurationProfileAssignmentPropertiesArgs']]:
        """
        Properties of the configuration profile assignment.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ConfigurationProfileAssignmentPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class ConfigurationProfileAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_profile_assignment_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ConfigurationProfileAssignmentPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 vm_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Configuration profile assignment is an association between a VM and automanage profile configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_profile_assignment_name: Name of the configuration profile assignment. Only default is supported.
        :param pulumi.Input[pulumi.InputType['ConfigurationProfileAssignmentPropertiesArgs']] properties: Properties of the configuration profile assignment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] vm_name: The name of the virtual machine.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationProfileAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configuration profile assignment is an association between a VM and automanage profile configuration.

        :param str resource_name: The name of the resource.
        :param ConfigurationProfileAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationProfileAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_profile_assignment_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ConfigurationProfileAssignmentPropertiesArgs']]] = None,
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
            __props__ = ConfigurationProfileAssignmentArgs.__new__(ConfigurationProfileAssignmentArgs)

            __props__.__dict__["configuration_profile_assignment_name"] = configuration_profile_assignment_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if vm_name is None and not opts.urn:
                raise TypeError("Missing required property 'vm_name'")
            __props__.__dict__["vm_name"] = vm_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automanage:ConfigurationProfileAssignment"), pulumi.Alias(type_="azure-native:automanage/v20200630preview:ConfigurationProfileAssignment"), pulumi.Alias(type_="azure-native:automanage/v20210430preview:ConfigurationProfileAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConfigurationProfileAssignment, __self__).__init__(
            'azure-native:automanage/v20220504:ConfigurationProfileAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigurationProfileAssignment':
        """
        Get an existing ConfigurationProfileAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationProfileAssignmentArgs.__new__(ConfigurationProfileAssignmentArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ConfigurationProfileAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ConfigurationProfileAssignmentPropertiesResponse']:
        """
        Properties of the configuration profile assignment.
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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

