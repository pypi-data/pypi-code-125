# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['PolicyDefinitionAtManagementGroupArgs', 'PolicyDefinitionAtManagementGroup']

@pulumi.input_type
class PolicyDefinitionAtManagementGroupArgs:
    def __init__(__self__, *,
                 management_group_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 mode: Optional[pulumi.Input[Union[str, 'PolicyMode']]] = None,
                 parameters: Optional[Any] = None,
                 policy_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_rule: Optional[Any] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None):
        """
        The set of arguments for constructing a PolicyDefinitionAtManagementGroup resource.
        :param pulumi.Input[str] management_group_id: The ID of the management group.
        :param pulumi.Input[str] description: The policy definition description.
        :param pulumi.Input[str] display_name: The display name of the policy definition.
        :param Any metadata: The policy definition metadata.
        :param pulumi.Input[Union[str, 'PolicyMode']] mode: The policy definition mode. Possible values are NotSpecified, Indexed, and All.
        :param Any parameters: Required if a parameter is used in policy rule.
        :param pulumi.Input[str] policy_definition_name: The name of the policy definition to create.
        :param Any policy_rule: The policy rule.
        :param pulumi.Input[Union[str, 'PolicyType']] policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom.
        """
        pulumi.set(__self__, "management_group_id", management_group_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if policy_definition_name is not None:
            pulumi.set(__self__, "policy_definition_name", policy_definition_name)
        if policy_rule is not None:
            pulumi.set(__self__, "policy_rule", policy_rule)
        if policy_type is not None:
            pulumi.set(__self__, "policy_type", policy_type)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the management group.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The policy definition description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the policy definition.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The policy definition metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[str, 'PolicyMode']]]:
        """
        The policy definition mode. Possible values are NotSpecified, Indexed, and All.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[str, 'PolicyMode']]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        """
        Required if a parameter is used in policy rule.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="policyDefinitionName")
    def policy_definition_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy definition to create.
        """
        return pulumi.get(self, "policy_definition_name")

    @policy_definition_name.setter
    def policy_definition_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_definition_name", value)

    @property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> Optional[Any]:
        """
        The policy rule.
        """
        return pulumi.get(self, "policy_rule")

    @policy_rule.setter
    def policy_rule(self, value: Optional[Any]):
        pulumi.set(self, "policy_rule", value)

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> Optional[pulumi.Input[Union[str, 'PolicyType']]]:
        """
        The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom.
        """
        return pulumi.get(self, "policy_type")

    @policy_type.setter
    def policy_type(self, value: Optional[pulumi.Input[Union[str, 'PolicyType']]]):
        pulumi.set(self, "policy_type", value)


warnings.warn("""Version 2016-12-01 will be removed in v2 of the provider.""", DeprecationWarning)


class PolicyDefinitionAtManagementGroup(pulumi.CustomResource):
    warnings.warn("""Version 2016-12-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 mode: Optional[pulumi.Input[Union[str, 'PolicyMode']]] = None,
                 parameters: Optional[Any] = None,
                 policy_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_rule: Optional[Any] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None,
                 __props__=None):
        """
        The policy definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The policy definition description.
        :param pulumi.Input[str] display_name: The display name of the policy definition.
        :param pulumi.Input[str] management_group_id: The ID of the management group.
        :param Any metadata: The policy definition metadata.
        :param pulumi.Input[Union[str, 'PolicyMode']] mode: The policy definition mode. Possible values are NotSpecified, Indexed, and All.
        :param Any parameters: Required if a parameter is used in policy rule.
        :param pulumi.Input[str] policy_definition_name: The name of the policy definition to create.
        :param Any policy_rule: The policy rule.
        :param pulumi.Input[Union[str, 'PolicyType']] policy_type: The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyDefinitionAtManagementGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The policy definition.

        :param str resource_name: The name of the resource.
        :param PolicyDefinitionAtManagementGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyDefinitionAtManagementGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 mode: Optional[pulumi.Input[Union[str, 'PolicyMode']]] = None,
                 parameters: Optional[Any] = None,
                 policy_definition_name: Optional[pulumi.Input[str]] = None,
                 policy_rule: Optional[Any] = None,
                 policy_type: Optional[pulumi.Input[Union[str, 'PolicyType']]] = None,
                 __props__=None):
        pulumi.log.warn("""PolicyDefinitionAtManagementGroup is deprecated: Version 2016-12-01 will be removed in v2 of the provider.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PolicyDefinitionAtManagementGroupArgs.__new__(PolicyDefinitionAtManagementGroupArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'management_group_id'")
            __props__.__dict__["management_group_id"] = management_group_id
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["mode"] = mode
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["policy_definition_name"] = policy_definition_name
            __props__.__dict__["policy_rule"] = policy_rule
            __props__.__dict__["policy_type"] = policy_type
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20180301:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20180501:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20190101:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20190601:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20190901:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20200301:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20200901:PolicyDefinitionAtManagementGroup"), pulumi.Alias(type_="azure-native:authorization/v20210601:PolicyDefinitionAtManagementGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PolicyDefinitionAtManagementGroup, __self__).__init__(
            'azure-native:authorization/v20161201:PolicyDefinitionAtManagementGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PolicyDefinitionAtManagementGroup':
        """
        Get an existing PolicyDefinitionAtManagementGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PolicyDefinitionAtManagementGroupArgs.__new__(PolicyDefinitionAtManagementGroupArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["policy_rule"] = None
        __props__.__dict__["policy_type"] = None
        return PolicyDefinitionAtManagementGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the policy definition.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy definition metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional[str]]:
        """
        The policy definition mode. Possible values are NotSpecified, Indexed, and All.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy definition.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        Required if a parameter is used in policy rule.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="policyRule")
    def policy_rule(self) -> pulumi.Output[Optional[Any]]:
        """
        The policy rule.
        """
        return pulumi.get(self, "policy_rule")

    @property
    @pulumi.getter(name="policyType")
    def policy_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of policy definition. Possible values are NotSpecified, BuiltIn, and Custom.
        """
        return pulumi.get(self, "policy_type")

