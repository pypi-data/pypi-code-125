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
    'GetAccountResult',
    'AwaitableGetAccountResult',
    'get_account',
    'get_account_output',
]

warnings.warn("""Version 2015-10-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetAccountResult:
    """
    A Data Lake Analytics account object, containing all information associated with the named Data Lake Analytics account.
    """
    def __init__(__self__, account_id=None, compute_policies=None, creation_time=None, current_tier=None, data_lake_store_accounts=None, debug_data_access_level=None, default_data_lake_store_account=None, endpoint=None, firewall_allow_azure_ips=None, firewall_rules=None, firewall_state=None, hierarchical_queue_state=None, hive_metastores=None, id=None, last_modified_time=None, location=None, max_degree_of_parallelism=None, max_degree_of_parallelism_per_job=None, max_job_count=None, min_priority_per_job=None, name=None, new_tier=None, provisioning_state=None, public_data_lake_store_accounts=None, query_store_retention=None, state=None, storage_accounts=None, system_max_degree_of_parallelism=None, system_max_job_count=None, tags=None, type=None, virtual_network_rules=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if compute_policies and not isinstance(compute_policies, list):
            raise TypeError("Expected argument 'compute_policies' to be a list")
        pulumi.set(__self__, "compute_policies", compute_policies)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if current_tier and not isinstance(current_tier, str):
            raise TypeError("Expected argument 'current_tier' to be a str")
        pulumi.set(__self__, "current_tier", current_tier)
        if data_lake_store_accounts and not isinstance(data_lake_store_accounts, list):
            raise TypeError("Expected argument 'data_lake_store_accounts' to be a list")
        pulumi.set(__self__, "data_lake_store_accounts", data_lake_store_accounts)
        if debug_data_access_level and not isinstance(debug_data_access_level, str):
            raise TypeError("Expected argument 'debug_data_access_level' to be a str")
        pulumi.set(__self__, "debug_data_access_level", debug_data_access_level)
        if default_data_lake_store_account and not isinstance(default_data_lake_store_account, str):
            raise TypeError("Expected argument 'default_data_lake_store_account' to be a str")
        pulumi.set(__self__, "default_data_lake_store_account", default_data_lake_store_account)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if firewall_allow_azure_ips and not isinstance(firewall_allow_azure_ips, str):
            raise TypeError("Expected argument 'firewall_allow_azure_ips' to be a str")
        pulumi.set(__self__, "firewall_allow_azure_ips", firewall_allow_azure_ips)
        if firewall_rules and not isinstance(firewall_rules, list):
            raise TypeError("Expected argument 'firewall_rules' to be a list")
        pulumi.set(__self__, "firewall_rules", firewall_rules)
        if firewall_state and not isinstance(firewall_state, str):
            raise TypeError("Expected argument 'firewall_state' to be a str")
        pulumi.set(__self__, "firewall_state", firewall_state)
        if hierarchical_queue_state and not isinstance(hierarchical_queue_state, str):
            raise TypeError("Expected argument 'hierarchical_queue_state' to be a str")
        pulumi.set(__self__, "hierarchical_queue_state", hierarchical_queue_state)
        if hive_metastores and not isinstance(hive_metastores, list):
            raise TypeError("Expected argument 'hive_metastores' to be a list")
        pulumi.set(__self__, "hive_metastores", hive_metastores)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_degree_of_parallelism and not isinstance(max_degree_of_parallelism, int):
            raise TypeError("Expected argument 'max_degree_of_parallelism' to be a int")
        pulumi.set(__self__, "max_degree_of_parallelism", max_degree_of_parallelism)
        if max_degree_of_parallelism_per_job and not isinstance(max_degree_of_parallelism_per_job, int):
            raise TypeError("Expected argument 'max_degree_of_parallelism_per_job' to be a int")
        pulumi.set(__self__, "max_degree_of_parallelism_per_job", max_degree_of_parallelism_per_job)
        if max_job_count and not isinstance(max_job_count, int):
            raise TypeError("Expected argument 'max_job_count' to be a int")
        pulumi.set(__self__, "max_job_count", max_job_count)
        if min_priority_per_job and not isinstance(min_priority_per_job, int):
            raise TypeError("Expected argument 'min_priority_per_job' to be a int")
        pulumi.set(__self__, "min_priority_per_job", min_priority_per_job)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if new_tier and not isinstance(new_tier, str):
            raise TypeError("Expected argument 'new_tier' to be a str")
        pulumi.set(__self__, "new_tier", new_tier)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_data_lake_store_accounts and not isinstance(public_data_lake_store_accounts, list):
            raise TypeError("Expected argument 'public_data_lake_store_accounts' to be a list")
        pulumi.set(__self__, "public_data_lake_store_accounts", public_data_lake_store_accounts)
        if query_store_retention and not isinstance(query_store_retention, int):
            raise TypeError("Expected argument 'query_store_retention' to be a int")
        pulumi.set(__self__, "query_store_retention", query_store_retention)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_accounts and not isinstance(storage_accounts, list):
            raise TypeError("Expected argument 'storage_accounts' to be a list")
        pulumi.set(__self__, "storage_accounts", storage_accounts)
        if system_max_degree_of_parallelism and not isinstance(system_max_degree_of_parallelism, int):
            raise TypeError("Expected argument 'system_max_degree_of_parallelism' to be a int")
        pulumi.set(__self__, "system_max_degree_of_parallelism", system_max_degree_of_parallelism)
        if system_max_job_count and not isinstance(system_max_job_count, int):
            raise TypeError("Expected argument 'system_max_job_count' to be a int")
        pulumi.set(__self__, "system_max_job_count", system_max_job_count)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network_rules and not isinstance(virtual_network_rules, list):
            raise TypeError("Expected argument 'virtual_network_rules' to be a list")
        pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        """
        The unique identifier associated with this Data Lake Analytics account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="computePolicies")
    def compute_policies(self) -> Sequence['outputs.ComputePolicyResponse']:
        """
        The list of compute policies associated with this account.
        """
        return pulumi.get(self, "compute_policies")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The account creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="currentTier")
    def current_tier(self) -> str:
        """
        The commitment tier in use for the current month.
        """
        return pulumi.get(self, "current_tier")

    @property
    @pulumi.getter(name="dataLakeStoreAccounts")
    def data_lake_store_accounts(self) -> Optional[Sequence['outputs.DataLakeStoreAccountInformationResponse']]:
        """
        The list of Data Lake Store accounts associated with this account.
        """
        return pulumi.get(self, "data_lake_store_accounts")

    @property
    @pulumi.getter(name="debugDataAccessLevel")
    def debug_data_access_level(self) -> str:
        """
        The current state of the DebugDataAccessLevel for this account.
        """
        return pulumi.get(self, "debug_data_access_level")

    @property
    @pulumi.getter(name="defaultDataLakeStoreAccount")
    def default_data_lake_store_account(self) -> str:
        """
        The default Data Lake Store account associated with this account.
        """
        return pulumi.get(self, "default_data_lake_store_account")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        """
        The full CName endpoint for this account.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="firewallAllowAzureIps")
    def firewall_allow_azure_ips(self) -> Optional[str]:
        """
        The current state of allowing or disallowing IPs originating within Azure through the firewall. If the firewall is disabled, this is not enforced.
        """
        return pulumi.get(self, "firewall_allow_azure_ips")

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Sequence['outputs.FirewallRuleResponse']:
        """
        The list of firewall rules associated with this account.
        """
        return pulumi.get(self, "firewall_rules")

    @property
    @pulumi.getter(name="firewallState")
    def firewall_state(self) -> Optional[str]:
        """
        The current state of the IP address firewall for this account.
        """
        return pulumi.get(self, "firewall_state")

    @property
    @pulumi.getter(name="hierarchicalQueueState")
    def hierarchical_queue_state(self) -> str:
        """
        The hierarchical queue state associated with this account.
        """
        return pulumi.get(self, "hierarchical_queue_state")

    @property
    @pulumi.getter(name="hiveMetastores")
    def hive_metastores(self) -> Sequence['outputs.HiveMetastoreResponse']:
        """
        The list of hiveMetastores associated with this account.
        """
        return pulumi.get(self, "hive_metastores")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        The account last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxDegreeOfParallelism")
    def max_degree_of_parallelism(self) -> Optional[int]:
        """
        The maximum supported degree of parallelism for this account.
        """
        return pulumi.get(self, "max_degree_of_parallelism")

    @property
    @pulumi.getter(name="maxDegreeOfParallelismPerJob")
    def max_degree_of_parallelism_per_job(self) -> Optional[int]:
        """
        The maximum supported degree of parallelism per job for this account.
        """
        return pulumi.get(self, "max_degree_of_parallelism_per_job")

    @property
    @pulumi.getter(name="maxJobCount")
    def max_job_count(self) -> Optional[int]:
        """
        The maximum supported jobs running under the account at the same time.
        """
        return pulumi.get(self, "max_job_count")

    @property
    @pulumi.getter(name="minPriorityPerJob")
    def min_priority_per_job(self) -> int:
        """
        The minimum supported priority per job for this account.
        """
        return pulumi.get(self, "min_priority_per_job")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="newTier")
    def new_tier(self) -> Optional[str]:
        """
        The commitment tier for the next month.
        """
        return pulumi.get(self, "new_tier")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning status of the Data Lake Analytics account.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicDataLakeStoreAccounts")
    def public_data_lake_store_accounts(self) -> Optional[Sequence['outputs.DataLakeStoreAccountInformationResponse']]:
        """
        The list of Data Lake Store accounts associated with this account.
        """
        return pulumi.get(self, "public_data_lake_store_accounts")

    @property
    @pulumi.getter(name="queryStoreRetention")
    def query_store_retention(self) -> Optional[int]:
        """
        The number of days that job metadata is retained.
        """
        return pulumi.get(self, "query_store_retention")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the Data Lake Analytics account.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageAccounts")
    def storage_accounts(self) -> Sequence['outputs.StorageAccountInformationResponse']:
        """
        The list of Azure Blob Storage accounts associated with this account.
        """
        return pulumi.get(self, "storage_accounts")

    @property
    @pulumi.getter(name="systemMaxDegreeOfParallelism")
    def system_max_degree_of_parallelism(self) -> int:
        """
        The system defined maximum supported degree of parallelism for this account, which restricts the maximum value of parallelism the user can set for the account.
        """
        return pulumi.get(self, "system_max_degree_of_parallelism")

    @property
    @pulumi.getter(name="systemMaxJobCount")
    def system_max_job_count(self) -> int:
        """
        The system defined maximum supported jobs running under the account at the same time, which restricts the maximum number of running jobs the user can set for the account.
        """
        return pulumi.get(self, "system_max_job_count")

    @property
    @pulumi.getter
    def tags(self) -> Mapping[str, str]:
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
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Sequence['outputs.VirtualNetworkRuleResponse']:
        """
        The list of virtualNetwork rules associated with this account.
        """
        return pulumi.get(self, "virtual_network_rules")


class AwaitableGetAccountResult(GetAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountResult(
            account_id=self.account_id,
            compute_policies=self.compute_policies,
            creation_time=self.creation_time,
            current_tier=self.current_tier,
            data_lake_store_accounts=self.data_lake_store_accounts,
            debug_data_access_level=self.debug_data_access_level,
            default_data_lake_store_account=self.default_data_lake_store_account,
            endpoint=self.endpoint,
            firewall_allow_azure_ips=self.firewall_allow_azure_ips,
            firewall_rules=self.firewall_rules,
            firewall_state=self.firewall_state,
            hierarchical_queue_state=self.hierarchical_queue_state,
            hive_metastores=self.hive_metastores,
            id=self.id,
            last_modified_time=self.last_modified_time,
            location=self.location,
            max_degree_of_parallelism=self.max_degree_of_parallelism,
            max_degree_of_parallelism_per_job=self.max_degree_of_parallelism_per_job,
            max_job_count=self.max_job_count,
            min_priority_per_job=self.min_priority_per_job,
            name=self.name,
            new_tier=self.new_tier,
            provisioning_state=self.provisioning_state,
            public_data_lake_store_accounts=self.public_data_lake_store_accounts,
            query_store_retention=self.query_store_retention,
            state=self.state,
            storage_accounts=self.storage_accounts,
            system_max_degree_of_parallelism=self.system_max_degree_of_parallelism,
            system_max_job_count=self.system_max_job_count,
            tags=self.tags,
            type=self.type,
            virtual_network_rules=self.virtual_network_rules)


def get_account(account_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountResult:
    """
    A Data Lake Analytics account object, containing all information associated with the named Data Lake Analytics account.


    :param str account_name: The name of the Data Lake Analytics account to retrieve.
    :param str resource_group_name: The name of the Azure resource group.
    """
    pulumi.log.warn("""get_account is deprecated: Version 2015-10-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datalakeanalytics/v20151001preview:getAccount', __args__, opts=opts, typ=GetAccountResult).value

    return AwaitableGetAccountResult(
        account_id=__ret__.account_id,
        compute_policies=__ret__.compute_policies,
        creation_time=__ret__.creation_time,
        current_tier=__ret__.current_tier,
        data_lake_store_accounts=__ret__.data_lake_store_accounts,
        debug_data_access_level=__ret__.debug_data_access_level,
        default_data_lake_store_account=__ret__.default_data_lake_store_account,
        endpoint=__ret__.endpoint,
        firewall_allow_azure_ips=__ret__.firewall_allow_azure_ips,
        firewall_rules=__ret__.firewall_rules,
        firewall_state=__ret__.firewall_state,
        hierarchical_queue_state=__ret__.hierarchical_queue_state,
        hive_metastores=__ret__.hive_metastores,
        id=__ret__.id,
        last_modified_time=__ret__.last_modified_time,
        location=__ret__.location,
        max_degree_of_parallelism=__ret__.max_degree_of_parallelism,
        max_degree_of_parallelism_per_job=__ret__.max_degree_of_parallelism_per_job,
        max_job_count=__ret__.max_job_count,
        min_priority_per_job=__ret__.min_priority_per_job,
        name=__ret__.name,
        new_tier=__ret__.new_tier,
        provisioning_state=__ret__.provisioning_state,
        public_data_lake_store_accounts=__ret__.public_data_lake_store_accounts,
        query_store_retention=__ret__.query_store_retention,
        state=__ret__.state,
        storage_accounts=__ret__.storage_accounts,
        system_max_degree_of_parallelism=__ret__.system_max_degree_of_parallelism,
        system_max_job_count=__ret__.system_max_job_count,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_network_rules=__ret__.virtual_network_rules)


@_utilities.lift_output_func(get_account)
def get_account_output(account_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccountResult]:
    """
    A Data Lake Analytics account object, containing all information associated with the named Data Lake Analytics account.


    :param str account_name: The name of the Data Lake Analytics account to retrieve.
    :param str resource_group_name: The name of the Azure resource group.
    """
    pulumi.log.warn("""get_account is deprecated: Version 2015-10-01-preview will be removed in v2 of the provider.""")
    ...
