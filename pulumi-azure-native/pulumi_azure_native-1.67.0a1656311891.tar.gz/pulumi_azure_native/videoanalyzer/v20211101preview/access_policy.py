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

__all__ = ['AccessPolicyArgs', 'AccessPolicy']

@pulumi.input_type
class AccessPolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 access_policy_name: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input['JwtAuthenticationArgs']] = None,
                 role: Optional[pulumi.Input[Union[str, 'AccessPolicyRole']]] = None):
        """
        The set of arguments for constructing a AccessPolicy resource.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] access_policy_name: The Access Policy name.
        :param pulumi.Input['JwtAuthenticationArgs'] authentication: Authentication method to be used when validating client API access.
        :param pulumi.Input[Union[str, 'AccessPolicyRole']] role: Defines the access level granted by this policy.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if access_policy_name is not None:
            pulumi.set(__self__, "access_policy_name", access_policy_name)
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if role is not None:
            pulumi.set(__self__, "role", role)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Azure Video Analyzer account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

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
    @pulumi.getter(name="accessPolicyName")
    def access_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Access Policy name.
        """
        return pulumi.get(self, "access_policy_name")

    @access_policy_name.setter
    def access_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_policy_name", value)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input['JwtAuthenticationArgs']]:
        """
        Authentication method to be used when validating client API access.
        """
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input['JwtAuthenticationArgs']]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[Union[str, 'AccessPolicyRole']]]:
        """
        Defines the access level granted by this policy.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[Union[str, 'AccessPolicyRole']]]):
        pulumi.set(self, "role", value)


class AccessPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policy_name: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['JwtAuthenticationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'AccessPolicyRole']]] = None,
                 __props__=None):
        """
        Access policies help define the authentication rules, and control access to specific video resources.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_policy_name: The Access Policy name.
        :param pulumi.Input[str] account_name: The Azure Video Analyzer account name.
        :param pulumi.Input[pulumi.InputType['JwtAuthenticationArgs']] authentication: Authentication method to be used when validating client API access.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'AccessPolicyRole']] role: Defines the access level granted by this policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Access policies help define the authentication rules, and control access to specific video resources.

        :param str resource_name: The name of the resource.
        :param AccessPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policy_name: Optional[pulumi.Input[str]] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[pulumi.InputType['JwtAuthenticationArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'AccessPolicyRole']]] = None,
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
            __props__ = AccessPolicyArgs.__new__(AccessPolicyArgs)

            __props__.__dict__["access_policy_name"] = access_policy_name
            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["authentication"] = authentication
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["role"] = role
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:videoanalyzer:AccessPolicy"), pulumi.Alias(type_="azure-native:videoanalyzer/v20210501preview:AccessPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AccessPolicy, __self__).__init__(
            'azure-native:videoanalyzer/v20211101preview:AccessPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AccessPolicy':
        """
        Get an existing AccessPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccessPolicyArgs.__new__(AccessPolicyArgs)

        __props__.__dict__["authentication"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return AccessPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional['outputs.JwtAuthenticationResponse']]:
        """
        Authentication method to be used when validating client API access.
        """
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[Optional[str]]:
        """
        Defines the access level granted by this policy.
        """
        return pulumi.get(self, "role")

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

