# ApiAlertProfile

AlertProfile represents an alert profile (event type and recipients)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the alert profile ID.  | [optional] 
**console_identifier** | **str** | ConsoleIdentifier is the console identifier.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**email** | [**ApiAlertProfileEmailSettings**](ApiAlertProfileEmailSettings.md) |  | [optional] 
**gcp_pubsub** | [**ApiAlertProfileGcpPubsubSettings**](ApiAlertProfileGcpPubsubSettings.md) |  | [optional] 
**jira** | [**ApiAlertProfileJIRASettings**](ApiAlertProfileJIRASettings.md) |  | [optional] 
**last_error** | **str** | LastError represents the last error when sending the profile.  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**pagerduty** | [**ApiAlertProfilePagerDutySettings**](ApiAlertProfilePagerDutySettings.md) |  | [optional] 
**policy** | [**dict(str, ApiAlertRule)**](ApiAlertRule.md) | Policy contains the mapping between alert type to the applied alert rules.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**security_advisor** | [**ApiAlertProfileSecurityAdvisor**](ApiAlertProfileSecurityAdvisor.md) |  | [optional] 
**security_center** | [**ApiAlertProfileSecurityCenterSettings**](ApiAlertProfileSecurityCenterSettings.md) |  | [optional] 
**security_hub** | [**ApiAlertProfileSecurityHubSettings**](ApiAlertProfileSecurityHubSettings.md) |  | [optional] 
**service_now** | [**ApiAlertProfileServiceNowSettings**](ApiAlertProfileServiceNowSettings.md) |  | [optional] 
**slack** | [**ApiAlertProfileSlackSettings**](ApiAlertProfileSlackSettings.md) |  | [optional] 
**webhook** | [**ApiAlertProfileWebhookSettings**](ApiAlertProfileWebhookSettings.md) |  | [optional] 
**xsoar** | [**ApiAlertProfileXSOARSettings**](ApiAlertProfileXSOARSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


