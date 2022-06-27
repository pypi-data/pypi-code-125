# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ScheduledTriggerArgs', 'ScheduledTrigger']

@pulumi.input_type
class ScheduledTriggerArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 recurrence_interval: pulumi.Input[Union[str, 'RecurrenceInterval']],
                 resource_group_name: pulumi.Input[str],
                 share_subscription_name: pulumi.Input[str],
                 synchronization_time: pulumi.Input[str],
                 synchronization_mode: Optional[pulumi.Input[Union[str, 'SynchronizationMode']]] = None,
                 trigger_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScheduledTrigger resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] kind: Kind of synchronization on trigger.
               Expected value is 'ScheduleBased'.
        :param pulumi.Input[Union[str, 'RecurrenceInterval']] recurrence_interval: Recurrence Interval
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[str] synchronization_time: Synchronization time
        :param pulumi.Input[Union[str, 'SynchronizationMode']] synchronization_mode: Synchronization mode
        :param pulumi.Input[str] trigger_name: The name of the trigger.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "kind", 'ScheduleBased')
        pulumi.set(__self__, "recurrence_interval", recurrence_interval)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "share_subscription_name", share_subscription_name)
        pulumi.set(__self__, "synchronization_time", synchronization_time)
        if synchronization_mode is not None:
            pulumi.set(__self__, "synchronization_mode", synchronization_mode)
        if trigger_name is not None:
            pulumi.set(__self__, "trigger_name", trigger_name)

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
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of synchronization on trigger.
        Expected value is 'ScheduleBased'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(self) -> pulumi.Input[Union[str, 'RecurrenceInterval']]:
        """
        Recurrence Interval
        """
        return pulumi.get(self, "recurrence_interval")

    @recurrence_interval.setter
    def recurrence_interval(self, value: pulumi.Input[Union[str, 'RecurrenceInterval']]):
        pulumi.set(self, "recurrence_interval", value)

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
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> pulumi.Input[str]:
        """
        Synchronization time
        """
        return pulumi.get(self, "synchronization_time")

    @synchronization_time.setter
    def synchronization_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "synchronization_time", value)

    @property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> Optional[pulumi.Input[Union[str, 'SynchronizationMode']]]:
        """
        Synchronization mode
        """
        return pulumi.get(self, "synchronization_mode")

    @synchronization_mode.setter
    def synchronization_mode(self, value: Optional[pulumi.Input[Union[str, 'SynchronizationMode']]]):
        pulumi.set(self, "synchronization_mode", value)

    @property
    @pulumi.getter(name="triggerName")
    def trigger_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the trigger.
        """
        return pulumi.get(self, "trigger_name")

    @trigger_name.setter
    def trigger_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "trigger_name", value)


class ScheduledTrigger(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 recurrence_interval: Optional[pulumi.Input[Union[str, 'RecurrenceInterval']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 synchronization_mode: Optional[pulumi.Input[Union[str, 'SynchronizationMode']]] = None,
                 synchronization_time: Optional[pulumi.Input[str]] = None,
                 trigger_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A type of trigger based on schedule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the share account.
        :param pulumi.Input[str] kind: Kind of synchronization on trigger.
               Expected value is 'ScheduleBased'.
        :param pulumi.Input[Union[str, 'RecurrenceInterval']] recurrence_interval: Recurrence Interval
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] share_subscription_name: The name of the share subscription which will hold the data set sink.
        :param pulumi.Input[Union[str, 'SynchronizationMode']] synchronization_mode: Synchronization mode
        :param pulumi.Input[str] synchronization_time: Synchronization time
        :param pulumi.Input[str] trigger_name: The name of the trigger.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledTriggerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A type of trigger based on schedule

        :param str resource_name: The name of the resource.
        :param ScheduledTriggerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledTriggerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 recurrence_interval: Optional[pulumi.Input[Union[str, 'RecurrenceInterval']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                 synchronization_mode: Optional[pulumi.Input[Union[str, 'SynchronizationMode']]] = None,
                 synchronization_time: Optional[pulumi.Input[str]] = None,
                 trigger_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ScheduledTriggerArgs.__new__(ScheduledTriggerArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'ScheduleBased'
            if recurrence_interval is None and not opts.urn:
                raise TypeError("Missing required property 'recurrence_interval'")
            __props__.__dict__["recurrence_interval"] = recurrence_interval
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if share_subscription_name is None and not opts.urn:
                raise TypeError("Missing required property 'share_subscription_name'")
            __props__.__dict__["share_subscription_name"] = share_subscription_name
            __props__.__dict__["synchronization_mode"] = synchronization_mode
            if synchronization_time is None and not opts.urn:
                raise TypeError("Missing required property 'synchronization_time'")
            __props__.__dict__["synchronization_time"] = synchronization_time
            __props__.__dict__["trigger_name"] = trigger_name
            __props__.__dict__["created_at"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["trigger_status"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["user_name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datashare:ScheduledTrigger"), pulumi.Alias(type_="azure-native:datashare/v20191101:ScheduledTrigger"), pulumi.Alias(type_="azure-native:datashare/v20200901:ScheduledTrigger"), pulumi.Alias(type_="azure-native:datashare/v20201001preview:ScheduledTrigger"), pulumi.Alias(type_="azure-native:datashare/v20210801:ScheduledTrigger")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScheduledTrigger, __self__).__init__(
            'azure-native:datashare/v20181101preview:ScheduledTrigger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduledTrigger':
        """
        Get an existing ScheduledTrigger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduledTriggerArgs.__new__(ScheduledTriggerArgs)

        __props__.__dict__["created_at"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["recurrence_interval"] = None
        __props__.__dict__["synchronization_mode"] = None
        __props__.__dict__["synchronization_time"] = None
        __props__.__dict__["trigger_status"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_name"] = None
        return ScheduledTrigger(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Time at which the trigger was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of synchronization on trigger.
        Expected value is 'ScheduleBased'.
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
        Gets the provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="recurrenceInterval")
    def recurrence_interval(self) -> pulumi.Output[str]:
        """
        Recurrence Interval
        """
        return pulumi.get(self, "recurrence_interval")

    @property
    @pulumi.getter(name="synchronizationMode")
    def synchronization_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Synchronization mode
        """
        return pulumi.get(self, "synchronization_mode")

    @property
    @pulumi.getter(name="synchronizationTime")
    def synchronization_time(self) -> pulumi.Output[str]:
        """
        Synchronization time
        """
        return pulumi.get(self, "synchronization_time")

    @property
    @pulumi.getter(name="triggerStatus")
    def trigger_status(self) -> pulumi.Output[str]:
        """
        Gets the trigger state
        """
        return pulumi.get(self, "trigger_status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Name of the user who created the trigger.
        """
        return pulumi.get(self, "user_name")

