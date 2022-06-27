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

__all__ = ['EncryptionScopeArgs', 'EncryptionScope']

@pulumi.input_type
class EncryptionScopeArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 encryption_scope_name: Optional[pulumi.Input[str]] = None,
                 key_vault_properties: Optional[pulumi.Input['EncryptionScopeKeyVaultPropertiesArgs']] = None,
                 require_infrastructure_encryption: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[Union[str, 'EncryptionScopeSource']]] = None,
                 state: Optional[pulumi.Input[Union[str, 'EncryptionScopeState']]] = None):
        """
        The set of arguments for constructing a EncryptionScope resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[str] encryption_scope_name: The name of the encryption scope within the specified storage account. Encryption scope names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        :param pulumi.Input['EncryptionScopeKeyVaultPropertiesArgs'] key_vault_properties: The key vault properties for the encryption scope. This is a required field if encryption scope 'source' attribute is set to 'Microsoft.KeyVault'.
        :param pulumi.Input[bool] require_infrastructure_encryption: A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.
        :param pulumi.Input[Union[str, 'EncryptionScopeSource']] source: The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
        :param pulumi.Input[Union[str, 'EncryptionScopeState']] state: The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if encryption_scope_name is not None:
            pulumi.set(__self__, "encryption_scope_name", encryption_scope_name)
        if key_vault_properties is not None:
            pulumi.set(__self__, "key_vault_properties", key_vault_properties)
        if require_infrastructure_encryption is not None:
            pulumi.set(__self__, "require_infrastructure_encryption", require_infrastructure_encryption)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="encryptionScopeName")
    def encryption_scope_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the encryption scope within the specified storage account. Encryption scope names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        """
        return pulumi.get(self, "encryption_scope_name")

    @encryption_scope_name.setter
    def encryption_scope_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_scope_name", value)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input['EncryptionScopeKeyVaultPropertiesArgs']]:
        """
        The key vault properties for the encryption scope. This is a required field if encryption scope 'source' attribute is set to 'Microsoft.KeyVault'.
        """
        return pulumi.get(self, "key_vault_properties")

    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input['EncryptionScopeKeyVaultPropertiesArgs']]):
        pulumi.set(self, "key_vault_properties", value)

    @property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(self) -> Optional[pulumi.Input[bool]]:
        """
        A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.
        """
        return pulumi.get(self, "require_infrastructure_encryption")

    @require_infrastructure_encryption.setter
    def require_infrastructure_encryption(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "require_infrastructure_encryption", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[Union[str, 'EncryptionScopeSource']]]:
        """
        The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[Union[str, 'EncryptionScopeSource']]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'EncryptionScopeState']]]:
        """
        The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'EncryptionScopeState']]]):
        pulumi.set(self, "state", value)


class EncryptionScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 encryption_scope_name: Optional[pulumi.Input[str]] = None,
                 key_vault_properties: Optional[pulumi.Input[pulumi.InputType['EncryptionScopeKeyVaultPropertiesArgs']]] = None,
                 require_infrastructure_encryption: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[str, 'EncryptionScopeSource']]] = None,
                 state: Optional[pulumi.Input[Union[str, 'EncryptionScopeState']]] = None,
                 __props__=None):
        """
        The Encryption Scope resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
        :param pulumi.Input[str] encryption_scope_name: The name of the encryption scope within the specified storage account. Encryption scope names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
        :param pulumi.Input[pulumi.InputType['EncryptionScopeKeyVaultPropertiesArgs']] key_vault_properties: The key vault properties for the encryption scope. This is a required field if encryption scope 'source' attribute is set to 'Microsoft.KeyVault'.
        :param pulumi.Input[bool] require_infrastructure_encryption: A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
        :param pulumi.Input[Union[str, 'EncryptionScopeSource']] source: The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
        :param pulumi.Input[Union[str, 'EncryptionScopeState']] state: The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EncryptionScopeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Encryption Scope resource.

        :param str resource_name: The name of the resource.
        :param EncryptionScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EncryptionScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 encryption_scope_name: Optional[pulumi.Input[str]] = None,
                 key_vault_properties: Optional[pulumi.Input[pulumi.InputType['EncryptionScopeKeyVaultPropertiesArgs']]] = None,
                 require_infrastructure_encryption: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[str, 'EncryptionScopeSource']]] = None,
                 state: Optional[pulumi.Input[Union[str, 'EncryptionScopeState']]] = None,
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
            __props__ = EncryptionScopeArgs.__new__(EncryptionScopeArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["encryption_scope_name"] = encryption_scope_name
            __props__.__dict__["key_vault_properties"] = key_vault_properties
            __props__.__dict__["require_infrastructure_encryption"] = require_infrastructure_encryption
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source"] = source
            __props__.__dict__["state"] = state
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20190601:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20200801preview:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20210101:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20210401:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20210601:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20210801:EncryptionScope"), pulumi.Alias(type_="azure-native:storage/v20210901:EncryptionScope")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EncryptionScope, __self__).__init__(
            'azure-native:storage/v20210201:EncryptionScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EncryptionScope':
        """
        Get an existing EncryptionScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EncryptionScopeArgs.__new__(EncryptionScopeArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["key_vault_properties"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["require_infrastructure_encryption"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["type"] = None
        return EncryptionScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Gets the creation date and time of the encryption scope in UTC.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> pulumi.Output[Optional['outputs.EncryptionScopeKeyVaultPropertiesResponse']]:
        """
        The key vault properties for the encryption scope. This is a required field if encryption scope 'source' attribute is set to 'Microsoft.KeyVault'.
        """
        return pulumi.get(self, "key_vault_properties")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        Gets the last modification date and time of the encryption scope in UTC.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requireInfrastructureEncryption")
    def require_infrastructure_encryption(self) -> pulumi.Output[Optional[bool]]:
        """
        A boolean indicating whether or not the service applies a secondary layer of encryption with platform managed keys for data at rest.
        """
        return pulumi.get(self, "require_infrastructure_encryption")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

