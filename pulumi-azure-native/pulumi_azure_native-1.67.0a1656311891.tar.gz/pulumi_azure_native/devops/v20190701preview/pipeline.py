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

__all__ = ['PipelineArgs', 'Pipeline']

@pulumi.input_type
class PipelineArgs:
    def __init__(__self__, *,
                 bootstrap_configuration: pulumi.Input['BootstrapConfigurationArgs'],
                 organization: pulumi.Input['OrganizationReferenceArgs'],
                 project: pulumi.Input['ProjectReferenceArgs'],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Pipeline resource.
        :param pulumi.Input['BootstrapConfigurationArgs'] bootstrap_configuration: Configuration used to bootstrap the Pipeline.
        :param pulumi.Input['OrganizationReferenceArgs'] organization: Reference to the Azure DevOps Organization containing the Pipeline.
        :param pulumi.Input['ProjectReferenceArgs'] project: Reference to the Azure DevOps Project containing the Pipeline.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] pipeline_name: The name of the Azure Pipeline resource in ARM.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource Tags
        """
        pulumi.set(__self__, "bootstrap_configuration", bootstrap_configuration)
        pulumi.set(__self__, "organization", organization)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if pipeline_name is not None:
            pulumi.set(__self__, "pipeline_name", pipeline_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="bootstrapConfiguration")
    def bootstrap_configuration(self) -> pulumi.Input['BootstrapConfigurationArgs']:
        """
        Configuration used to bootstrap the Pipeline.
        """
        return pulumi.get(self, "bootstrap_configuration")

    @bootstrap_configuration.setter
    def bootstrap_configuration(self, value: pulumi.Input['BootstrapConfigurationArgs']):
        pulumi.set(self, "bootstrap_configuration", value)

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Input['OrganizationReferenceArgs']:
        """
        Reference to the Azure DevOps Organization containing the Pipeline.
        """
        return pulumi.get(self, "organization")

    @organization.setter
    def organization(self, value: pulumi.Input['OrganizationReferenceArgs']):
        pulumi.set(self, "organization", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input['ProjectReferenceArgs']:
        """
        Reference to the Azure DevOps Project containing the Pipeline.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input['ProjectReferenceArgs']):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

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
    @pulumi.getter(name="pipelineName")
    def pipeline_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Azure Pipeline resource in ARM.
        """
        return pulumi.get(self, "pipeline_name")

    @pipeline_name.setter
    def pipeline_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pipeline_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource Tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""Version 2019-07-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class Pipeline(pulumi.CustomResource):
    warnings.warn("""Version 2019-07-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bootstrap_configuration: Optional[pulumi.Input[pulumi.InputType['BootstrapConfigurationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[pulumi.InputType['OrganizationReferenceArgs']]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[pulumi.InputType['ProjectReferenceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Azure DevOps Pipeline used to configure Continuous Integration (CI) & Continuous Delivery (CD) for Azure resources.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BootstrapConfigurationArgs']] bootstrap_configuration: Configuration used to bootstrap the Pipeline.
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[pulumi.InputType['OrganizationReferenceArgs']] organization: Reference to the Azure DevOps Organization containing the Pipeline.
        :param pulumi.Input[str] pipeline_name: The name of the Azure Pipeline resource in ARM.
        :param pulumi.Input[pulumi.InputType['ProjectReferenceArgs']] project: Reference to the Azure DevOps Project containing the Pipeline.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource Tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PipelineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure DevOps Pipeline used to configure Continuous Integration (CI) & Continuous Delivery (CD) for Azure resources.

        :param str resource_name: The name of the resource.
        :param PipelineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PipelineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bootstrap_configuration: Optional[pulumi.Input[pulumi.InputType['BootstrapConfigurationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 organization: Optional[pulumi.Input[pulumi.InputType['OrganizationReferenceArgs']]] = None,
                 pipeline_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[pulumi.InputType['ProjectReferenceArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""Pipeline is deprecated: Version 2019-07-01-preview will be removed in v2 of the provider.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PipelineArgs.__new__(PipelineArgs)

            if bootstrap_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'bootstrap_configuration'")
            __props__.__dict__["bootstrap_configuration"] = bootstrap_configuration
            __props__.__dict__["location"] = location
            if organization is None and not opts.urn:
                raise TypeError("Missing required property 'organization'")
            __props__.__dict__["organization"] = organization
            __props__.__dict__["pipeline_name"] = pipeline_name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["pipeline_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devops:Pipeline"), pulumi.Alias(type_="azure-native:devops/v20200713preview:Pipeline")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pipeline, __self__).__init__(
            'azure-native:devops/v20190701preview:Pipeline',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pipeline':
        """
        Get an existing Pipeline resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PipelineArgs.__new__(PipelineArgs)

        __props__.__dict__["bootstrap_configuration"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization"] = None
        __props__.__dict__["pipeline_id"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Pipeline(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bootstrapConfiguration")
    def bootstrap_configuration(self) -> pulumi.Output['outputs.BootstrapConfigurationResponse']:
        """
        Configuration used to bootstrap the Pipeline.
        """
        return pulumi.get(self, "bootstrap_configuration")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def organization(self) -> pulumi.Output['outputs.OrganizationReferenceResponse']:
        """
        Reference to the Azure DevOps Organization containing the Pipeline.
        """
        return pulumi.get(self, "organization")

    @property
    @pulumi.getter(name="pipelineId")
    def pipeline_id(self) -> pulumi.Output[int]:
        """
        Unique identifier of the Azure Pipeline within the Azure DevOps Project.
        """
        return pulumi.get(self, "pipeline_id")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output['outputs.ProjectReferenceResponse']:
        """
        Reference to the Azure DevOps Project containing the Pipeline.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource Tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

