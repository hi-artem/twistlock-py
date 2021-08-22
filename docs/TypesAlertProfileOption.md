# TypesAlertProfileOption

AlertProfileOption describes options available for configuring an alert type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_type** | [**ApiAlertType**](ApiAlertType.md) |  | [optional] 
**has_policy** | **bool** | HasPolicy defines whether the alerts are triggered by policy (e.g., this is false for defender alerts).  | [optional] 
**name** | **str** | Name is the display name for the option.  | [optional] 
**rules** | **list[str]** | Rules are the rule names for the policy associated with this alert type (only relevant if HasPolicy is true).  | [optional] 
**supported_clients** | **list[str]** | SupportedClients are the supported alert clients for this alert (e.g., jira, email).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


