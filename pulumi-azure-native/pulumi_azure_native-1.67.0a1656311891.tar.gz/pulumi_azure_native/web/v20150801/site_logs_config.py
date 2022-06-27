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

__all__ = ['SiteLogsConfigArgs', 'SiteLogsConfig']

@pulumi.input_type
class SiteLogsConfigArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 application_logs: Optional[pulumi.Input['ApplicationLogsConfigArgs']] = None,
                 detailed_error_messages: Optional[pulumi.Input['EnabledConfigArgs']] = None,
                 failed_requests_tracing: Optional[pulumi.Input['EnabledConfigArgs']] = None,
                 http_logs: Optional[pulumi.Input['HttpLogsConfigArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SiteLogsConfig resource.
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input['ApplicationLogsConfigArgs'] application_logs: Application logs configuration
        :param pulumi.Input['EnabledConfigArgs'] detailed_error_messages: Detailed error messages configuration
        :param pulumi.Input['EnabledConfigArgs'] failed_requests_tracing: Failed requests tracing configuration
        :param pulumi.Input['HttpLogsConfigArgs'] http_logs: Http logs configuration
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_logs is not None:
            pulumi.set(__self__, "application_logs", application_logs)
        if detailed_error_messages is not None:
            pulumi.set(__self__, "detailed_error_messages", detailed_error_messages)
        if failed_requests_tracing is not None:
            pulumi.set(__self__, "failed_requests_tracing", failed_requests_tracing)
        if http_logs is not None:
            pulumi.set(__self__, "http_logs", http_logs)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="applicationLogs")
    def application_logs(self) -> Optional[pulumi.Input['ApplicationLogsConfigArgs']]:
        """
        Application logs configuration
        """
        return pulumi.get(self, "application_logs")

    @application_logs.setter
    def application_logs(self, value: Optional[pulumi.Input['ApplicationLogsConfigArgs']]):
        pulumi.set(self, "application_logs", value)

    @property
    @pulumi.getter(name="detailedErrorMessages")
    def detailed_error_messages(self) -> Optional[pulumi.Input['EnabledConfigArgs']]:
        """
        Detailed error messages configuration
        """
        return pulumi.get(self, "detailed_error_messages")

    @detailed_error_messages.setter
    def detailed_error_messages(self, value: Optional[pulumi.Input['EnabledConfigArgs']]):
        pulumi.set(self, "detailed_error_messages", value)

    @property
    @pulumi.getter(name="failedRequestsTracing")
    def failed_requests_tracing(self) -> Optional[pulumi.Input['EnabledConfigArgs']]:
        """
        Failed requests tracing configuration
        """
        return pulumi.get(self, "failed_requests_tracing")

    @failed_requests_tracing.setter
    def failed_requests_tracing(self, value: Optional[pulumi.Input['EnabledConfigArgs']]):
        pulumi.set(self, "failed_requests_tracing", value)

    @property
    @pulumi.getter(name="httpLogs")
    def http_logs(self) -> Optional[pulumi.Input['HttpLogsConfigArgs']]:
        """
        Http logs configuration
        """
        return pulumi.get(self, "http_logs")

    @http_logs.setter
    def http_logs(self, value: Optional[pulumi.Input['HttpLogsConfigArgs']]):
        pulumi.set(self, "http_logs", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class SiteLogsConfig(pulumi.CustomResource):
    warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_logs: Optional[pulumi.Input[pulumi.InputType['ApplicationLogsConfigArgs']]] = None,
                 detailed_error_messages: Optional[pulumi.Input[pulumi.InputType['EnabledConfigArgs']]] = None,
                 failed_requests_tracing: Optional[pulumi.Input[pulumi.InputType['EnabledConfigArgs']]] = None,
                 http_logs: Optional[pulumi.Input[pulumi.InputType['HttpLogsConfigArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Configuration of Azure web site

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ApplicationLogsConfigArgs']] application_logs: Application logs configuration
        :param pulumi.Input[pulumi.InputType['EnabledConfigArgs']] detailed_error_messages: Detailed error messages configuration
        :param pulumi.Input[pulumi.InputType['EnabledConfigArgs']] failed_requests_tracing: Failed requests tracing configuration
        :param pulumi.Input[pulumi.InputType['HttpLogsConfigArgs']] http_logs: Http logs configuration
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SiteLogsConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configuration of Azure web site

        :param str resource_name: The name of the resource.
        :param SiteLogsConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SiteLogsConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_logs: Optional[pulumi.Input[pulumi.InputType['ApplicationLogsConfigArgs']]] = None,
                 detailed_error_messages: Optional[pulumi.Input[pulumi.InputType['EnabledConfigArgs']]] = None,
                 failed_requests_tracing: Optional[pulumi.Input[pulumi.InputType['EnabledConfigArgs']]] = None,
                 http_logs: Optional[pulumi.Input[pulumi.InputType['HttpLogsConfigArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SiteLogsConfig is deprecated: Version 2015-08-01 will be removed in v2 of the provider.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SiteLogsConfigArgs.__new__(SiteLogsConfigArgs)

            __props__.__dict__["application_logs"] = application_logs
            __props__.__dict__["detailed_error_messages"] = detailed_error_messages
            __props__.__dict__["failed_requests_tracing"] = failed_requests_tracing
            __props__.__dict__["http_logs"] = http_logs
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20160801:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20180201:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20181101:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20190801:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20200601:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20200901:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20201001:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20201201:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20210101:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20210115:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20210201:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20210301:SiteLogsConfig"), pulumi.Alias(type_="azure-native:web/v20220301:SiteLogsConfig")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SiteLogsConfig, __self__).__init__(
            'azure-native:web/v20150801:SiteLogsConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SiteLogsConfig':
        """
        Get an existing SiteLogsConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SiteLogsConfigArgs.__new__(SiteLogsConfigArgs)

        __props__.__dict__["application_logs"] = None
        __props__.__dict__["detailed_error_messages"] = None
        __props__.__dict__["failed_requests_tracing"] = None
        __props__.__dict__["http_logs"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SiteLogsConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationLogs")
    def application_logs(self) -> pulumi.Output[Optional['outputs.ApplicationLogsConfigResponse']]:
        """
        Application logs configuration
        """
        return pulumi.get(self, "application_logs")

    @property
    @pulumi.getter(name="detailedErrorMessages")
    def detailed_error_messages(self) -> pulumi.Output[Optional['outputs.EnabledConfigResponse']]:
        """
        Detailed error messages configuration
        """
        return pulumi.get(self, "detailed_error_messages")

    @property
    @pulumi.getter(name="failedRequestsTracing")
    def failed_requests_tracing(self) -> pulumi.Output[Optional['outputs.EnabledConfigResponse']]:
        """
        Failed requests tracing configuration
        """
        return pulumi.get(self, "failed_requests_tracing")

    @property
    @pulumi.getter(name="httpLogs")
    def http_logs(self) -> pulumi.Output[Optional['outputs.HttpLogsConfigResponse']]:
        """
        Http logs configuration
        """
        return pulumi.get(self, "http_logs")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

