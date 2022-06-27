# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ActionType',
    'AlertDetail',
    'AlertRuleKind',
    'AlertSeverity',
    'AttackTactic',
    'AutomationRulePropertyConditionSupportedOperator',
    'AutomationRulePropertyConditionSupportedProperty',
    'ConditionType',
    'DataConnectorKind',
    'DataTypeState',
    'EntityMappingType',
    'EventGroupingAggregationKind',
    'IncidentClassification',
    'IncidentClassificationReason',
    'IncidentSeverity',
    'IncidentStatus',
    'MatchingMethod',
    'MicrosoftSecurityProductName',
    'OwnerType',
    'Source',
    'ThreatIntelligenceResourceInnerKind',
    'TriggerOperator',
    'TriggersOn',
    'TriggersWhen',
]


class ActionType(str, Enum):
    """
    The type of the automation rule action
    """
    MODIFY_PROPERTIES = "ModifyProperties"
    """
    Modify an object's properties
    """
    RUN_PLAYBOOK = "RunPlaybook"
    """
    Run a playbook on an object
    """


class AlertDetail(str, Enum):
    """
    Alert detail
    """
    DISPLAY_NAME = "DisplayName"
    """
    Alert display name
    """
    SEVERITY = "Severity"
    """
    Alert severity
    """


class AlertRuleKind(str, Enum):
    """
    The alert rule kind
    """
    SCHEDULED = "Scheduled"
    MICROSOFT_SECURITY_INCIDENT_CREATION = "MicrosoftSecurityIncidentCreation"
    FUSION = "Fusion"


class AlertSeverity(str, Enum):
    """
    The severity for alerts created by this alert rule.
    """
    HIGH = "High"
    """
    High severity
    """
    MEDIUM = "Medium"
    """
    Medium severity
    """
    LOW = "Low"
    """
    Low severity
    """
    INFORMATIONAL = "Informational"
    """
    Informational severity
    """


class AttackTactic(str, Enum):
    """
    The severity for alerts created by this alert rule.
    """
    INITIAL_ACCESS = "InitialAccess"
    EXECUTION = "Execution"
    PERSISTENCE = "Persistence"
    PRIVILEGE_ESCALATION = "PrivilegeEscalation"
    DEFENSE_EVASION = "DefenseEvasion"
    CREDENTIAL_ACCESS = "CredentialAccess"
    DISCOVERY = "Discovery"
    LATERAL_MOVEMENT = "LateralMovement"
    COLLECTION = "Collection"
    EXFILTRATION = "Exfiltration"
    COMMAND_AND_CONTROL = "CommandAndControl"
    IMPACT = "Impact"
    PRE_ATTACK = "PreAttack"


class AutomationRulePropertyConditionSupportedOperator(str, Enum):
    EQUALS = "Equals"
    """
    Evaluates if the property equals at least one of the condition values
    """
    NOT_EQUALS = "NotEquals"
    """
    Evaluates if the property does not equal any of the condition values
    """
    CONTAINS = "Contains"
    """
    Evaluates if the property contains at least one of the condition values
    """
    NOT_CONTAINS = "NotContains"
    """
    Evaluates if the property does not contain any of the condition values
    """
    STARTS_WITH = "StartsWith"
    """
    Evaluates if the property starts with any of the condition values
    """
    NOT_STARTS_WITH = "NotStartsWith"
    """
    Evaluates if the property does not start with any of the condition values
    """
    ENDS_WITH = "EndsWith"
    """
    Evaluates if the property ends with any of the condition values
    """
    NOT_ENDS_WITH = "NotEndsWith"
    """
    Evaluates if the property does not end with any of the condition values
    """


class AutomationRulePropertyConditionSupportedProperty(str, Enum):
    """
    The property to evaluate in an automation rule property condition
    """
    INCIDENT_TITLE = "IncidentTitle"
    """
    The title of the incident
    """
    INCIDENT_DESCRIPTION = "IncidentDescription"
    """
    The description of the incident
    """
    INCIDENT_SEVERITY = "IncidentSeverity"
    """
    The severity of the incident
    """
    INCIDENT_STATUS = "IncidentStatus"
    """
    The status of the incident
    """
    INCIDENT_RELATED_ANALYTIC_RULE_IDS = "IncidentRelatedAnalyticRuleIds"
    """
    The related Analytic rule ids of the incident
    """
    INCIDENT_TACTICS = "IncidentTactics"
    """
    The tactics of the incident
    """
    INCIDENT_LABEL = "IncidentLabel"
    """
    The labels of the incident
    """
    INCIDENT_PROVIDER_NAME = "IncidentProviderName"
    """
    The provider name of the incident
    """
    ACCOUNT_AAD_TENANT_ID = "AccountAadTenantId"
    """
    The account Azure Active Directory tenant id
    """
    ACCOUNT_AAD_USER_ID = "AccountAadUserId"
    """
    The account Azure Active Directory user id
    """
    ACCOUNT_NAME = "AccountName"
    """
    The account name
    """
    ACCOUNT_NT_DOMAIN = "AccountNTDomain"
    """
    The account NetBIOS domain name
    """
    ACCOUNT_PUID = "AccountPUID"
    """
    The account Azure Active Directory Passport User ID
    """
    ACCOUNT_SID = "AccountSid"
    """
    The account security identifier
    """
    ACCOUNT_OBJECT_GUID = "AccountObjectGuid"
    """
    The account unique identifier
    """
    ACCOUNT_UPN_SUFFIX = "AccountUPNSuffix"
    """
    The account user principal name suffix
    """
    ALERT_PRODUCT_NAMES = "AlertProductNames"
    """
    The name of the product of the alert
    """
    AZURE_RESOURCE_RESOURCE_ID = "AzureResourceResourceId"
    """
    The Azure resource id
    """
    AZURE_RESOURCE_SUBSCRIPTION_ID = "AzureResourceSubscriptionId"
    """
    The Azure resource subscription id
    """
    CLOUD_APPLICATION_APP_ID = "CloudApplicationAppId"
    """
    The cloud application identifier
    """
    CLOUD_APPLICATION_APP_NAME = "CloudApplicationAppName"
    """
    The cloud application name
    """
    DNS_DOMAIN_NAME = "DNSDomainName"
    """
    The dns record domain name
    """
    FILE_DIRECTORY = "FileDirectory"
    """
    The file directory full path
    """
    FILE_NAME = "FileName"
    """
    The file name without path
    """
    FILE_HASH_VALUE = "FileHashValue"
    """
    The file hash value
    """
    HOST_AZURE_ID = "HostAzureID"
    """
    The host Azure resource id
    """
    HOST_NAME = "HostName"
    """
    The host name without domain
    """
    HOST_NET_BIOS_NAME = "HostNetBiosName"
    """
    The host NetBIOS name
    """
    HOST_NT_DOMAIN = "HostNTDomain"
    """
    The host NT domain
    """
    HOST_OS_VERSION = "HostOSVersion"
    """
    The host operating system
    """
    IO_T_DEVICE_ID = "IoTDeviceId"
    """
    "The IoT device id
    """
    IO_T_DEVICE_NAME = "IoTDeviceName"
    """
    The IoT device name
    """
    IO_T_DEVICE_TYPE = "IoTDeviceType"
    """
    The IoT device type
    """
    IO_T_DEVICE_VENDOR = "IoTDeviceVendor"
    """
    The IoT device vendor
    """
    IO_T_DEVICE_MODEL = "IoTDeviceModel"
    """
    The IoT device model
    """
    IO_T_DEVICE_OPERATING_SYSTEM = "IoTDeviceOperatingSystem"
    """
    The IoT device operating system
    """
    IP_ADDRESS = "IPAddress"
    """
    The IP address
    """
    MAILBOX_DISPLAY_NAME = "MailboxDisplayName"
    """
    The mailbox display name
    """
    MAILBOX_PRIMARY_ADDRESS = "MailboxPrimaryAddress"
    """
    The mailbox primary address
    """
    MAILBOX_UPN = "MailboxUPN"
    """
    The mailbox user principal name
    """
    MAIL_MESSAGE_DELIVERY_ACTION = "MailMessageDeliveryAction"
    """
    The mail message delivery action
    """
    MAIL_MESSAGE_DELIVERY_LOCATION = "MailMessageDeliveryLocation"
    """
    The mail message delivery location
    """
    MAIL_MESSAGE_RECIPIENT = "MailMessageRecipient"
    """
    The mail message recipient
    """
    MAIL_MESSAGE_SENDER_IP = "MailMessageSenderIP"
    """
    The mail message sender IP address
    """
    MAIL_MESSAGE_SUBJECT = "MailMessageSubject"
    """
    The mail message subject
    """
    MAIL_MESSAGE_P1_SENDER = "MailMessageP1Sender"
    """
    The mail message P1 sender
    """
    MAIL_MESSAGE_P2_SENDER = "MailMessageP2Sender"
    """
    The mail message P2 sender
    """
    MALWARE_CATEGORY = "MalwareCategory"
    """
    The malware category
    """
    MALWARE_NAME = "MalwareName"
    """
    The malware name
    """
    PROCESS_COMMAND_LINE = "ProcessCommandLine"
    """
    The process execution command line
    """
    PROCESS_ID = "ProcessId"
    """
    The process id
    """
    REGISTRY_KEY = "RegistryKey"
    """
    The registry key path
    """
    REGISTRY_VALUE_DATA = "RegistryValueData"
    """
    The registry key value in string formatted representation
    """
    URL = "Url"
    """
    The url
    """


class ConditionType(str, Enum):
    PROPERTY = "Property"
    """
    Evaluate an object property value
    """


class DataConnectorKind(str, Enum):
    """
    The data connector kind
    """
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    AZURE_SECURITY_CENTER = "AzureSecurityCenter"
    MICROSOFT_CLOUD_APP_SECURITY = "MicrosoftCloudAppSecurity"
    THREAT_INTELLIGENCE = "ThreatIntelligence"
    OFFICE365 = "Office365"
    AMAZON_WEB_SERVICES_CLOUD_TRAIL = "AmazonWebServicesCloudTrail"
    AZURE_ADVANCED_THREAT_PROTECTION = "AzureAdvancedThreatProtection"
    MICROSOFT_DEFENDER_ADVANCED_THREAT_PROTECTION = "MicrosoftDefenderAdvancedThreatProtection"


class DataTypeState(str, Enum):
    """
    Describe whether this data type connection is enabled or not.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EntityMappingType(str, Enum):
    """
    The V3 type of the mapped entity
    """
    ACCOUNT = "Account"
    """
    User account entity type
    """
    HOST = "Host"
    """
    Host entity type
    """
    IP = "IP"
    """
    IP address entity type
    """
    MALWARE = "Malware"
    """
    Malware entity type
    """
    FILE = "File"
    """
    System file entity type
    """
    PROCESS = "Process"
    """
    Process entity type
    """
    CLOUD_APPLICATION = "CloudApplication"
    """
    Cloud app entity type
    """
    DNS = "DNS"
    """
    DNS entity type
    """
    AZURE_RESOURCE = "AzureResource"
    """
    Azure resource entity type
    """
    FILE_HASH = "FileHash"
    """
    File-hash entity type
    """
    REGISTRY_KEY = "RegistryKey"
    """
    Registry key entity type
    """
    REGISTRY_VALUE = "RegistryValue"
    """
    Registry value entity type
    """
    SECURITY_GROUP = "SecurityGroup"
    """
    Security group entity type
    """
    URL = "URL"
    """
    URL entity type
    """
    MAILBOX = "Mailbox"
    """
    Mailbox entity type
    """
    MAIL_CLUSTER = "MailCluster"
    """
    Mail cluster entity type
    """
    MAIL_MESSAGE = "MailMessage"
    """
    Mail message entity type
    """
    SUBMISSION_MAIL = "SubmissionMail"
    """
    Submission mail entity type
    """


class EventGroupingAggregationKind(str, Enum):
    """
    The event grouping aggregation kinds
    """
    SINGLE_ALERT = "SingleAlert"
    ALERT_PER_RESULT = "AlertPerResult"


class IncidentClassification(str, Enum):
    """
    The reason the incident was closed
    """
    UNDETERMINED = "Undetermined"
    """
    Incident classification was undetermined
    """
    TRUE_POSITIVE = "TruePositive"
    """
    Incident was true positive
    """
    BENIGN_POSITIVE = "BenignPositive"
    """
    Incident was benign positive
    """
    FALSE_POSITIVE = "FalsePositive"
    """
    Incident was false positive
    """


class IncidentClassificationReason(str, Enum):
    """
    The classification reason the incident was closed with
    """
    SUSPICIOUS_ACTIVITY = "SuspiciousActivity"
    """
    Classification reason was suspicious activity
    """
    SUSPICIOUS_BUT_EXPECTED = "SuspiciousButExpected"
    """
    Classification reason was suspicious but expected
    """
    INCORRECT_ALERT_LOGIC = "IncorrectAlertLogic"
    """
    Classification reason was incorrect alert logic
    """
    INACCURATE_DATA = "InaccurateData"
    """
    Classification reason was inaccurate data
    """


class IncidentSeverity(str, Enum):
    """
    The severity of the incident
    """
    HIGH = "High"
    """
    High severity
    """
    MEDIUM = "Medium"
    """
    Medium severity
    """
    LOW = "Low"
    """
    Low severity
    """
    INFORMATIONAL = "Informational"
    """
    Informational severity
    """


class IncidentStatus(str, Enum):
    """
    The status of the incident
    """
    NEW = "New"
    """
    An active incident which isn't being handled currently
    """
    ACTIVE = "Active"
    """
    An active incident which is being handled
    """
    CLOSED = "Closed"
    """
    A non-active incident
    """


class MatchingMethod(str, Enum):
    """
    Grouping matching method. When method is Selected at least one of groupByEntities, groupByAlertDetails, groupByCustomDetails must be provided and not empty.
    """
    ALL_ENTITIES = "AllEntities"
    """
    Grouping alerts into a single incident if all the entities match
    """
    ANY_ALERT = "AnyAlert"
    """
    Grouping any alerts triggered by this rule into a single incident
    """
    SELECTED = "Selected"
    """
    Grouping alerts into a single incident if the selected entities, custom details and alert details match
    """


class MicrosoftSecurityProductName(str, Enum):
    """
    The alerts' productName on which the cases will be generated
    """
    MICROSOFT_CLOUD_APP_SECURITY = "Microsoft Cloud App Security"
    AZURE_SECURITY_CENTER = "Azure Security Center"
    AZURE_ADVANCED_THREAT_PROTECTION = "Azure Advanced Threat Protection"
    AZURE_ACTIVE_DIRECTORY_IDENTITY_PROTECTION = "Azure Active Directory Identity Protection"
    AZURE_SECURITY_CENTER_FOR_IO_T = "Azure Security Center for IoT"


class OwnerType(str, Enum):
    """
    The type of the owner the incident is assigned to.
    """
    UNKNOWN = "Unknown"
    """
    The incident owner type is unknown
    """
    USER = "User"
    """
    The incident owner type is an AAD user
    """
    GROUP = "Group"
    """
    The incident owner type is an AAD group
    """


class Source(str, Enum):
    """
    The source of the watchlist
    """
    LOCAL_FILE = "Local file"
    REMOTE_STORAGE = "Remote storage"


class ThreatIntelligenceResourceInnerKind(str, Enum):
    """
    The kind of the entity.
    """
    INDICATOR = "indicator"
    """
    Entity represents threat intelligence indicator in the system.
    """


class TriggerOperator(str, Enum):
    """
    The operation against the threshold that triggers alert rule.
    """
    GREATER_THAN = "GreaterThan"
    LESS_THAN = "LessThan"
    EQUAL = "Equal"
    NOT_EQUAL = "NotEqual"


class TriggersOn(str, Enum):
    INCIDENTS = "Incidents"
    """
    Trigger on Incidents
    """


class TriggersWhen(str, Enum):
    CREATED = "Created"
    """
    Trigger on created objects
    """
