# CustomrulesRule

Rule represents a custom rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rule ID. Must be unique.  | [optional] 
**attack_techniques** | [**list[MitreTechnique]**](MitreTechnique.md) | List of attack techniques.  | [optional] 
**description** | **str** | Description of the rule.  | [optional] 
**message** | **str** | Macro that is printed as part of the audit/incident message.  | [optional] 
**modified** | **int** | Datetime when the rule was created or last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**owner** | **str** | User who created or modified the rule.  | [optional] 
**script** | **str** | Custom script.  | [optional] 
**type** | [**CustomrulesType**](CustomrulesType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


