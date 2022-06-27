# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetPeeringServicePrefixResult',
    'AwaitableGetPeeringServicePrefixResult',
    'get_peering_service_prefix',
    'get_peering_service_prefix_output',
]

warnings.warn("""Version 2019-08-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetPeeringServicePrefixResult:
    """
    The peering service prefix class.
    """
    def __init__(__self__, id=None, learned_type=None, name=None, prefix=None, prefix_validation_state=None, provisioning_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if learned_type and not isinstance(learned_type, str):
            raise TypeError("Expected argument 'learned_type' to be a str")
        pulumi.set(__self__, "learned_type", learned_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prefix and not isinstance(prefix, str):
            raise TypeError("Expected argument 'prefix' to be a str")
        pulumi.set(__self__, "prefix", prefix)
        if prefix_validation_state and not isinstance(prefix_validation_state, str):
            raise TypeError("Expected argument 'prefix_validation_state' to be a str")
        pulumi.set(__self__, "prefix_validation_state", prefix_validation_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="learnedType")
    def learned_type(self) -> Optional[str]:
        """
        The prefix learned type
        """
        return pulumi.get(self, "learned_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        Valid route prefix
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="prefixValidationState")
    def prefix_validation_state(self) -> Optional[str]:
        """
        The prefix validation state
        """
        return pulumi.get(self, "prefix_validation_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetPeeringServicePrefixResult(GetPeeringServicePrefixResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPeeringServicePrefixResult(
            id=self.id,
            learned_type=self.learned_type,
            name=self.name,
            prefix=self.prefix,
            prefix_validation_state=self.prefix_validation_state,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_peering_service_prefix(peering_service_name: Optional[str] = None,
                               prefix_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPeeringServicePrefixResult:
    """
    The peering service prefix class.


    :param str peering_service_name: The peering service name.
    :param str prefix_name: The prefix name.
    :param str resource_group_name: The resource group name.
    """
    pulumi.log.warn("""get_peering_service_prefix is deprecated: Version 2019-08-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['peeringServiceName'] = peering_service_name
    __args__['prefixName'] = prefix_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:peering/v20190801preview:getPeeringServicePrefix', __args__, opts=opts, typ=GetPeeringServicePrefixResult).value

    return AwaitableGetPeeringServicePrefixResult(
        id=__ret__.id,
        learned_type=__ret__.learned_type,
        name=__ret__.name,
        prefix=__ret__.prefix,
        prefix_validation_state=__ret__.prefix_validation_state,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_peering_service_prefix)
def get_peering_service_prefix_output(peering_service_name: Optional[pulumi.Input[str]] = None,
                                      prefix_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPeeringServicePrefixResult]:
    """
    The peering service prefix class.


    :param str peering_service_name: The peering service name.
    :param str prefix_name: The prefix name.
    :param str resource_group_name: The resource group name.
    """
    pulumi.log.warn("""get_peering_service_prefix is deprecated: Version 2019-08-01-preview will be removed in v2 of the provider.""")
    ...
