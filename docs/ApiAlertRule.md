# ApiAlertRule

AlertRule represents the configuration of an alert type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_rules** | **bool** | AllRules controls whether an alert is sent out for audits on all policy rules.  | [optional] 
**enabled** | **bool** | Enabled controls whether the rule is enabled.  | [optional] 
**rules** | **list[str]** | AssociatedRules defines the specific rules whose audits will generate alerts (relevant only if AllRules is false).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


