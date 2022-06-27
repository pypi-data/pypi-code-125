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

__all__ = ['RelationshipLinkArgs', 'RelationshipLink']

@pulumi.input_type
class RelationshipLinkArgs:
    def __init__(__self__, *,
                 hub_name: pulumi.Input[str],
                 interaction_type: pulumi.Input[str],
                 profile_property_references: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]],
                 related_profile_property_references: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]],
                 relationship_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input['RelationshipLinkFieldMappingArgs']]]] = None,
                 relationship_link_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RelationshipLink resource.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[str] interaction_type: The InteractionType associated with the Relationship Link.
        :param pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]] profile_property_references: The property references for the Profile of the Relationship.
        :param pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]] related_profile_property_references: The property references for the Related Profile of the Relationship.
        :param pulumi.Input[str] relationship_name: The Relationship associated with the Link.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Relationship Link.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Relationship Link.
        :param pulumi.Input[Sequence[pulumi.Input['RelationshipLinkFieldMappingArgs']]] mappings: The mappings between Interaction and Relationship fields.
        :param pulumi.Input[str] relationship_link_name: The name of the relationship link.
        """
        pulumi.set(__self__, "hub_name", hub_name)
        pulumi.set(__self__, "interaction_type", interaction_type)
        pulumi.set(__self__, "profile_property_references", profile_property_references)
        pulumi.set(__self__, "related_profile_property_references", related_profile_property_references)
        pulumi.set(__self__, "relationship_name", relationship_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if mappings is not None:
            pulumi.set(__self__, "mappings", mappings)
        if relationship_link_name is not None:
            pulumi.set(__self__, "relationship_link_name", relationship_link_name)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[str]:
        """
        The name of the hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_name", value)

    @property
    @pulumi.getter(name="interactionType")
    def interaction_type(self) -> pulumi.Input[str]:
        """
        The InteractionType associated with the Relationship Link.
        """
        return pulumi.get(self, "interaction_type")

    @interaction_type.setter
    def interaction_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "interaction_type", value)

    @property
    @pulumi.getter(name="profilePropertyReferences")
    def profile_property_references(self) -> pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]:
        """
        The property references for the Profile of the Relationship.
        """
        return pulumi.get(self, "profile_property_references")

    @profile_property_references.setter
    def profile_property_references(self, value: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]):
        pulumi.set(self, "profile_property_references", value)

    @property
    @pulumi.getter(name="relatedProfilePropertyReferences")
    def related_profile_property_references(self) -> pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]:
        """
        The property references for the Related Profile of the Relationship.
        """
        return pulumi.get(self, "related_profile_property_references")

    @related_profile_property_references.setter
    def related_profile_property_references(self, value: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]):
        pulumi.set(self, "related_profile_property_references", value)

    @property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> pulumi.Input[str]:
        """
        The Relationship associated with the Link.
        """
        return pulumi.get(self, "relationship_name")

    @relationship_name.setter
    def relationship_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "relationship_name", value)

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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized descriptions for the Relationship Link.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized display name for the Relationship Link.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RelationshipLinkFieldMappingArgs']]]]:
        """
        The mappings between Interaction and Relationship fields.
        """
        return pulumi.get(self, "mappings")

    @mappings.setter
    def mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RelationshipLinkFieldMappingArgs']]]]):
        pulumi.set(self, "mappings", value)

    @property
    @pulumi.getter(name="relationshipLinkName")
    def relationship_link_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the relationship link.
        """
        return pulumi.get(self, "relationship_link_name")

    @relationship_link_name.setter
    def relationship_link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relationship_link_name", value)


warnings.warn("""Version 2017-01-01 will be removed in v2 of the provider.""", DeprecationWarning)


class RelationshipLink(pulumi.CustomResource):
    warnings.warn("""Version 2017-01-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 interaction_type: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelationshipLinkFieldMappingArgs']]]]] = None,
                 profile_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]]] = None,
                 related_profile_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]]] = None,
                 relationship_link_name: Optional[pulumi.Input[str]] = None,
                 relationship_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The relationship link resource format.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Relationship Link.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Relationship Link.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[str] interaction_type: The InteractionType associated with the Relationship Link.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelationshipLinkFieldMappingArgs']]]] mappings: The mappings between Interaction and Relationship fields.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]] profile_property_references: The property references for the Profile of the Relationship.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]] related_profile_property_references: The property references for the Related Profile of the Relationship.
        :param pulumi.Input[str] relationship_link_name: The name of the relationship link.
        :param pulumi.Input[str] relationship_name: The Relationship associated with the Link.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RelationshipLinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The relationship link resource format.

        :param str resource_name: The name of the resource.
        :param RelationshipLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RelationshipLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 interaction_type: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RelationshipLinkFieldMappingArgs']]]]] = None,
                 profile_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]]] = None,
                 related_profile_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParticipantPropertyReferenceArgs']]]]] = None,
                 relationship_link_name: Optional[pulumi.Input[str]] = None,
                 relationship_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""RelationshipLink is deprecated: Version 2017-01-01 will be removed in v2 of the provider.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RelationshipLinkArgs.__new__(RelationshipLinkArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__.__dict__["hub_name"] = hub_name
            if interaction_type is None and not opts.urn:
                raise TypeError("Missing required property 'interaction_type'")
            __props__.__dict__["interaction_type"] = interaction_type
            __props__.__dict__["mappings"] = mappings
            if profile_property_references is None and not opts.urn:
                raise TypeError("Missing required property 'profile_property_references'")
            __props__.__dict__["profile_property_references"] = profile_property_references
            if related_profile_property_references is None and not opts.urn:
                raise TypeError("Missing required property 'related_profile_property_references'")
            __props__.__dict__["related_profile_property_references"] = related_profile_property_references
            __props__.__dict__["relationship_link_name"] = relationship_link_name
            if relationship_name is None and not opts.urn:
                raise TypeError("Missing required property 'relationship_name'")
            __props__.__dict__["relationship_name"] = relationship_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["link_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["relationship_guid_id"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customerinsights:RelationshipLink"), pulumi.Alias(type_="azure-native:customerinsights/v20170426:RelationshipLink")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RelationshipLink, __self__).__init__(
            'azure-native:customerinsights/v20170101:RelationshipLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RelationshipLink':
        """
        Get an existing RelationshipLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RelationshipLinkArgs.__new__(RelationshipLinkArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["interaction_type"] = None
        __props__.__dict__["link_name"] = None
        __props__.__dict__["mappings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["profile_property_references"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["related_profile_property_references"] = None
        __props__.__dict__["relationship_guid_id"] = None
        __props__.__dict__["relationship_name"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return RelationshipLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized descriptions for the Relationship Link.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized display name for the Relationship Link.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="interactionType")
    def interaction_type(self) -> pulumi.Output[str]:
        """
        The InteractionType associated with the Relationship Link.
        """
        return pulumi.get(self, "interaction_type")

    @property
    @pulumi.getter(name="linkName")
    def link_name(self) -> pulumi.Output[str]:
        """
        The name of the Relationship Link.
        """
        return pulumi.get(self, "link_name")

    @property
    @pulumi.getter
    def mappings(self) -> pulumi.Output[Optional[Sequence['outputs.RelationshipLinkFieldMappingResponse']]]:
        """
        The mappings between Interaction and Relationship fields.
        """
        return pulumi.get(self, "mappings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profilePropertyReferences")
    def profile_property_references(self) -> pulumi.Output[Sequence['outputs.ParticipantPropertyReferenceResponse']]:
        """
        The property references for the Profile of the Relationship.
        """
        return pulumi.get(self, "profile_property_references")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="relatedProfilePropertyReferences")
    def related_profile_property_references(self) -> pulumi.Output[Sequence['outputs.ParticipantPropertyReferenceResponse']]:
        """
        The property references for the Related Profile of the Relationship.
        """
        return pulumi.get(self, "related_profile_property_references")

    @property
    @pulumi.getter(name="relationshipGuidId")
    def relationship_guid_id(self) -> pulumi.Output[str]:
        """
        The relationship guid id.
        """
        return pulumi.get(self, "relationship_guid_id")

    @property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> pulumi.Output[str]:
        """
        The Relationship associated with the Link.
        """
        return pulumi.get(self, "relationship_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

