# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ManagedInstanceAdministratorArgs', 'ManagedInstanceAdministrator']

@pulumi.input_type
class ManagedInstanceAdministratorArgs:
    def __init__(__self__, *,
                 administrator_type: pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']],
                 login: pulumi.Input[str],
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sid: pulumi.Input[str],
                 administrator_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedInstanceAdministrator resource.
        :param pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']] administrator_type: Type of the managed instance administrator.
        :param pulumi.Input[str] login: Login name of the managed instance administrator.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] sid: SID (object ID) of the managed instance administrator.
        :param pulumi.Input[str] tenant_id: Tenant ID of the managed instance administrator.
        """
        pulumi.set(__self__, "administrator_type", administrator_type)
        pulumi.set(__self__, "login", login)
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sid", sid)
        if administrator_name is not None:
            pulumi.set(__self__, "administrator_name", administrator_name)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']]:
        """
        Type of the managed instance administrator.
        """
        return pulumi.get(self, "administrator_type")

    @administrator_type.setter
    def administrator_type(self, value: pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']]):
        pulumi.set(self, "administrator_type", value)

    @property
    @pulumi.getter
    def login(self) -> pulumi.Input[str]:
        """
        Login name of the managed instance administrator.
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: pulumi.Input[str]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sid(self) -> pulumi.Input[str]:
        """
        SID (object ID) of the managed instance administrator.
        """
        return pulumi.get(self, "sid")

    @sid.setter
    def sid(self, value: pulumi.Input[str]):
        pulumi.set(self, "sid", value)

    @property
    @pulumi.getter(name="administratorName")
    def administrator_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "administrator_name")

    @administrator_name.setter
    def administrator_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_name", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant ID of the managed instance administrator.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class ManagedInstanceAdministrator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_name: Optional[pulumi.Input[str]] = None,
                 administrator_type: Optional[pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure SQL managed instance administrator.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']] administrator_type: Type of the managed instance administrator.
        :param pulumi.Input[str] login: Login name of the managed instance administrator.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] sid: SID (object ID) of the managed instance administrator.
        :param pulumi.Input[str] tenant_id: Tenant ID of the managed instance administrator.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstanceAdministratorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL managed instance administrator.

        :param str resource_name: The name of the resource.
        :param ManagedInstanceAdministratorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstanceAdministratorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_name: Optional[pulumi.Input[str]] = None,
                 administrator_type: Optional[pulumi.Input[Union[str, 'ManagedInstanceAdministratorType']]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagedInstanceAdministratorArgs.__new__(ManagedInstanceAdministratorArgs)

            __props__.__dict__["administrator_name"] = administrator_name
            if administrator_type is None and not opts.urn:
                raise TypeError("Missing required property 'administrator_type'")
            __props__.__dict__["administrator_type"] = administrator_type
            if login is None and not opts.urn:
                raise TypeError("Missing required property 'login'")
            __props__.__dict__["login"] = login
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sid is None and not opts.urn:
                raise TypeError("Missing required property 'sid'")
            __props__.__dict__["sid"] = sid
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20170301preview:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ManagedInstanceAdministrator"), pulumi.Alias(type_="azure-native:sql/v20211101preview:ManagedInstanceAdministrator")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedInstanceAdministrator, __self__).__init__(
            'azure-native:sql/v20200801preview:ManagedInstanceAdministrator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedInstanceAdministrator':
        """
        Get an existing ManagedInstanceAdministrator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedInstanceAdministratorArgs.__new__(ManagedInstanceAdministratorArgs)

        __props__.__dict__["administrator_type"] = None
        __props__.__dict__["login"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sid"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return ManagedInstanceAdministrator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> pulumi.Output[str]:
        """
        Type of the managed instance administrator.
        """
        return pulumi.get(self, "administrator_type")

    @property
    @pulumi.getter
    def login(self) -> pulumi.Output[str]:
        """
        Login name of the managed instance administrator.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sid(self) -> pulumi.Output[str]:
        """
        SID (object ID) of the managed instance administrator.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        Tenant ID of the managed instance administrator.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

