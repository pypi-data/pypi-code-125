# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['SqlVirtualMachineArgs', 'SqlVirtualMachine']

@pulumi.input_type
class SqlVirtualMachineArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 assessment_settings: Optional[pulumi.Input['AssessmentSettingsArgs']] = None,
                 auto_backup_settings: Optional[pulumi.Input['AutoBackupSettingsArgs']] = None,
                 auto_patching_settings: Optional[pulumi.Input['AutoPatchingSettingsArgs']] = None,
                 identity: Optional[pulumi.Input['ResourceIdentityArgs']] = None,
                 key_vault_credential_settings: Optional[pulumi.Input['KeyVaultCredentialSettingsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 server_configurations_management_settings: Optional[pulumi.Input['ServerConfigurationsManagementSettingsArgs']] = None,
                 sql_image_offer: Optional[pulumi.Input[str]] = None,
                 sql_image_sku: Optional[pulumi.Input[Union[str, 'SqlImageSku']]] = None,
                 sql_management: Optional[pulumi.Input[Union[str, 'SqlManagementMode']]] = None,
                 sql_server_license_type: Optional[pulumi.Input[Union[str, 'SqlServerLicenseType']]] = None,
                 sql_virtual_machine_group_resource_id: Optional[pulumi.Input[str]] = None,
                 sql_virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 storage_configuration_settings: Optional[pulumi.Input['StorageConfigurationSettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_resource_id: Optional[pulumi.Input[str]] = None,
                 wsfc_domain_credentials: Optional[pulumi.Input['WsfcDomainCredentialsArgs']] = None):
        """
        The set of arguments for constructing a SqlVirtualMachine resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input['AssessmentSettingsArgs'] assessment_settings: Assessment Settings.
        :param pulumi.Input['AutoBackupSettingsArgs'] auto_backup_settings: Auto backup settings for SQL Server.
        :param pulumi.Input['AutoPatchingSettingsArgs'] auto_patching_settings: Auto patching settings for applying critical security updates to SQL virtual machine.
        :param pulumi.Input['ResourceIdentityArgs'] identity: Azure Active Directory identity of the server.
        :param pulumi.Input['KeyVaultCredentialSettingsArgs'] key_vault_credential_settings: Key vault credential settings.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['ServerConfigurationsManagementSettingsArgs'] server_configurations_management_settings: SQL Server configuration management settings.
        :param pulumi.Input[str] sql_image_offer: SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.
        :param pulumi.Input[Union[str, 'SqlImageSku']] sql_image_sku: SQL Server edition type.
        :param pulumi.Input[Union[str, 'SqlManagementMode']] sql_management: SQL Server Management type.
        :param pulumi.Input[Union[str, 'SqlServerLicenseType']] sql_server_license_type: SQL Server license type.
        :param pulumi.Input[str] sql_virtual_machine_group_resource_id: ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.
        :param pulumi.Input[str] sql_virtual_machine_name: Name of the SQL virtual machine.
        :param pulumi.Input['StorageConfigurationSettingsArgs'] storage_configuration_settings: Storage Configuration Settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_machine_resource_id: ARM Resource id of underlying virtual machine created from SQL marketplace image.
        :param pulumi.Input['WsfcDomainCredentialsArgs'] wsfc_domain_credentials: Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if assessment_settings is not None:
            pulumi.set(__self__, "assessment_settings", assessment_settings)
        if auto_backup_settings is not None:
            pulumi.set(__self__, "auto_backup_settings", auto_backup_settings)
        if auto_patching_settings is not None:
            pulumi.set(__self__, "auto_patching_settings", auto_patching_settings)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if key_vault_credential_settings is not None:
            pulumi.set(__self__, "key_vault_credential_settings", key_vault_credential_settings)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if server_configurations_management_settings is not None:
            pulumi.set(__self__, "server_configurations_management_settings", server_configurations_management_settings)
        if sql_image_offer is not None:
            pulumi.set(__self__, "sql_image_offer", sql_image_offer)
        if sql_image_sku is not None:
            pulumi.set(__self__, "sql_image_sku", sql_image_sku)
        if sql_management is not None:
            pulumi.set(__self__, "sql_management", sql_management)
        if sql_server_license_type is not None:
            pulumi.set(__self__, "sql_server_license_type", sql_server_license_type)
        if sql_virtual_machine_group_resource_id is not None:
            pulumi.set(__self__, "sql_virtual_machine_group_resource_id", sql_virtual_machine_group_resource_id)
        if sql_virtual_machine_name is not None:
            pulumi.set(__self__, "sql_virtual_machine_name", sql_virtual_machine_name)
        if storage_configuration_settings is not None:
            pulumi.set(__self__, "storage_configuration_settings", storage_configuration_settings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if virtual_machine_resource_id is not None:
            pulumi.set(__self__, "virtual_machine_resource_id", virtual_machine_resource_id)
        if wsfc_domain_credentials is not None:
            pulumi.set(__self__, "wsfc_domain_credentials", wsfc_domain_credentials)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="assessmentSettings")
    def assessment_settings(self) -> Optional[pulumi.Input['AssessmentSettingsArgs']]:
        """
        Assessment Settings.
        """
        return pulumi.get(self, "assessment_settings")

    @assessment_settings.setter
    def assessment_settings(self, value: Optional[pulumi.Input['AssessmentSettingsArgs']]):
        pulumi.set(self, "assessment_settings", value)

    @property
    @pulumi.getter(name="autoBackupSettings")
    def auto_backup_settings(self) -> Optional[pulumi.Input['AutoBackupSettingsArgs']]:
        """
        Auto backup settings for SQL Server.
        """
        return pulumi.get(self, "auto_backup_settings")

    @auto_backup_settings.setter
    def auto_backup_settings(self, value: Optional[pulumi.Input['AutoBackupSettingsArgs']]):
        pulumi.set(self, "auto_backup_settings", value)

    @property
    @pulumi.getter(name="autoPatchingSettings")
    def auto_patching_settings(self) -> Optional[pulumi.Input['AutoPatchingSettingsArgs']]:
        """
        Auto patching settings for applying critical security updates to SQL virtual machine.
        """
        return pulumi.get(self, "auto_patching_settings")

    @auto_patching_settings.setter
    def auto_patching_settings(self, value: Optional[pulumi.Input['AutoPatchingSettingsArgs']]):
        pulumi.set(self, "auto_patching_settings", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ResourceIdentityArgs']]:
        """
        Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="keyVaultCredentialSettings")
    def key_vault_credential_settings(self) -> Optional[pulumi.Input['KeyVaultCredentialSettingsArgs']]:
        """
        Key vault credential settings.
        """
        return pulumi.get(self, "key_vault_credential_settings")

    @key_vault_credential_settings.setter
    def key_vault_credential_settings(self, value: Optional[pulumi.Input['KeyVaultCredentialSettingsArgs']]):
        pulumi.set(self, "key_vault_credential_settings", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="serverConfigurationsManagementSettings")
    def server_configurations_management_settings(self) -> Optional[pulumi.Input['ServerConfigurationsManagementSettingsArgs']]:
        """
        SQL Server configuration management settings.
        """
        return pulumi.get(self, "server_configurations_management_settings")

    @server_configurations_management_settings.setter
    def server_configurations_management_settings(self, value: Optional[pulumi.Input['ServerConfigurationsManagementSettingsArgs']]):
        pulumi.set(self, "server_configurations_management_settings", value)

    @property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[pulumi.Input[str]]:
        """
        SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.
        """
        return pulumi.get(self, "sql_image_offer")

    @sql_image_offer.setter
    def sql_image_offer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_image_offer", value)

    @property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[pulumi.Input[Union[str, 'SqlImageSku']]]:
        """
        SQL Server edition type.
        """
        return pulumi.get(self, "sql_image_sku")

    @sql_image_sku.setter
    def sql_image_sku(self, value: Optional[pulumi.Input[Union[str, 'SqlImageSku']]]):
        pulumi.set(self, "sql_image_sku", value)

    @property
    @pulumi.getter(name="sqlManagement")
    def sql_management(self) -> Optional[pulumi.Input[Union[str, 'SqlManagementMode']]]:
        """
        SQL Server Management type.
        """
        return pulumi.get(self, "sql_management")

    @sql_management.setter
    def sql_management(self, value: Optional[pulumi.Input[Union[str, 'SqlManagementMode']]]):
        pulumi.set(self, "sql_management", value)

    @property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> Optional[pulumi.Input[Union[str, 'SqlServerLicenseType']]]:
        """
        SQL Server license type.
        """
        return pulumi.get(self, "sql_server_license_type")

    @sql_server_license_type.setter
    def sql_server_license_type(self, value: Optional[pulumi.Input[Union[str, 'SqlServerLicenseType']]]):
        pulumi.set(self, "sql_server_license_type", value)

    @property
    @pulumi.getter(name="sqlVirtualMachineGroupResourceId")
    def sql_virtual_machine_group_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.
        """
        return pulumi.get(self, "sql_virtual_machine_group_resource_id")

    @sql_virtual_machine_group_resource_id.setter
    def sql_virtual_machine_group_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_virtual_machine_group_resource_id", value)

    @property
    @pulumi.getter(name="sqlVirtualMachineName")
    def sql_virtual_machine_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SQL virtual machine.
        """
        return pulumi.get(self, "sql_virtual_machine_name")

    @sql_virtual_machine_name.setter
    def sql_virtual_machine_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_virtual_machine_name", value)

    @property
    @pulumi.getter(name="storageConfigurationSettings")
    def storage_configuration_settings(self) -> Optional[pulumi.Input['StorageConfigurationSettingsArgs']]:
        """
        Storage Configuration Settings.
        """
        return pulumi.get(self, "storage_configuration_settings")

    @storage_configuration_settings.setter
    def storage_configuration_settings(self, value: Optional[pulumi.Input['StorageConfigurationSettingsArgs']]):
        pulumi.set(self, "storage_configuration_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="virtualMachineResourceId")
    def virtual_machine_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM Resource id of underlying virtual machine created from SQL marketplace image.
        """
        return pulumi.get(self, "virtual_machine_resource_id")

    @virtual_machine_resource_id.setter
    def virtual_machine_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_machine_resource_id", value)

    @property
    @pulumi.getter(name="wsfcDomainCredentials")
    def wsfc_domain_credentials(self) -> Optional[pulumi.Input['WsfcDomainCredentialsArgs']]:
        """
        Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.
        """
        return pulumi.get(self, "wsfc_domain_credentials")

    @wsfc_domain_credentials.setter
    def wsfc_domain_credentials(self, value: Optional[pulumi.Input['WsfcDomainCredentialsArgs']]):
        pulumi.set(self, "wsfc_domain_credentials", value)


class SqlVirtualMachine(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_settings: Optional[pulumi.Input[pulumi.InputType['AssessmentSettingsArgs']]] = None,
                 auto_backup_settings: Optional[pulumi.Input[pulumi.InputType['AutoBackupSettingsArgs']]] = None,
                 auto_patching_settings: Optional[pulumi.Input[pulumi.InputType['AutoPatchingSettingsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 key_vault_credential_settings: Optional[pulumi.Input[pulumi.InputType['KeyVaultCredentialSettingsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_configurations_management_settings: Optional[pulumi.Input[pulumi.InputType['ServerConfigurationsManagementSettingsArgs']]] = None,
                 sql_image_offer: Optional[pulumi.Input[str]] = None,
                 sql_image_sku: Optional[pulumi.Input[Union[str, 'SqlImageSku']]] = None,
                 sql_management: Optional[pulumi.Input[Union[str, 'SqlManagementMode']]] = None,
                 sql_server_license_type: Optional[pulumi.Input[Union[str, 'SqlServerLicenseType']]] = None,
                 sql_virtual_machine_group_resource_id: Optional[pulumi.Input[str]] = None,
                 sql_virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 storage_configuration_settings: Optional[pulumi.Input[pulumi.InputType['StorageConfigurationSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_resource_id: Optional[pulumi.Input[str]] = None,
                 wsfc_domain_credentials: Optional[pulumi.Input[pulumi.InputType['WsfcDomainCredentialsArgs']]] = None,
                 __props__=None):
        """
        A SQL virtual machine.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AssessmentSettingsArgs']] assessment_settings: Assessment Settings.
        :param pulumi.Input[pulumi.InputType['AutoBackupSettingsArgs']] auto_backup_settings: Auto backup settings for SQL Server.
        :param pulumi.Input[pulumi.InputType['AutoPatchingSettingsArgs']] auto_patching_settings: Auto patching settings for applying critical security updates to SQL virtual machine.
        :param pulumi.Input[pulumi.InputType['ResourceIdentityArgs']] identity: Azure Active Directory identity of the server.
        :param pulumi.Input[pulumi.InputType['KeyVaultCredentialSettingsArgs']] key_vault_credential_settings: Key vault credential settings.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[pulumi.InputType['ServerConfigurationsManagementSettingsArgs']] server_configurations_management_settings: SQL Server configuration management settings.
        :param pulumi.Input[str] sql_image_offer: SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.
        :param pulumi.Input[Union[str, 'SqlImageSku']] sql_image_sku: SQL Server edition type.
        :param pulumi.Input[Union[str, 'SqlManagementMode']] sql_management: SQL Server Management type.
        :param pulumi.Input[Union[str, 'SqlServerLicenseType']] sql_server_license_type: SQL Server license type.
        :param pulumi.Input[str] sql_virtual_machine_group_resource_id: ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.
        :param pulumi.Input[str] sql_virtual_machine_name: Name of the SQL virtual machine.
        :param pulumi.Input[pulumi.InputType['StorageConfigurationSettingsArgs']] storage_configuration_settings: Storage Configuration Settings.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_machine_resource_id: ARM Resource id of underlying virtual machine created from SQL marketplace image.
        :param pulumi.Input[pulumi.InputType['WsfcDomainCredentialsArgs']] wsfc_domain_credentials: Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlVirtualMachineArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SQL virtual machine.

        :param str resource_name: The name of the resource.
        :param SqlVirtualMachineArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlVirtualMachineArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_settings: Optional[pulumi.Input[pulumi.InputType['AssessmentSettingsArgs']]] = None,
                 auto_backup_settings: Optional[pulumi.Input[pulumi.InputType['AutoBackupSettingsArgs']]] = None,
                 auto_patching_settings: Optional[pulumi.Input[pulumi.InputType['AutoPatchingSettingsArgs']]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 key_vault_credential_settings: Optional[pulumi.Input[pulumi.InputType['KeyVaultCredentialSettingsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_configurations_management_settings: Optional[pulumi.Input[pulumi.InputType['ServerConfigurationsManagementSettingsArgs']]] = None,
                 sql_image_offer: Optional[pulumi.Input[str]] = None,
                 sql_image_sku: Optional[pulumi.Input[Union[str, 'SqlImageSku']]] = None,
                 sql_management: Optional[pulumi.Input[Union[str, 'SqlManagementMode']]] = None,
                 sql_server_license_type: Optional[pulumi.Input[Union[str, 'SqlServerLicenseType']]] = None,
                 sql_virtual_machine_group_resource_id: Optional[pulumi.Input[str]] = None,
                 sql_virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 storage_configuration_settings: Optional[pulumi.Input[pulumi.InputType['StorageConfigurationSettingsArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_resource_id: Optional[pulumi.Input[str]] = None,
                 wsfc_domain_credentials: Optional[pulumi.Input[pulumi.InputType['WsfcDomainCredentialsArgs']]] = None,
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
            __props__ = SqlVirtualMachineArgs.__new__(SqlVirtualMachineArgs)

            __props__.__dict__["assessment_settings"] = assessment_settings
            __props__.__dict__["auto_backup_settings"] = auto_backup_settings
            __props__.__dict__["auto_patching_settings"] = auto_patching_settings
            __props__.__dict__["identity"] = identity
            __props__.__dict__["key_vault_credential_settings"] = key_vault_credential_settings
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["server_configurations_management_settings"] = server_configurations_management_settings
            __props__.__dict__["sql_image_offer"] = sql_image_offer
            __props__.__dict__["sql_image_sku"] = sql_image_sku
            __props__.__dict__["sql_management"] = sql_management
            __props__.__dict__["sql_server_license_type"] = sql_server_license_type
            __props__.__dict__["sql_virtual_machine_group_resource_id"] = sql_virtual_machine_group_resource_id
            __props__.__dict__["sql_virtual_machine_name"] = sql_virtual_machine_name
            __props__.__dict__["storage_configuration_settings"] = storage_configuration_settings
            __props__.__dict__["tags"] = tags
            __props__.__dict__["virtual_machine_resource_id"] = virtual_machine_resource_id
            __props__.__dict__["wsfc_domain_credentials"] = wsfc_domain_credentials
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sqlvirtualmachine:SqlVirtualMachine"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20170301preview:SqlVirtualMachine"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20220201:SqlVirtualMachine"), pulumi.Alias(type_="azure-native:sqlvirtualmachine/v20220201preview:SqlVirtualMachine")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlVirtualMachine, __self__).__init__(
            'azure-native:sqlvirtualmachine/v20211101preview:SqlVirtualMachine',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlVirtualMachine':
        """
        Get an existing SqlVirtualMachine resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlVirtualMachineArgs.__new__(SqlVirtualMachineArgs)

        __props__.__dict__["assessment_settings"] = None
        __props__.__dict__["auto_backup_settings"] = None
        __props__.__dict__["auto_patching_settings"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["key_vault_credential_settings"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["server_configurations_management_settings"] = None
        __props__.__dict__["sql_image_offer"] = None
        __props__.__dict__["sql_image_sku"] = None
        __props__.__dict__["sql_management"] = None
        __props__.__dict__["sql_server_license_type"] = None
        __props__.__dict__["sql_virtual_machine_group_resource_id"] = None
        __props__.__dict__["storage_configuration_settings"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machine_resource_id"] = None
        __props__.__dict__["wsfc_domain_credentials"] = None
        return SqlVirtualMachine(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assessmentSettings")
    def assessment_settings(self) -> pulumi.Output[Optional['outputs.AssessmentSettingsResponse']]:
        """
        Assessment Settings.
        """
        return pulumi.get(self, "assessment_settings")

    @property
    @pulumi.getter(name="autoBackupSettings")
    def auto_backup_settings(self) -> pulumi.Output[Optional['outputs.AutoBackupSettingsResponse']]:
        """
        Auto backup settings for SQL Server.
        """
        return pulumi.get(self, "auto_backup_settings")

    @property
    @pulumi.getter(name="autoPatchingSettings")
    def auto_patching_settings(self) -> pulumi.Output[Optional['outputs.AutoPatchingSettingsResponse']]:
        """
        Auto patching settings for applying critical security updates to SQL virtual machine.
        """
        return pulumi.get(self, "auto_patching_settings")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        """
        Azure Active Directory identity of the server.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="keyVaultCredentialSettings")
    def key_vault_credential_settings(self) -> pulumi.Output[Optional['outputs.KeyVaultCredentialSettingsResponse']]:
        """
        Key vault credential settings.
        """
        return pulumi.get(self, "key_vault_credential_settings")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state to track the async operation status.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serverConfigurationsManagementSettings")
    def server_configurations_management_settings(self) -> pulumi.Output[Optional['outputs.ServerConfigurationsManagementSettingsResponse']]:
        """
        SQL Server configuration management settings.
        """
        return pulumi.get(self, "server_configurations_management_settings")

    @property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> pulumi.Output[Optional[str]]:
        """
        SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016.
        """
        return pulumi.get(self, "sql_image_offer")

    @property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> pulumi.Output[Optional[str]]:
        """
        SQL Server edition type.
        """
        return pulumi.get(self, "sql_image_sku")

    @property
    @pulumi.getter(name="sqlManagement")
    def sql_management(self) -> pulumi.Output[Optional[str]]:
        """
        SQL Server Management type.
        """
        return pulumi.get(self, "sql_management")

    @property
    @pulumi.getter(name="sqlServerLicenseType")
    def sql_server_license_type(self) -> pulumi.Output[Optional[str]]:
        """
        SQL Server license type.
        """
        return pulumi.get(self, "sql_server_license_type")

    @property
    @pulumi.getter(name="sqlVirtualMachineGroupResourceId")
    def sql_virtual_machine_group_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of.
        """
        return pulumi.get(self, "sql_virtual_machine_group_resource_id")

    @property
    @pulumi.getter(name="storageConfigurationSettings")
    def storage_configuration_settings(self) -> pulumi.Output[Optional['outputs.StorageConfigurationSettingsResponse']]:
        """
        Storage Configuration Settings.
        """
        return pulumi.get(self, "storage_configuration_settings")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachineResourceId")
    def virtual_machine_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM Resource id of underlying virtual machine created from SQL marketplace image.
        """
        return pulumi.get(self, "virtual_machine_resource_id")

    @property
    @pulumi.getter(name="wsfcDomainCredentials")
    def wsfc_domain_credentials(self) -> pulumi.Output[Optional['outputs.WsfcDomainCredentialsResponse']]:
        """
        Domain credentials for setting up Windows Server Failover Cluster for SQL availability group.
        """
        return pulumi.get(self, "wsfc_domain_credentials")

