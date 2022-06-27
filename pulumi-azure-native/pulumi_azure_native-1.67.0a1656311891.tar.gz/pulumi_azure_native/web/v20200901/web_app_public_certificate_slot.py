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

__all__ = ['WebAppPublicCertificateSlotArgs', 'WebAppPublicCertificateSlot']

@pulumi.input_type
class WebAppPublicCertificateSlotArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 slot: pulumi.Input[str],
                 blob: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 public_certificate_location: Optional[pulumi.Input['PublicCertificateLocation']] = None,
                 public_certificate_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WebAppPublicCertificateSlot resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] slot: Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
        :param pulumi.Input[str] blob: Public Certificate byte array
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input['PublicCertificateLocation'] public_certificate_location: Public Certificate Location
        :param pulumi.Input[str] public_certificate_name: Public certificate name.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "slot", slot)
        if blob is not None:
            pulumi.set(__self__, "blob", blob)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if public_certificate_location is not None:
            pulumi.set(__self__, "public_certificate_location", public_certificate_location)
        if public_certificate_name is not None:
            pulumi.set(__self__, "public_certificate_name", public_certificate_name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the app.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def slot(self) -> pulumi.Input[str]:
        """
        Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
        """
        return pulumi.get(self, "slot")

    @slot.setter
    def slot(self, value: pulumi.Input[str]):
        pulumi.set(self, "slot", value)

    @property
    @pulumi.getter
    def blob(self) -> Optional[pulumi.Input[str]]:
        """
        Public Certificate byte array
        """
        return pulumi.get(self, "blob")

    @blob.setter
    def blob(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "blob", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="publicCertificateLocation")
    def public_certificate_location(self) -> Optional[pulumi.Input['PublicCertificateLocation']]:
        """
        Public Certificate Location
        """
        return pulumi.get(self, "public_certificate_location")

    @public_certificate_location.setter
    def public_certificate_location(self, value: Optional[pulumi.Input['PublicCertificateLocation']]):
        pulumi.set(self, "public_certificate_location", value)

    @property
    @pulumi.getter(name="publicCertificateName")
    def public_certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Public certificate name.
        """
        return pulumi.get(self, "public_certificate_name")

    @public_certificate_name.setter
    def public_certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_certificate_name", value)


class WebAppPublicCertificateSlot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blob: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_certificate_location: Optional[pulumi.Input['PublicCertificateLocation']] = None,
                 public_certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Public certificate object

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] blob: Public Certificate byte array
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the app.
        :param pulumi.Input['PublicCertificateLocation'] public_certificate_location: Public Certificate Location
        :param pulumi.Input[str] public_certificate_name: Public certificate name.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] slot: Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebAppPublicCertificateSlotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Public certificate object

        :param str resource_name: The name of the resource.
        :param WebAppPublicCertificateSlotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebAppPublicCertificateSlotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blob: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_certificate_location: Optional[pulumi.Input['PublicCertificateLocation']] = None,
                 public_certificate_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slot: Optional[pulumi.Input[str]] = None,
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
            __props__ = WebAppPublicCertificateSlotArgs.__new__(WebAppPublicCertificateSlotArgs)

            __props__.__dict__["blob"] = blob
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["public_certificate_location"] = public_certificate_location
            __props__.__dict__["public_certificate_name"] = public_certificate_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if slot is None and not opts.urn:
                raise TypeError("Missing required property 'slot'")
            __props__.__dict__["slot"] = slot
            __props__.__dict__["system_data"] = None
            __props__.__dict__["thumbprint"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20160801:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20180201:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20181101:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20190801:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20200601:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20201001:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20201201:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20210101:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20210115:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20210201:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20210301:WebAppPublicCertificateSlot"), pulumi.Alias(type_="azure-native:web/v20220301:WebAppPublicCertificateSlot")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebAppPublicCertificateSlot, __self__).__init__(
            'azure-native:web/v20200901:WebAppPublicCertificateSlot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebAppPublicCertificateSlot':
        """
        Get an existing WebAppPublicCertificateSlot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebAppPublicCertificateSlotArgs.__new__(WebAppPublicCertificateSlotArgs)

        __props__.__dict__["blob"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["public_certificate_location"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["thumbprint"] = None
        __props__.__dict__["type"] = None
        return WebAppPublicCertificateSlot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def blob(self) -> pulumi.Output[Optional[str]]:
        """
        Public Certificate byte array
        """
        return pulumi.get(self, "blob")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicCertificateLocation")
    def public_certificate_location(self) -> pulumi.Output[Optional[str]]:
        """
        Public Certificate Location
        """
        return pulumi.get(self, "public_certificate_location")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        Certificate Thumbprint
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

