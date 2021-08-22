# CnnfRule

Rule contains the properties common to both host and container network firewall

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**dst** | **int** | EntityID represents the ID of each network firewall entity. 20 bits are used. Max legal value: 2^20-1 | [optional] 
**effect** | [**CommonEffect**](CommonEffect.md) |  | [optional] 
**id** | **int** | RuleID represents the ID of each container network firewall policy rule | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**ports** | [**list[CommonPortRange]**](CommonPortRange.md) | Ports are the entity port range specifications.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**src** | **int** | EntityID represents the ID of each network firewall entity. 20 bits are used. Max legal value: 2^20-1 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


