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
    'GetProjectResult',
    'AwaitableGetProjectResult',
    'get_project',
    'get_project_output',
]

@pulumi.output_type
class GetProjectResult:
    """
    Azure Migrate Project.
    """
    def __init__(__self__, e_tag=None, id=None, location=None, name=None, properties=None, tags=None, type=None):
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Path reference to this project /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/assessmentProjects/{projectName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Azure location in which project is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the project.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ProjectPropertiesResponse':
        """
        Properties of the project.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        Tags provided by Azure Tagging service.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the object = [Microsoft.Migrate/assessmentProjects].
        """
        return pulumi.get(self, "type")


class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            e_tag=self.e_tag,
            id=self.id,
            location=self.location,
            name=self.name,
            properties=self.properties,
            tags=self.tags,
            type=self.type)


def get_project(project_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectResult:
    """
    Azure Migrate Project.


    :param str project_name: Name of the Azure Migrate project.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    __args__ = dict()
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:migrate/v20191001:getProject', __args__, opts=opts, typ=GetProjectResult).value

    return AwaitableGetProjectResult(
        e_tag=__ret__.e_tag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        properties=__ret__.properties,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_project)
def get_project_output(project_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectResult]:
    """
    Azure Migrate Project.


    :param str project_name: Name of the Azure Migrate project.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    """
    ...
