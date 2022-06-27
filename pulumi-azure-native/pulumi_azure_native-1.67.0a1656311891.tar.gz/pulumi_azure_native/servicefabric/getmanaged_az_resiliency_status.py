# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetmanagedAzResiliencyStatusResult',
    'AwaitableGetmanagedAzResiliencyStatusResult',
    'getmanaged_az_resiliency_status',
    'getmanaged_az_resiliency_status_output',
]

@pulumi.output_type
class GetmanagedAzResiliencyStatusResult:
    """
    Describes the result of the request to list Managed VM Sizes for Service Fabric Managed Clusters.
    """
    def __init__(__self__, base_resource_status=None, is_cluster_zone_resilient=None):
        if base_resource_status and not isinstance(base_resource_status, list):
            raise TypeError("Expected argument 'base_resource_status' to be a list")
        pulumi.set(__self__, "base_resource_status", base_resource_status)
        if is_cluster_zone_resilient and not isinstance(is_cluster_zone_resilient, bool):
            raise TypeError("Expected argument 'is_cluster_zone_resilient' to be a bool")
        pulumi.set(__self__, "is_cluster_zone_resilient", is_cluster_zone_resilient)

    @property
    @pulumi.getter(name="baseResourceStatus")
    def base_resource_status(self) -> Optional[Sequence['outputs.ResourceAzStatusResponse']]:
        """
        List of Managed VM Sizes for Service Fabric Managed Clusters.
        """
        return pulumi.get(self, "base_resource_status")

    @property
    @pulumi.getter(name="isClusterZoneResilient")
    def is_cluster_zone_resilient(self) -> bool:
        """
        URL to get the next set of Managed VM Sizes if there are any.
        """
        return pulumi.get(self, "is_cluster_zone_resilient")


class AwaitableGetmanagedAzResiliencyStatusResult(GetmanagedAzResiliencyStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetmanagedAzResiliencyStatusResult(
            base_resource_status=self.base_resource_status,
            is_cluster_zone_resilient=self.is_cluster_zone_resilient)


def getmanaged_az_resiliency_status(cluster_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetmanagedAzResiliencyStatusResult:
    """
    Describes the result of the request to list Managed VM Sizes for Service Fabric Managed Clusters.
    API Version: 2022-02-01-preview.


    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric:getmanagedAzResiliencyStatus', __args__, opts=opts, typ=GetmanagedAzResiliencyStatusResult).value

    return AwaitableGetmanagedAzResiliencyStatusResult(
        base_resource_status=__ret__.base_resource_status,
        is_cluster_zone_resilient=__ret__.is_cluster_zone_resilient)


@_utilities.lift_output_func(getmanaged_az_resiliency_status)
def getmanaged_az_resiliency_status_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetmanagedAzResiliencyStatusResult]:
    """
    Describes the result of the request to list Managed VM Sizes for Service Fabric Managed Clusters.
    API Version: 2022-02-01-preview.


    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    """
    ...
