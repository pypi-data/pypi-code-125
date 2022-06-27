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
    'ListBuildTaskSourceRepositoryPropertiesResult',
    'AwaitableListBuildTaskSourceRepositoryPropertiesResult',
    'list_build_task_source_repository_properties',
    'list_build_task_source_repository_properties_output',
]

@pulumi.output_type
class ListBuildTaskSourceRepositoryPropertiesResult:
    """
    The properties of the source code repository.
    """
    def __init__(__self__, is_commit_trigger_enabled=None, repository_url=None, source_control_auth_properties=None, source_control_type=None):
        if is_commit_trigger_enabled and not isinstance(is_commit_trigger_enabled, bool):
            raise TypeError("Expected argument 'is_commit_trigger_enabled' to be a bool")
        pulumi.set(__self__, "is_commit_trigger_enabled", is_commit_trigger_enabled)
        if repository_url and not isinstance(repository_url, str):
            raise TypeError("Expected argument 'repository_url' to be a str")
        pulumi.set(__self__, "repository_url", repository_url)
        if source_control_auth_properties and not isinstance(source_control_auth_properties, dict):
            raise TypeError("Expected argument 'source_control_auth_properties' to be a dict")
        pulumi.set(__self__, "source_control_auth_properties", source_control_auth_properties)
        if source_control_type and not isinstance(source_control_type, str):
            raise TypeError("Expected argument 'source_control_type' to be a str")
        pulumi.set(__self__, "source_control_type", source_control_type)

    @property
    @pulumi.getter(name="isCommitTriggerEnabled")
    def is_commit_trigger_enabled(self) -> Optional[bool]:
        """
        The value of this property indicates whether the source control commit trigger is enabled or not.
        """
        return pulumi.get(self, "is_commit_trigger_enabled")

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> str:
        """
        The full URL to the source code repository
        """
        return pulumi.get(self, "repository_url")

    @property
    @pulumi.getter(name="sourceControlAuthProperties")
    def source_control_auth_properties(self) -> Optional['outputs.SourceControlAuthInfoResponse']:
        """
        The authorization properties for accessing the source code repository.
        """
        return pulumi.get(self, "source_control_auth_properties")

    @property
    @pulumi.getter(name="sourceControlType")
    def source_control_type(self) -> str:
        """
        The type of source control service.
        """
        return pulumi.get(self, "source_control_type")


class AwaitableListBuildTaskSourceRepositoryPropertiesResult(ListBuildTaskSourceRepositoryPropertiesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListBuildTaskSourceRepositoryPropertiesResult(
            is_commit_trigger_enabled=self.is_commit_trigger_enabled,
            repository_url=self.repository_url,
            source_control_auth_properties=self.source_control_auth_properties,
            source_control_type=self.source_control_type)


def list_build_task_source_repository_properties(build_task_name: Optional[str] = None,
                                                 registry_name: Optional[str] = None,
                                                 resource_group_name: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListBuildTaskSourceRepositoryPropertiesResult:
    """
    The properties of the source code repository.


    :param str build_task_name: The name of the container registry build task.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    __args__ = dict()
    __args__['buildTaskName'] = build_task_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20180201preview:listBuildTaskSourceRepositoryProperties', __args__, opts=opts, typ=ListBuildTaskSourceRepositoryPropertiesResult).value

    return AwaitableListBuildTaskSourceRepositoryPropertiesResult(
        is_commit_trigger_enabled=__ret__.is_commit_trigger_enabled,
        repository_url=__ret__.repository_url,
        source_control_auth_properties=__ret__.source_control_auth_properties,
        source_control_type=__ret__.source_control_type)


@_utilities.lift_output_func(list_build_task_source_repository_properties)
def list_build_task_source_repository_properties_output(build_task_name: Optional[pulumi.Input[str]] = None,
                                                        registry_name: Optional[pulumi.Input[str]] = None,
                                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListBuildTaskSourceRepositoryPropertiesResult]:
    """
    The properties of the source code repository.


    :param str build_task_name: The name of the container registry build task.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    ...
