# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ChannelName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    ALEXA_CHANNEL = "AlexaChannel"
    FACEBOOK_CHANNEL = "FacebookChannel"
    EMAIL_CHANNEL = "EmailChannel"
    KIK_CHANNEL = "KikChannel"
    TELEGRAM_CHANNEL = "TelegramChannel"
    SLACK_CHANNEL = "SlackChannel"
    MS_TEAMS_CHANNEL = "MsTeamsChannel"
    SKYPE_CHANNEL = "SkypeChannel"
    WEB_CHAT_CHANNEL = "WebChatChannel"
    DIRECT_LINE_CHANNEL = "DirectLineChannel"
    SMS_CHANNEL = "SmsChannel"
    LINE_CHANNEL = "LineChannel"
    DIRECT_LINE_SPEECH_CHANNEL = "DirectLineSpeechChannel"
    OUTLOOK_CHANNEL = "OutlookChannel"

class Key(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Determines which key is to be regenerated
    """

    KEY1 = "key1"
    KEY2 = "key2"

class Kind(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the type of bot service
    """

    SDK = "sdk"
    DESIGNER = "designer"
    BOT = "bot"
    FUNCTION = "function"
    AZUREBOT = "azurebot"

class MsaAppType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Microsoft App Type for the bot
    """

    USER_ASSIGNED_MSI = "UserAssignedMSI"
    SINGLE_TENANT = "SingleTenant"
    MULTI_TENANT = "MultiTenant"

class OperationResultStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the operation being performed.
    """

    CANCELED = "Canceled"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    REQUESTED = "Requested"
    RUNNING = "Running"

class PrivateEndpointConnectionProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"

class PrivateEndpointServiceConnectionStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The private endpoint connection status.
    """

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class PublicNetworkAccess(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Whether the bot is in an isolated network
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class RegenerateKeysChannelName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    WEB_CHAT_CHANNEL = "WebChatChannel"
    DIRECT_LINE_CHANNEL = "DirectLineChannel"

class SkuName(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The name of SKU.
    """

    F0 = "F0"
    S1 = "S1"

class SkuTier(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Gets the sku tier. This is based on the SKU name.
    """

    FREE = "Free"
    STANDARD = "Standard"
