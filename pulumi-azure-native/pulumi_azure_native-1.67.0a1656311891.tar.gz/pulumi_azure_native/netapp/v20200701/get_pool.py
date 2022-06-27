# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetPoolResult',
    'AwaitableGetPoolResult',
    'get_pool',
    'get_pool_output',
]

warnings.warn("""Version 2020-07-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetPoolResult:
    """
    Capacity pool resource
    """
    def __init__(__self__, id=None, location=None, name=None, pool_id=None, provisioning_state=None, qos_type=None, service_level=None, size=None, tags=None, total_throughput_mibps=None, type=None, utilized_throughput_mibps=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pool_id and not isinstance(pool_id, str):
            raise TypeError("Expected argument 'pool_id' to be a str")
        pulumi.set(__self__, "pool_id", pool_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if qos_type and not isinstance(qos_type, str):
            raise TypeError("Expected argument 'qos_type' to be a str")
        pulumi.set(__self__, "qos_type", qos_type)
        if service_level and not isinstance(service_level, str):
            raise TypeError("Expected argument 'service_level' to be a str")
        pulumi.set(__self__, "service_level", service_level)
        if size and not isinstance(size, float):
            raise TypeError("Expected argument 'size' to be a float")
        pulumi.set(__self__, "size", size)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if total_throughput_mibps and not isinstance(total_throughput_mibps, float):
            raise TypeError("Expected argument 'total_throughput_mibps' to be a float")
        pulumi.set(__self__, "total_throughput_mibps", total_throughput_mibps)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if utilized_throughput_mibps and not isinstance(utilized_throughput_mibps, float):
            raise TypeError("Expected argument 'utilized_throughput_mibps' to be a float")
        pulumi.set(__self__, "utilized_throughput_mibps", utilized_throughput_mibps)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="poolId")
    def pool_id(self) -> str:
        """
        UUID v4 used to identify the Pool
        """
        return pulumi.get(self, "pool_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="qosType")
    def qos_type(self) -> Optional[str]:
        """
        The qos type of the pool
        """
        return pulumi.get(self, "qos_type")

    @property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> str:
        """
        The service level of the file system
        """
        return pulumi.get(self, "service_level")

    @property
    @pulumi.getter
    def size(self) -> float:
        """
        Provisioned size of the pool (in bytes). Allowed values are in 4TiB chunks (value must be multiply of 4398046511104).
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="totalThroughputMibps")
    def total_throughput_mibps(self) -> float:
        """
        Total throughput of pool in Mibps
        """
        return pulumi.get(self, "total_throughput_mibps")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="utilizedThroughputMibps")
    def utilized_throughput_mibps(self) -> float:
        """
        Utilized throughput of pool in Mibps
        """
        return pulumi.get(self, "utilized_throughput_mibps")


class AwaitableGetPoolResult(GetPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPoolResult(
            id=self.id,
            location=self.location,
            name=self.name,
            pool_id=self.pool_id,
            provisioning_state=self.provisioning_state,
            qos_type=self.qos_type,
            service_level=self.service_level,
            size=self.size,
            tags=self.tags,
            total_throughput_mibps=self.total_throughput_mibps,
            type=self.type,
            utilized_throughput_mibps=self.utilized_throughput_mibps)


def get_pool(account_name: Optional[str] = None,
             pool_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPoolResult:
    """
    Capacity pool resource


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_pool is deprecated: Version 2020-07-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20200701:getPool', __args__, opts=opts, typ=GetPoolResult).value

    return AwaitableGetPoolResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        pool_id=__ret__.pool_id,
        provisioning_state=__ret__.provisioning_state,
        qos_type=__ret__.qos_type,
        service_level=__ret__.service_level,
        size=__ret__.size,
        tags=__ret__.tags,
        total_throughput_mibps=__ret__.total_throughput_mibps,
        type=__ret__.type,
        utilized_throughput_mibps=__ret__.utilized_throughput_mibps)


@_utilities.lift_output_func(get_pool)
def get_pool_output(account_name: Optional[pulumi.Input[str]] = None,
                    pool_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPoolResult]:
    """
    Capacity pool resource


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_pool is deprecated: Version 2020-07-01 will be removed in v2 of the provider.""")
    ...
