# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetFactoryResult',
    'AwaitableGetFactoryResult',
    'get_factory',
    'get_factory_output',
]

@pulumi.output_type
class GetFactoryResult:
    """
    Factory resource type.
    """
    def __init__(__self__, create_time=None, e_tag=None, encryption=None, global_parameters=None, id=None, identity=None, location=None, name=None, provisioning_state=None, public_network_access=None, purview_configuration=None, repo_configuration=None, tags=None, type=None, version=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if global_parameters and not isinstance(global_parameters, dict):
            raise TypeError("Expected argument 'global_parameters' to be a dict")
        pulumi.set(__self__, "global_parameters", global_parameters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if purview_configuration and not isinstance(purview_configuration, dict):
            raise TypeError("Expected argument 'purview_configuration' to be a dict")
        pulumi.set(__self__, "purview_configuration", purview_configuration)
        if repo_configuration and not isinstance(repo_configuration, dict):
            raise TypeError("Expected argument 'repo_configuration' to be a dict")
        pulumi.set(__self__, "repo_configuration", repo_configuration)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time the factory was created in ISO8601 format.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionConfigurationResponse']:
        """
        Properties to enable Customer Managed Key for the factory.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="globalParameters")
    def global_parameters(self) -> Optional[Mapping[str, 'outputs.GlobalParameterSpecificationResponse']]:
        """
        List of parameters for factory.
        """
        return pulumi.get(self, "global_parameters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.FactoryIdentityResponse']:
        """
        Managed service identity of the factory.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Factory provisioning state, example Succeeded.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Whether or not public network access is allowed for the data factory.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(self) -> Optional['outputs.PurviewConfigurationResponse']:
        """
        Purview information of the factory.
        """
        return pulumi.get(self, "purview_configuration")

    @property
    @pulumi.getter(name="repoConfiguration")
    def repo_configuration(self) -> Optional[Any]:
        """
        Git repo information of the factory.
        """
        return pulumi.get(self, "repo_configuration")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of the factory.
        """
        return pulumi.get(self, "version")


class AwaitableGetFactoryResult(GetFactoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFactoryResult(
            create_time=self.create_time,
            e_tag=self.e_tag,
            encryption=self.encryption,
            global_parameters=self.global_parameters,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            purview_configuration=self.purview_configuration,
            repo_configuration=self.repo_configuration,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_factory(factory_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFactoryResult:
    """
    Factory resource type.


    :param str factory_name: The factory name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory/v20180601:getFactory', __args__, opts=opts, typ=GetFactoryResult).value

    return AwaitableGetFactoryResult(
        create_time=__ret__.create_time,
        e_tag=__ret__.e_tag,
        encryption=__ret__.encryption,
        global_parameters=__ret__.global_parameters,
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        public_network_access=__ret__.public_network_access,
        purview_configuration=__ret__.purview_configuration,
        repo_configuration=__ret__.repo_configuration,
        tags=__ret__.tags,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_factory)
def get_factory_output(factory_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFactoryResult]:
    """
    Factory resource type.


    :param str factory_name: The factory name.
    :param str resource_group_name: The resource group name.
    """
    ...
