# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['OuContainerArgs', 'OuContainer']

@pulumi.input_type
class OuContainerArgs:
    def __init__(__self__, *,
                 domain_service_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 ou_container_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 spn: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OuContainer resource.
        :param pulumi.Input[str] domain_service_name: The name of the domain service.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] account_name: The account name
        :param pulumi.Input[str] ou_container_name: The name of the OuContainer.
        :param pulumi.Input[str] password: The account password
        :param pulumi.Input[str] spn: The account spn
        """
        pulumi.set(__self__, "domain_service_name", domain_service_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if ou_container_name is not None:
            pulumi.set(__self__, "ou_container_name", ou_container_name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if spn is not None:
            pulumi.set(__self__, "spn", spn)

    @property
    @pulumi.getter(name="domainServiceName")
    def domain_service_name(self) -> pulumi.Input[str]:
        """
        The name of the domain service.
        """
        return pulumi.get(self, "domain_service_name")

    @domain_service_name.setter
    def domain_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_service_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The account name
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="ouContainerName")
    def ou_container_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OuContainer.
        """
        return pulumi.get(self, "ou_container_name")

    @ou_container_name.setter
    def ou_container_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ou_container_name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The account password
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def spn(self) -> Optional[pulumi.Input[str]]:
        """
        The account spn
        """
        return pulumi.get(self, "spn")

    @spn.setter
    def spn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "spn", value)


warnings.warn("""Version 2017-06-01 will be removed in v2 of the provider.""", DeprecationWarning)


class OuContainer(pulumi.CustomResource):
    warnings.warn("""Version 2017-06-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 domain_service_name: Optional[pulumi.Input[str]] = None,
                 ou_container_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 spn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for OuContainer.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The account name
        :param pulumi.Input[str] domain_service_name: The name of the domain service.
        :param pulumi.Input[str] ou_container_name: The name of the OuContainer.
        :param pulumi.Input[str] password: The account password
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] spn: The account spn
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OuContainerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for OuContainer.

        :param str resource_name: The name of the resource.
        :param OuContainerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OuContainerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 domain_service_name: Optional[pulumi.Input[str]] = None,
                 ou_container_name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 spn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""OuContainer is deprecated: Version 2017-06-01 will be removed in v2 of the provider.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OuContainerArgs.__new__(OuContainerArgs)

            __props__.__dict__["account_name"] = account_name
            if domain_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_service_name'")
            __props__.__dict__["domain_service_name"] = domain_service_name
            __props__.__dict__["ou_container_name"] = ou_container_name
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["spn"] = spn
            __props__.__dict__["accounts"] = None
            __props__.__dict__["container_id"] = None
            __props__.__dict__["deployment_id"] = None
            __props__.__dict__["distinguished_name"] = None
            __props__.__dict__["domain_name"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["service_status"] = None
            __props__.__dict__["tags"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:aad:OuContainer"), pulumi.Alias(type_="azure-native:aad/v20200101:OuContainer"), pulumi.Alias(type_="azure-native:aad/v20210301:OuContainer"), pulumi.Alias(type_="azure-native:aad/v20210501:OuContainer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OuContainer, __self__).__init__(
            'azure-native:aad/v20170601:OuContainer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OuContainer':
        """
        Get an existing OuContainer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OuContainerArgs.__new__(OuContainerArgs)

        __props__.__dict__["accounts"] = None
        __props__.__dict__["container_id"] = None
        __props__.__dict__["deployment_id"] = None
        __props__.__dict__["distinguished_name"] = None
        __props__.__dict__["domain_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return OuContainer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accounts(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerAccountResponse']]]:
        """
        The list of container accounts
        """
        return pulumi.get(self, "accounts")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> pulumi.Output[str]:
        """
        The OuContainer name
        """
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        The Deployment id
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="distinguishedName")
    def distinguished_name(self) -> pulumi.Output[str]:
        """
        Distinguished Name of OuContainer instance
        """
        return pulumi.get(self, "distinguished_name")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name of Domain Services.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Resource etag
        """
        return pulumi.get(self, "etag")

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
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceStatus")
    def service_status(self) -> pulumi.Output[str]:
        """
        Status of OuContainer instance
        """
        return pulumi.get(self, "service_status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Azure Active Directory tenant id
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

