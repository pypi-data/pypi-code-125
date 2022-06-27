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

__all__ = ['LabPlanArgs', 'LabPlan']

@pulumi.input_type
class LabPlanArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_auto_shutdown_profile: Optional[pulumi.Input['AutoShutdownProfileArgs']] = None,
                 default_connection_profile: Optional[pulumi.Input['ConnectionProfileArgs']] = None,
                 default_network_profile: Optional[pulumi.Input['LabPlanNetworkProfileArgs']] = None,
                 lab_plan_name: Optional[pulumi.Input[str]] = None,
                 linked_lms_instance: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support_info: Optional[pulumi.Input['SupportInfoArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LabPlan resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_regions: The allowed regions for the lab creator to use when creating labs using this lab plan.
        :param pulumi.Input['AutoShutdownProfileArgs'] default_auto_shutdown_profile: The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.
        :param pulumi.Input['ConnectionProfileArgs'] default_connection_profile: The default lab connection profile. This can be changed on a lab resource and only provides a default profile.
        :param pulumi.Input['LabPlanNetworkProfileArgs'] default_network_profile: The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.
        :param pulumi.Input[str] lab_plan_name: The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.
        :param pulumi.Input[str] linked_lms_instance: Base Url of the lms instance this lab plan can link lab rosters against.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] shared_gallery_id: Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.
        :param pulumi.Input['SupportInfoArgs'] support_info: Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if allowed_regions is not None:
            pulumi.set(__self__, "allowed_regions", allowed_regions)
        if default_auto_shutdown_profile is not None:
            pulumi.set(__self__, "default_auto_shutdown_profile", default_auto_shutdown_profile)
        if default_connection_profile is not None:
            pulumi.set(__self__, "default_connection_profile", default_connection_profile)
        if default_network_profile is not None:
            pulumi.set(__self__, "default_network_profile", default_network_profile)
        if lab_plan_name is not None:
            pulumi.set(__self__, "lab_plan_name", lab_plan_name)
        if linked_lms_instance is not None:
            pulumi.set(__self__, "linked_lms_instance", linked_lms_instance)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if shared_gallery_id is not None:
            pulumi.set(__self__, "shared_gallery_id", shared_gallery_id)
        if support_info is not None:
            pulumi.set(__self__, "support_info", support_info)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The allowed regions for the lab creator to use when creating labs using this lab plan.
        """
        return pulumi.get(self, "allowed_regions")

    @allowed_regions.setter
    def allowed_regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_regions", value)

    @property
    @pulumi.getter(name="defaultAutoShutdownProfile")
    def default_auto_shutdown_profile(self) -> Optional[pulumi.Input['AutoShutdownProfileArgs']]:
        """
        The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.
        """
        return pulumi.get(self, "default_auto_shutdown_profile")

    @default_auto_shutdown_profile.setter
    def default_auto_shutdown_profile(self, value: Optional[pulumi.Input['AutoShutdownProfileArgs']]):
        pulumi.set(self, "default_auto_shutdown_profile", value)

    @property
    @pulumi.getter(name="defaultConnectionProfile")
    def default_connection_profile(self) -> Optional[pulumi.Input['ConnectionProfileArgs']]:
        """
        The default lab connection profile. This can be changed on a lab resource and only provides a default profile.
        """
        return pulumi.get(self, "default_connection_profile")

    @default_connection_profile.setter
    def default_connection_profile(self, value: Optional[pulumi.Input['ConnectionProfileArgs']]):
        pulumi.set(self, "default_connection_profile", value)

    @property
    @pulumi.getter(name="defaultNetworkProfile")
    def default_network_profile(self) -> Optional[pulumi.Input['LabPlanNetworkProfileArgs']]:
        """
        The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.
        """
        return pulumi.get(self, "default_network_profile")

    @default_network_profile.setter
    def default_network_profile(self, value: Optional[pulumi.Input['LabPlanNetworkProfileArgs']]):
        pulumi.set(self, "default_network_profile", value)

    @property
    @pulumi.getter(name="labPlanName")
    def lab_plan_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.
        """
        return pulumi.get(self, "lab_plan_name")

    @lab_plan_name.setter
    def lab_plan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lab_plan_name", value)

    @property
    @pulumi.getter(name="linkedLmsInstance")
    def linked_lms_instance(self) -> Optional[pulumi.Input[str]]:
        """
        Base Url of the lms instance this lab plan can link lab rosters against.
        """
        return pulumi.get(self, "linked_lms_instance")

    @linked_lms_instance.setter
    def linked_lms_instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_lms_instance", value)

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
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.
        """
        return pulumi.get(self, "shared_gallery_id")

    @shared_gallery_id.setter
    def shared_gallery_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "shared_gallery_id", value)

    @property
    @pulumi.getter(name="supportInfo")
    def support_info(self) -> Optional[pulumi.Input['SupportInfoArgs']]:
        """
        Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.
        """
        return pulumi.get(self, "support_info")

    @support_info.setter
    def support_info(self, value: Optional[pulumi.Input['SupportInfoArgs']]):
        pulumi.set(self, "support_info", value)

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


class LabPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_auto_shutdown_profile: Optional[pulumi.Input[pulumi.InputType['AutoShutdownProfileArgs']]] = None,
                 default_connection_profile: Optional[pulumi.Input[pulumi.InputType['ConnectionProfileArgs']]] = None,
                 default_network_profile: Optional[pulumi.Input[pulumi.InputType['LabPlanNetworkProfileArgs']]] = None,
                 lab_plan_name: Optional[pulumi.Input[str]] = None,
                 linked_lms_instance: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support_info: Optional[pulumi.Input[pulumi.InputType['SupportInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Lab Plans act as a permission container for creating labs via labs.azure.com. Additionally, they can provide a set of default configurations that will apply at the time of creating a lab, but these defaults can still be overwritten.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_regions: The allowed regions for the lab creator to use when creating labs using this lab plan.
        :param pulumi.Input[pulumi.InputType['AutoShutdownProfileArgs']] default_auto_shutdown_profile: The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.
        :param pulumi.Input[pulumi.InputType['ConnectionProfileArgs']] default_connection_profile: The default lab connection profile. This can be changed on a lab resource and only provides a default profile.
        :param pulumi.Input[pulumi.InputType['LabPlanNetworkProfileArgs']] default_network_profile: The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.
        :param pulumi.Input[str] lab_plan_name: The name of the lab plan that uniquely identifies it within containing resource group. Used in resource URIs and in UI.
        :param pulumi.Input[str] linked_lms_instance: Base Url of the lms instance this lab plan can link lab rosters against.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] shared_gallery_id: Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.
        :param pulumi.Input[pulumi.InputType['SupportInfoArgs']] support_info: Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LabPlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Lab Plans act as a permission container for creating labs via labs.azure.com. Additionally, they can provide a set of default configurations that will apply at the time of creating a lab, but these defaults can still be overwritten.

        :param str resource_name: The name of the resource.
        :param LabPlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LabPlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_auto_shutdown_profile: Optional[pulumi.Input[pulumi.InputType['AutoShutdownProfileArgs']]] = None,
                 default_connection_profile: Optional[pulumi.Input[pulumi.InputType['ConnectionProfileArgs']]] = None,
                 default_network_profile: Optional[pulumi.Input[pulumi.InputType['LabPlanNetworkProfileArgs']]] = None,
                 lab_plan_name: Optional[pulumi.Input[str]] = None,
                 linked_lms_instance: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_gallery_id: Optional[pulumi.Input[str]] = None,
                 support_info: Optional[pulumi.Input[pulumi.InputType['SupportInfoArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = LabPlanArgs.__new__(LabPlanArgs)

            __props__.__dict__["allowed_regions"] = allowed_regions
            __props__.__dict__["default_auto_shutdown_profile"] = default_auto_shutdown_profile
            __props__.__dict__["default_connection_profile"] = default_connection_profile
            __props__.__dict__["default_network_profile"] = default_network_profile
            __props__.__dict__["lab_plan_name"] = lab_plan_name
            __props__.__dict__["linked_lms_instance"] = linked_lms_instance
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["shared_gallery_id"] = shared_gallery_id
            __props__.__dict__["support_info"] = support_info
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:labservices:LabPlan"), pulumi.Alias(type_="azure-native:labservices/v20211001preview:LabPlan")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LabPlan, __self__).__init__(
            'azure-native:labservices/v20211115preview:LabPlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LabPlan':
        """
        Get an existing LabPlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LabPlanArgs.__new__(LabPlanArgs)

        __props__.__dict__["allowed_regions"] = None
        __props__.__dict__["default_auto_shutdown_profile"] = None
        __props__.__dict__["default_connection_profile"] = None
        __props__.__dict__["default_network_profile"] = None
        __props__.__dict__["linked_lms_instance"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["shared_gallery_id"] = None
        __props__.__dict__["support_info"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return LabPlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedRegions")
    def allowed_regions(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The allowed regions for the lab creator to use when creating labs using this lab plan.
        """
        return pulumi.get(self, "allowed_regions")

    @property
    @pulumi.getter(name="defaultAutoShutdownProfile")
    def default_auto_shutdown_profile(self) -> pulumi.Output[Optional['outputs.AutoShutdownProfileResponse']]:
        """
        The default lab shutdown profile. This can be changed on a lab resource and only provides a default profile.
        """
        return pulumi.get(self, "default_auto_shutdown_profile")

    @property
    @pulumi.getter(name="defaultConnectionProfile")
    def default_connection_profile(self) -> pulumi.Output[Optional['outputs.ConnectionProfileResponse']]:
        """
        The default lab connection profile. This can be changed on a lab resource and only provides a default profile.
        """
        return pulumi.get(self, "default_connection_profile")

    @property
    @pulumi.getter(name="defaultNetworkProfile")
    def default_network_profile(self) -> pulumi.Output[Optional['outputs.LabPlanNetworkProfileResponse']]:
        """
        The lab plan network profile. To enforce lab network policies they must be defined here and cannot be changed when there are existing labs associated with this lab plan.
        """
        return pulumi.get(self, "default_network_profile")

    @property
    @pulumi.getter(name="linkedLmsInstance")
    def linked_lms_instance(self) -> pulumi.Output[Optional[str]]:
        """
        Base Url of the lms instance this lab plan can link lab rosters against.
        """
        return pulumi.get(self, "linked_lms_instance")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Current provisioning state of the lab plan.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sharedGalleryId")
    def shared_gallery_id(self) -> pulumi.Output[Optional[str]]:
        """
        Resource ID of the Shared Image Gallery attached to this lab plan. When saving a lab template virtual machine image it will be persisted in this gallery. Shared images from the gallery can be made available to use when creating new labs.
        """
        return pulumi.get(self, "shared_gallery_id")

    @property
    @pulumi.getter(name="supportInfo")
    def support_info(self) -> pulumi.Output[Optional['outputs.SupportInfoResponse']]:
        """
        Support contact information and instructions for users of the lab plan. This information is displayed to lab owners and virtual machine users for all labs in the lab plan.
        """
        return pulumi.get(self, "support_info")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the lab plan.
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
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

