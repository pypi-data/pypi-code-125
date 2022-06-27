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
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
    'get_environment_output',
]

warnings.warn("""Version 2018-08-15-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetEnvironmentResult:
    """
    An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource.
    """
    def __init__(__self__, id=None, kind=None, location=None, name=None, sku=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the environment.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        The sku determines the type of environment, either standard (S1 or S2) or long-term (L1). For standard environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_environment(environment_name: Optional[str] = None,
                    expand: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str expand: Setting $expand=status will include the status of the internal services of the environment in the Time Series Insights service.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    pulumi.log.warn("""get_environment is deprecated: Version 2018-08-15-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:timeseriesinsights/v20180815preview:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_environment)
def get_environment_output(environment_name: Optional[pulumi.Input[str]] = None,
                           expand: Optional[pulumi.Input[Optional[str]]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentResult]:
    """
    An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str expand: Setting $expand=status will include the status of the internal services of the environment in the Time Series Insights service.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    pulumi.log.warn("""get_environment is deprecated: Version 2018-08-15-preview will be removed in v2 of the provider.""")
    ...
