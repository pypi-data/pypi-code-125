# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 access_control_record_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 device_name: pulumi.Input[str],
                 manager_name: pulumi.Input[str],
                 monitoring_status: pulumi.Input['MonitoringStatus'],
                 resource_group_name: pulumi.Input[str],
                 size_in_bytes: pulumi.Input[float],
                 volume_container_name: pulumi.Input[str],
                 volume_status: pulumi.Input['VolumeStatus'],
                 volume_type: pulumi.Input['VolumeType'],
                 kind: Optional[pulumi.Input['Kind']] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_control_record_ids: The IDs of the access control records, associated with the volume.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input['MonitoringStatus'] monitoring_status: The monitoring status of the volume.
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[float] size_in_bytes: The size of the volume in bytes.
        :param pulumi.Input[str] volume_container_name: The volume container name.
        :param pulumi.Input['VolumeStatus'] volume_status: The volume status.
        :param pulumi.Input['VolumeType'] volume_type: The type of the volume.
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] volume_name: The volume name.
        """
        pulumi.set(__self__, "access_control_record_ids", access_control_record_ids)
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "manager_name", manager_name)
        pulumi.set(__self__, "monitoring_status", monitoring_status)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        pulumi.set(__self__, "volume_container_name", volume_container_name)
        pulumi.set(__self__, "volume_status", volume_status)
        pulumi.set(__self__, "volume_type", volume_type)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter(name="accessControlRecordIds")
    def access_control_record_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The IDs of the access control records, associated with the volume.
        """
        return pulumi.get(self, "access_control_record_ids")

    @access_control_record_ids.setter
    def access_control_record_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "access_control_record_ids", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="managerName")
    def manager_name(self) -> pulumi.Input[str]:
        """
        The manager name
        """
        return pulumi.get(self, "manager_name")

    @manager_name.setter
    def manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "manager_name", value)

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> pulumi.Input['MonitoringStatus']:
        """
        The monitoring status of the volume.
        """
        return pulumi.get(self, "monitoring_status")

    @monitoring_status.setter
    def monitoring_status(self, value: pulumi.Input['MonitoringStatus']):
        pulumi.set(self, "monitoring_status", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Input[float]:
        """
        The size of the volume in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @size_in_bytes.setter
    def size_in_bytes(self, value: pulumi.Input[float]):
        pulumi.set(self, "size_in_bytes", value)

    @property
    @pulumi.getter(name="volumeContainerName")
    def volume_container_name(self) -> pulumi.Input[str]:
        """
        The volume container name.
        """
        return pulumi.get(self, "volume_container_name")

    @volume_container_name.setter
    def volume_container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_container_name", value)

    @property
    @pulumi.getter(name="volumeStatus")
    def volume_status(self) -> pulumi.Input['VolumeStatus']:
        """
        The volume status.
        """
        return pulumi.get(self, "volume_status")

    @volume_status.setter
    def volume_status(self, value: pulumi.Input['VolumeStatus']):
        pulumi.set(self, "volume_status", value)

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Input['VolumeType']:
        """
        The type of the volume.
        """
        return pulumi.get(self, "volume_type")

    @volume_type.setter
    def volume_type(self, value: pulumi.Input['VolumeType']):
        pulumi.set(self, "volume_type", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input['Kind']]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input['Kind']]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The volume name.
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


class Volume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control_record_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 monitoring_status: Optional[pulumi.Input['MonitoringStatus']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size_in_bytes: Optional[pulumi.Input[float]] = None,
                 volume_container_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_status: Optional[pulumi.Input['VolumeStatus']] = None,
                 volume_type: Optional[pulumi.Input['VolumeType']] = None,
                 __props__=None):
        """
        The volume.
        API Version: 2017-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] access_control_record_ids: The IDs of the access control records, associated with the volume.
        :param pulumi.Input[str] device_name: The device name
        :param pulumi.Input['Kind'] kind: The Kind of the object. Currently only Series8000 is supported
        :param pulumi.Input[str] manager_name: The manager name
        :param pulumi.Input['MonitoringStatus'] monitoring_status: The monitoring status of the volume.
        :param pulumi.Input[str] resource_group_name: The resource group name
        :param pulumi.Input[float] size_in_bytes: The size of the volume in bytes.
        :param pulumi.Input[str] volume_container_name: The volume container name.
        :param pulumi.Input[str] volume_name: The volume name.
        :param pulumi.Input['VolumeStatus'] volume_status: The volume status.
        :param pulumi.Input['VolumeType'] volume_type: The type of the volume.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The volume.
        API Version: 2017-06-01.

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_control_record_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input['Kind']] = None,
                 manager_name: Optional[pulumi.Input[str]] = None,
                 monitoring_status: Optional[pulumi.Input['MonitoringStatus']] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size_in_bytes: Optional[pulumi.Input[float]] = None,
                 volume_container_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 volume_status: Optional[pulumi.Input['VolumeStatus']] = None,
                 volume_type: Optional[pulumi.Input['VolumeType']] = None,
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
            __props__ = VolumeArgs.__new__(VolumeArgs)

            if access_control_record_ids is None and not opts.urn:
                raise TypeError("Missing required property 'access_control_record_ids'")
            __props__.__dict__["access_control_record_ids"] = access_control_record_ids
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            __props__.__dict__["kind"] = kind
            if manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'manager_name'")
            __props__.__dict__["manager_name"] = manager_name
            if monitoring_status is None and not opts.urn:
                raise TypeError("Missing required property 'monitoring_status'")
            __props__.__dict__["monitoring_status"] = monitoring_status
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if size_in_bytes is None and not opts.urn:
                raise TypeError("Missing required property 'size_in_bytes'")
            __props__.__dict__["size_in_bytes"] = size_in_bytes
            if volume_container_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_container_name'")
            __props__.__dict__["volume_container_name"] = volume_container_name
            __props__.__dict__["volume_name"] = volume_name
            if volume_status is None and not opts.urn:
                raise TypeError("Missing required property 'volume_status'")
            __props__.__dict__["volume_status"] = volume_status
            if volume_type is None and not opts.urn:
                raise TypeError("Missing required property 'volume_type'")
            __props__.__dict__["volume_type"] = volume_type
            __props__.__dict__["backup_policy_ids"] = None
            __props__.__dict__["backup_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["operation_status"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["volume_container_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storsimple/v20170601:Volume")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Volume, __self__).__init__(
            'azure-native:storsimple:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeArgs.__new__(VolumeArgs)

        __props__.__dict__["access_control_record_ids"] = None
        __props__.__dict__["backup_policy_ids"] = None
        __props__.__dict__["backup_status"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["monitoring_status"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation_status"] = None
        __props__.__dict__["size_in_bytes"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["volume_container_id"] = None
        __props__.__dict__["volume_status"] = None
        __props__.__dict__["volume_type"] = None
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessControlRecordIds")
    def access_control_record_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The IDs of the access control records, associated with the volume.
        """
        return pulumi.get(self, "access_control_record_ids")

    @property
    @pulumi.getter(name="backupPolicyIds")
    def backup_policy_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The IDs of the backup policies, in which this volume is part of.
        """
        return pulumi.get(self, "backup_policy_ids")

    @property
    @pulumi.getter(name="backupStatus")
    def backup_status(self) -> pulumi.Output[str]:
        """
        The backup status of the volume.
        """
        return pulumi.get(self, "backup_status")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> pulumi.Output[str]:
        """
        The monitoring status of the volume.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationStatus")
    def operation_status(self) -> pulumi.Output[str]:
        """
        The operation status on the volume.
        """
        return pulumi.get(self, "operation_status")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[float]:
        """
        The size of the volume in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeContainerId")
    def volume_container_id(self) -> pulumi.Output[str]:
        """
        The ID of the volume container, in which this volume is created.
        """
        return pulumi.get(self, "volume_container_id")

    @property
    @pulumi.getter(name="volumeStatus")
    def volume_status(self) -> pulumi.Output[str]:
        """
        The volume status.
        """
        return pulumi.get(self, "volume_status")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> pulumi.Output[str]:
        """
        The type of the volume.
        """
        return pulumi.get(self, "volume_type")

