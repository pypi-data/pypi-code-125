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

__all__ = ['SecurityUserConfigurationArgs', 'SecurityUserConfiguration']

@pulumi.input_type
class SecurityUserConfigurationArgs:
    def __init__(__self__, *,
                 network_manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 delete_existing_nsgs: Optional[pulumi.Input[Union[str, 'DeleteExistingNSGs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 security_type: Optional[pulumi.Input[Union[str, 'SecurityType']]] = None):
        """
        The set of arguments for constructing a SecurityUserConfiguration resource.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] configuration_name: The name of the network manager security Configuration.
        :param pulumi.Input[Union[str, 'DeleteExistingNSGs']] delete_existing_nsgs: Flag if need to delete existing network security groups.
        :param pulumi.Input[str] description: A description of the security configuration.
        :param pulumi.Input[str] display_name: A display name of the security configuration.
        :param pulumi.Input[Union[str, 'SecurityType']] security_type: Security Type.
        """
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if delete_existing_nsgs is not None:
            pulumi.set(__self__, "delete_existing_nsgs", delete_existing_nsgs)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if security_type is not None:
            pulumi.set(__self__, "security_type", security_type)

    @property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager.
        """
        return pulumi.get(self, "network_manager_name")

    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_manager_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network manager security Configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="deleteExistingNSGs")
    def delete_existing_nsgs(self) -> Optional[pulumi.Input[Union[str, 'DeleteExistingNSGs']]]:
        """
        Flag if need to delete existing network security groups.
        """
        return pulumi.get(self, "delete_existing_nsgs")

    @delete_existing_nsgs.setter
    def delete_existing_nsgs(self, value: Optional[pulumi.Input[Union[str, 'DeleteExistingNSGs']]]):
        pulumi.set(self, "delete_existing_nsgs", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the security configuration.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        A display name of the security configuration.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="securityType")
    def security_type(self) -> Optional[pulumi.Input[Union[str, 'SecurityType']]]:
        """
        Security Type.
        """
        return pulumi.get(self, "security_type")

    @security_type.setter
    def security_type(self, value: Optional[pulumi.Input[Union[str, 'SecurityType']]]):
        pulumi.set(self, "security_type", value)


class SecurityUserConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 delete_existing_nsgs: Optional[pulumi.Input[Union[str, 'DeleteExistingNSGs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_type: Optional[pulumi.Input[Union[str, 'SecurityType']]] = None,
                 __props__=None):
        """
        Defines the security configuration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_name: The name of the network manager security Configuration.
        :param pulumi.Input[Union[str, 'DeleteExistingNSGs']] delete_existing_nsgs: Flag if need to delete existing network security groups.
        :param pulumi.Input[str] description: A description of the security configuration.
        :param pulumi.Input[str] display_name: A display name of the security configuration.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'SecurityType']] security_type: Security Type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityUserConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the security configuration

        :param str resource_name: The name of the resource.
        :param SecurityUserConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityUserConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 delete_existing_nsgs: Optional[pulumi.Input[Union[str, 'DeleteExistingNSGs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_type: Optional[pulumi.Input[Union[str, 'SecurityType']]] = None,
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
            __props__ = SecurityUserConfigurationArgs.__new__(SecurityUserConfigurationArgs)

            __props__.__dict__["configuration_name"] = configuration_name
            __props__.__dict__["delete_existing_nsgs"] = delete_existing_nsgs
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["security_type"] = security_type
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:SecurityUserConfiguration"), pulumi.Alias(type_="azure-native:network/v20210501preview:SecurityUserConfiguration"), pulumi.Alias(type_="azure-native:network/v20220201preview:SecurityUserConfiguration"), pulumi.Alias(type_="azure-native:network/v20220401preview:SecurityUserConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SecurityUserConfiguration, __self__).__init__(
            'azure-native:network/v20210201preview:SecurityUserConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SecurityUserConfiguration':
        """
        Get an existing SecurityUserConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SecurityUserConfigurationArgs.__new__(SecurityUserConfigurationArgs)

        __props__.__dict__["delete_existing_nsgs"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["security_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SecurityUserConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deleteExistingNSGs")
    def delete_existing_nsgs(self) -> pulumi.Output[Optional[str]]:
        """
        Flag if need to delete existing network security groups.
        """
        return pulumi.get(self, "delete_existing_nsgs")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the security configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        A display name of the security configuration.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityType")
    def security_type(self) -> pulumi.Output[Optional[str]]:
        """
        Security Type.
        """
        return pulumi.get(self, "security_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

