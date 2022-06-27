# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAppServiceCertificateOrderCertificateResult',
    'AwaitableGetAppServiceCertificateOrderCertificateResult',
    'get_app_service_certificate_order_certificate',
    'get_app_service_certificate_order_certificate_output',
]

warnings.warn("""Version 2019-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetAppServiceCertificateOrderCertificateResult:
    """
    Key Vault container ARM resource for a certificate that is purchased through Azure.
    """
    def __init__(__self__, id=None, key_vault_id=None, key_vault_secret_name=None, kind=None, location=None, name=None, provisioning_state=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_id and not isinstance(key_vault_id, str):
            raise TypeError("Expected argument 'key_vault_id' to be a str")
        pulumi.set(__self__, "key_vault_id", key_vault_id)
        if key_vault_secret_name and not isinstance(key_vault_secret_name, str):
            raise TypeError("Expected argument 'key_vault_secret_name' to be a str")
        pulumi.set(__self__, "key_vault_secret_name", key_vault_secret_name)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
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
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[str]:
        """
        Key Vault resource Id.
        """
        return pulumi.get(self, "key_vault_id")

    @property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> Optional[str]:
        """
        Key Vault secret name.
        """
        return pulumi.get(self, "key_vault_secret_name")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Status of the Key Vault secret.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetAppServiceCertificateOrderCertificateResult(GetAppServiceCertificateOrderCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppServiceCertificateOrderCertificateResult(
            id=self.id,
            key_vault_id=self.key_vault_id,
            key_vault_secret_name=self.key_vault_secret_name,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_app_service_certificate_order_certificate(certificate_order_name: Optional[str] = None,
                                                  name: Optional[str] = None,
                                                  resource_group_name: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppServiceCertificateOrderCertificateResult:
    """
    Key Vault container ARM resource for a certificate that is purchased through Azure.


    :param str certificate_order_name: Name of the certificate order.
    :param str name: Name of the certificate.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    pulumi.log.warn("""get_app_service_certificate_order_certificate is deprecated: Version 2019-08-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['certificateOrderName'] = certificate_order_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:certificateregistration/v20190801:getAppServiceCertificateOrderCertificate', __args__, opts=opts, typ=GetAppServiceCertificateOrderCertificateResult).value

    return AwaitableGetAppServiceCertificateOrderCertificateResult(
        id=__ret__.id,
        key_vault_id=__ret__.key_vault_id,
        key_vault_secret_name=__ret__.key_vault_secret_name,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_app_service_certificate_order_certificate)
def get_app_service_certificate_order_certificate_output(certificate_order_name: Optional[pulumi.Input[str]] = None,
                                                         name: Optional[pulumi.Input[str]] = None,
                                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppServiceCertificateOrderCertificateResult]:
    """
    Key Vault container ARM resource for a certificate that is purchased through Azure.


    :param str certificate_order_name: Name of the certificate order.
    :param str name: Name of the certificate.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    pulumi.log.warn("""get_app_service_certificate_order_certificate is deprecated: Version 2019-08-01 will be removed in v2 of the provider.""")
    ...
