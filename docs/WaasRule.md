# WaasRule

Rule represents a single rule that is associated with a container firewall

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications_spec** | [**list[WaasApplicationSpec]**](WaasApplicationSpec.md) | List of API specifications in the rule.  | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | List of collections. Used to scope the rule.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**read_timeout_seconds** | **int** | ReadTimeout is the timeout of request reads in seconds, when no value is specified (0) the timeout is 5 seconds.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


