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
    'GetDiagnosticSettingResult',
    'AwaitableGetDiagnosticSettingResult',
    'get_diagnostic_setting',
    'get_diagnostic_setting_output',
]

@pulumi.output_type
class GetDiagnosticSettingResult:
    """
    The diagnostic setting resource.
    """
    def __init__(__self__, event_hub_authorization_rule_id=None, event_hub_name=None, id=None, log_analytics_destination_type=None, logs=None, metrics=None, name=None, service_bus_rule_id=None, storage_account_id=None, type=None, workspace_id=None):
        if event_hub_authorization_rule_id and not isinstance(event_hub_authorization_rule_id, str):
            raise TypeError("Expected argument 'event_hub_authorization_rule_id' to be a str")
        pulumi.set(__self__, "event_hub_authorization_rule_id", event_hub_authorization_rule_id)
        if event_hub_name and not isinstance(event_hub_name, str):
            raise TypeError("Expected argument 'event_hub_name' to be a str")
        pulumi.set(__self__, "event_hub_name", event_hub_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if log_analytics_destination_type and not isinstance(log_analytics_destination_type, str):
            raise TypeError("Expected argument 'log_analytics_destination_type' to be a str")
        pulumi.set(__self__, "log_analytics_destination_type", log_analytics_destination_type)
        if logs and not isinstance(logs, list):
            raise TypeError("Expected argument 'logs' to be a list")
        pulumi.set(__self__, "logs", logs)
        if metrics and not isinstance(metrics, list):
            raise TypeError("Expected argument 'metrics' to be a list")
        pulumi.set(__self__, "metrics", metrics)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if service_bus_rule_id and not isinstance(service_bus_rule_id, str):
            raise TypeError("Expected argument 'service_bus_rule_id' to be a str")
        pulumi.set(__self__, "service_bus_rule_id", service_bus_rule_id)
        if storage_account_id and not isinstance(storage_account_id, str):
            raise TypeError("Expected argument 'storage_account_id' to be a str")
        pulumi.set(__self__, "storage_account_id", storage_account_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if workspace_id and not isinstance(workspace_id, str):
            raise TypeError("Expected argument 'workspace_id' to be a str")
        pulumi.set(__self__, "workspace_id", workspace_id)

    @property
    @pulumi.getter(name="eventHubAuthorizationRuleId")
    def event_hub_authorization_rule_id(self) -> Optional[str]:
        """
        The resource Id for the event hub authorization rule.
        """
        return pulumi.get(self, "event_hub_authorization_rule_id")

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[str]:
        """
        The name of the event hub. If none is specified, the default event hub will be selected.
        """
        return pulumi.get(self, "event_hub_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logAnalyticsDestinationType")
    def log_analytics_destination_type(self) -> Optional[str]:
        """
        A string indicating whether the export to Log Analytics should use the default destination type, i.e. AzureDiagnostics, or use a destination type constructed as follows: <normalized service identity>_<normalized category name>. Possible values are: Dedicated and null (null is default.)
        """
        return pulumi.get(self, "log_analytics_destination_type")

    @property
    @pulumi.getter
    def logs(self) -> Optional[Sequence['outputs.LogSettingsResponse']]:
        """
        The list of logs settings.
        """
        return pulumi.get(self, "logs")

    @property
    @pulumi.getter
    def metrics(self) -> Optional[Sequence['outputs.MetricSettingsResponse']]:
        """
        The list of metric settings.
        """
        return pulumi.get(self, "metrics")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceBusRuleId")
    def service_bus_rule_id(self) -> Optional[str]:
        """
        The service bus rule Id of the diagnostic setting. This is here to maintain backwards compatibility.
        """
        return pulumi.get(self, "service_bus_rule_id")

    @property
    @pulumi.getter(name="storageAccountId")
    def storage_account_id(self) -> Optional[str]:
        """
        The resource ID of the storage account to which you would like to send Diagnostic Logs.
        """
        return pulumi.get(self, "storage_account_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[str]:
        """
        The full ARM resource ID of the Log Analytics workspace to which you would like to send Diagnostic Logs. Example: /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
        """
        return pulumi.get(self, "workspace_id")


class AwaitableGetDiagnosticSettingResult(GetDiagnosticSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiagnosticSettingResult(
            event_hub_authorization_rule_id=self.event_hub_authorization_rule_id,
            event_hub_name=self.event_hub_name,
            id=self.id,
            log_analytics_destination_type=self.log_analytics_destination_type,
            logs=self.logs,
            metrics=self.metrics,
            name=self.name,
            service_bus_rule_id=self.service_bus_rule_id,
            storage_account_id=self.storage_account_id,
            type=self.type,
            workspace_id=self.workspace_id)


def get_diagnostic_setting(name: Optional[str] = None,
                           resource_uri: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiagnosticSettingResult:
    """
    The diagnostic setting resource.


    :param str name: The name of the diagnostic setting.
    :param str resource_uri: The identifier of the resource.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceUri'] = resource_uri
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20170501preview:getDiagnosticSetting', __args__, opts=opts, typ=GetDiagnosticSettingResult).value

    return AwaitableGetDiagnosticSettingResult(
        event_hub_authorization_rule_id=__ret__.event_hub_authorization_rule_id,
        event_hub_name=__ret__.event_hub_name,
        id=__ret__.id,
        log_analytics_destination_type=__ret__.log_analytics_destination_type,
        logs=__ret__.logs,
        metrics=__ret__.metrics,
        name=__ret__.name,
        service_bus_rule_id=__ret__.service_bus_rule_id,
        storage_account_id=__ret__.storage_account_id,
        type=__ret__.type,
        workspace_id=__ret__.workspace_id)


@_utilities.lift_output_func(get_diagnostic_setting)
def get_diagnostic_setting_output(name: Optional[pulumi.Input[str]] = None,
                                  resource_uri: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiagnosticSettingResult]:
    """
    The diagnostic setting resource.


    :param str name: The name of the diagnostic setting.
    :param str resource_uri: The identifier of the resource.
    """
    ...
