# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['SqlDWTableDataSetMappingArgs', 'SqlDWTableDataSetMapping']

@pulumi.input_type
class SqlDWTableDataSetMappingArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 data_set_id: pulumi.Input[str],
                 data_warehouse_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 schema_name: pulumi.Input[str],
                 share_subscription_name: pulumi.Input[str],
                 sql_server_resource_id: pulumi.Input[str],
                 table_name: pulumi.Input[str],
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlDWTableDataSetMapping resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] data_set_id: The id of the source data set.
        :param pulumi.Input[str] data_warehouse_name: DataWarehouse name of the source data set
        :param pulumi.Input[str] kind: Kind of data set mapping.
               Expected value is 'SqlDWTable'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] schema_name: Schema of the table. Default value is dbo.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[str] sql_server_resource_id: Resource id of SQL server
        :param pulumi.Input[str] table_name: SQL DW table name.
        :param pulumi.Input[str] data_set_mapping_name: The name of the data set mapping to be created.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "data_set_id", data_set_id)
        pulumi.set(__self__, "data_warehouse_name", data_warehouse_name)
        pulumi.set(__self__, "kind", 'SqlDWTable')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schema_name", schema_name)
        pulumi.set(__self__, "share_subscription_name", share_subscription_name)
        pulumi.set(__self__, "sql_server_resource_id", sql_server_resource_id)
        pulumi.set(__self__, "table_name", table_name)
        if data_set_mapping_name is not None:
            pulumi.set(__self__, "data_set_mapping_name", data_set_mapping_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the share account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Input[str]:
        """
        The id of the source data set.
        """
        return pulumi.get(self, "data_set_id")

    @data_set_id.setter
    def data_set_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_set_id", value)

    @property
    @pulumi.getter(name="dataWarehouseName")
    def data_warehouse_name(self) -> pulumi.Input[str]:
        """
        DataWarehouse name of the source data set
        """
        return pulumi.get(self, "data_warehouse_name")

    @data_warehouse_name.setter
    def data_warehouse_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_warehouse_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of data set mapping.
        Expected value is 'SqlDWTable'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Input[str]:
        """
        Schema of the table. Default value is dbo.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema_name", value)

    @property
    @pulumi.getter(name="shareSubscriptionName")
    def share_subscription_name(self) -> pulumi.Input[str]:
        """
        The name of the share subscription which will hold the data set sink.
        """
        return pulumi.get(self, "share_subscription_name")

    @share_subscription_name.setter
    def share_subscription_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "share_subscription_name", value)

    @property
    @pulumi.getter(name="sqlServerResourceId")
    def sql_server_resource_id(self) -> pulumi.Input[str]:
        """
        Resource id of SQL server
        """
        return pulumi.get(self, "sql_server_resource_id")

    @sql_server_resource_id.setter
    def sql_server_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_server_resource_id", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[str]:
        """
        SQL DW table name.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter(name="dataSetMappingName")
    def data_set_mapping_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data set mapping to be created.
        """
        return pulumi.get(self, "data_set_mapping_name")

    @data_set_mapping_name.setter
    def data_set_mapping_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_set_mapping_name", value)


class SqlDWTableDataSetMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                 data_warehouse_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 sql_server_resource_id: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A SQL DW Table data set mapping.
        API Version: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] data_set_id: The id of the source data set.
        :param pulumi.Input[str] data_set_mapping_name: The name of the data set mapping to be created.
        :param pulumi.Input[str] data_warehouse_name: DataWarehouse name of the source data set
        :param pulumi.Input[str] kind: Kind of data set mapping.
               Expected value is 'SqlDWTable'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] schema_name: Schema of the table. Default value is dbo.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[str] sql_server_resource_id: Resource id of SQL server
        :param pulumi.Input[str] table_name: SQL DW table name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlDWTableDataSetMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SQL DW Table data set mapping.
        API Version: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param SqlDWTableDataSetMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlDWTableDataSetMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 data_set_id: Optional[pulumi.Input[str]] = None,
                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                 data_warehouse_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 sql_server_resource_id: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlDWTableDataSetMappingArgs.__new__(SqlDWTableDataSetMappingArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if data_set_id is None and not opts.urn:
                raise TypeError("Missing required property 'data_set_id'")
            __props__.__dict__["data_set_id"] = data_set_id
            __props__.__dict__["data_set_mapping_name"] = data_set_mapping_name
            if data_warehouse_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_warehouse_name'")
            __props__.__dict__["data_warehouse_name"] = data_warehouse_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'SqlDWTable'
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if schema_name is None and not opts.urn:
                raise TypeError("Missing required property 'schema_name'")
            __props__.__dict__["schema_name"] = schema_name
            if share_subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'share_subscription_name'")
            __props__.__dict__["share_subscription_name"] = share_subscription_name
            if sql_server_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'sql_server_resource_id'")
            __props__.__dict__["sql_server_resource_id"] = sql_server_resource_id
            if table_name is None and not opts.urn:
                raise TypeError("Missing required property 'table_name'")
            __props__.__dict__["table_name"] = table_name
            __props__.__dict__["data_set_mapping_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datashare/v20181101preview:SqlDWTableDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20191101:SqlDWTableDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20200901:SqlDWTableDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:SqlDWTableDataSetMapping"), pulumi.Alias(type_="azure-native:datashare/v20210801:SqlDWTableDataSetMapping")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlDWTableDataSetMapping, __self__).__init__(
            'azure-native:datashare:SqlDWTableDataSetMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlDWTableDataSetMapping':
        """
        Get an existing SqlDWTableDataSetMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlDWTableDataSetMappingArgs.__new__(SqlDWTableDataSetMappingArgs)

        __props__.__dict__["data_set_id"] = None
        __props__.__dict__["data_set_mapping_status"] = None
        __props__.__dict__["data_warehouse_name"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["schema_name"] = None
        __props__.__dict__["sql_server_resource_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["type"] = None
        return SqlDWTableDataSetMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> pulumi.Output[str]:
        """
        The id of the source data set.
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataSetMappingStatus")
    def data_set_mapping_status(self) -> pulumi.Output[str]:
        """
        Gets the status of the data set mapping.
        """
        return pulumi.get(self, "data_set_mapping_status")

    @property
    @pulumi.getter(name="dataWarehouseName")
    def data_warehouse_name(self) -> pulumi.Output[str]:
        """
        DataWarehouse name of the source data set
        """
        return pulumi.get(self, "data_warehouse_name")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of data set mapping.
        Expected value is 'SqlDWTable'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the data set mapping.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> pulumi.Output[str]:
        """
        Schema of the table. Default value is dbo.
        """
        return pulumi.get(self, "schema_name")

    @property
    @pulumi.getter(name="sqlServerResourceId")
    def sql_server_resource_id(self) -> pulumi.Output[str]:
        """
        Resource id of SQL server
        """
        return pulumi.get(self, "sql_server_resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[str]:
        """
        SQL DW table name.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

