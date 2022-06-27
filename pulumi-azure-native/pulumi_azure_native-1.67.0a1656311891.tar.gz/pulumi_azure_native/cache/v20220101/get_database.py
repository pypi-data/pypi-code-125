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
    'GetDatabaseResult',
    'AwaitableGetDatabaseResult',
    'get_database',
    'get_database_output',
]

@pulumi.output_type
class GetDatabaseResult:
    """
    Describes a database on the RedisEnterprise cluster
    """
    def __init__(__self__, client_protocol=None, clustering_policy=None, eviction_policy=None, geo_replication=None, id=None, modules=None, name=None, persistence=None, port=None, provisioning_state=None, resource_state=None, type=None):
        if client_protocol and not isinstance(client_protocol, str):
            raise TypeError("Expected argument 'client_protocol' to be a str")
        pulumi.set(__self__, "client_protocol", client_protocol)
        if clustering_policy and not isinstance(clustering_policy, str):
            raise TypeError("Expected argument 'clustering_policy' to be a str")
        pulumi.set(__self__, "clustering_policy", clustering_policy)
        if eviction_policy and not isinstance(eviction_policy, str):
            raise TypeError("Expected argument 'eviction_policy' to be a str")
        pulumi.set(__self__, "eviction_policy", eviction_policy)
        if geo_replication and not isinstance(geo_replication, dict):
            raise TypeError("Expected argument 'geo_replication' to be a dict")
        pulumi.set(__self__, "geo_replication", geo_replication)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if modules and not isinstance(modules, list):
            raise TypeError("Expected argument 'modules' to be a list")
        pulumi.set(__self__, "modules", modules)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if persistence and not isinstance(persistence, dict):
            raise TypeError("Expected argument 'persistence' to be a dict")
        pulumi.set(__self__, "persistence", persistence)
        if port and not isinstance(port, int):
            raise TypeError("Expected argument 'port' to be a int")
        pulumi.set(__self__, "port", port)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clientProtocol")
    def client_protocol(self) -> Optional[str]:
        """
        Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted.
        """
        return pulumi.get(self, "client_protocol")

    @property
    @pulumi.getter(name="clusteringPolicy")
    def clustering_policy(self) -> Optional[str]:
        """
        Clustering policy - default is OSSCluster. Specified at create time.
        """
        return pulumi.get(self, "clustering_policy")

    @property
    @pulumi.getter(name="evictionPolicy")
    def eviction_policy(self) -> Optional[str]:
        """
        Redis eviction policy - default is VolatileLRU
        """
        return pulumi.get(self, "eviction_policy")

    @property
    @pulumi.getter(name="geoReplication")
    def geo_replication(self) -> Optional['outputs.DatabasePropertiesResponseGeoReplication']:
        """
        Optional set of properties to configure geo replication for this database.
        """
        return pulumi.get(self, "geo_replication")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def modules(self) -> Optional[Sequence['outputs.ModuleResponse']]:
        """
        Optional set of redis modules to enable in this database - modules can only be added at creation time.
        """
        return pulumi.get(self, "modules")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def persistence(self) -> Optional['outputs.PersistenceResponse']:
        """
        Persistence settings
        """
        return pulumi.get(self, "persistence")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        TCP port of the database endpoint. Specified at create time. Defaults to an available port.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current provisioning status of the database
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Current resource status of the database
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDatabaseResult(GetDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDatabaseResult(
            client_protocol=self.client_protocol,
            clustering_policy=self.clustering_policy,
            eviction_policy=self.eviction_policy,
            geo_replication=self.geo_replication,
            id=self.id,
            modules=self.modules,
            name=self.name,
            persistence=self.persistence,
            port=self.port,
            provisioning_state=self.provisioning_state,
            resource_state=self.resource_state,
            type=self.type)


def get_database(cluster_name: Optional[str] = None,
                 database_name: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDatabaseResult:
    """
    Describes a database on the RedisEnterprise cluster


    :param str cluster_name: The name of the RedisEnterprise cluster.
    :param str database_name: The name of the database.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20220101:getDatabase', __args__, opts=opts, typ=GetDatabaseResult).value

    return AwaitableGetDatabaseResult(
        client_protocol=__ret__.client_protocol,
        clustering_policy=__ret__.clustering_policy,
        eviction_policy=__ret__.eviction_policy,
        geo_replication=__ret__.geo_replication,
        id=__ret__.id,
        modules=__ret__.modules,
        name=__ret__.name,
        persistence=__ret__.persistence,
        port=__ret__.port,
        provisioning_state=__ret__.provisioning_state,
        resource_state=__ret__.resource_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_database)
def get_database_output(cluster_name: Optional[pulumi.Input[str]] = None,
                        database_name: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDatabaseResult]:
    """
    Describes a database on the RedisEnterprise cluster


    :param str cluster_name: The name of the RedisEnterprise cluster.
    :param str database_name: The name of the database.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
