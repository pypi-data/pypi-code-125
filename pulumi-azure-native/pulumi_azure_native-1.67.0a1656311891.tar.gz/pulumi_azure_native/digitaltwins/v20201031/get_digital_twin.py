# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetDigitalTwinResult',
    'AwaitableGetDigitalTwinResult',
    'get_digital_twin',
    'get_digital_twin_output',
]

warnings.warn("""Version 2020-10-31 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetDigitalTwinResult:
    """
    The description of the DigitalTwins service.
    """
    def __init__(__self__, created_time=None, host_name=None, id=None, last_updated_time=None, location=None, name=None, provisioning_state=None, tags=None, type=None):
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        Time when DigitalTwinsInstance was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        Api endpoint to work with DigitalTwinsInstance.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> str:
        """
        Time when DigitalTwinsInstance was updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def location(self) -> str:
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
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetDigitalTwinResult(GetDigitalTwinResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDigitalTwinResult(
            created_time=self.created_time,
            host_name=self.host_name,
            id=self.id,
            last_updated_time=self.last_updated_time,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_digital_twin(resource_group_name: Optional[str] = None,
                     resource_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDigitalTwinResult:
    """
    The description of the DigitalTwins service.


    :param str resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :param str resource_name: The name of the DigitalTwinsInstance.
    """
    pulumi.log.warn("""get_digital_twin is deprecated: Version 2020-10-31 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:digitaltwins/v20201031:getDigitalTwin', __args__, opts=opts, typ=GetDigitalTwinResult).value

    return AwaitableGetDigitalTwinResult(
        created_time=__ret__.created_time,
        host_name=__ret__.host_name,
        id=__ret__.id,
        last_updated_time=__ret__.last_updated_time,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_digital_twin)
def get_digital_twin_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            resource_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDigitalTwinResult]:
    """
    The description of the DigitalTwins service.


    :param str resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
    :param str resource_name: The name of the DigitalTwinsInstance.
    """
    pulumi.log.warn("""get_digital_twin is deprecated: Version 2020-10-31 will be removed in v2 of the provider.""")
    ...
