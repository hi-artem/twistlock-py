# RuntimeContainerPolicyRule

ContainerPolicyRule represents a single rule in the runtime policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_protection** | **bool** | Indicates whether advanced protection (e.g., custom or premium feeds for container, added whitelist rules for serverless) is enabled (true) or not (false).  | [optional] 
**cloud_metadata_enforcement** | **bool** | Catches containers that access the cloud provider metadata API.  | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | List of collections. Used to scope the rule.  | [optional] 
**custom_rules** | [**list[CustomrulesRef]**](CustomrulesRef.md) | List of custom runtime rules.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**dns** | [**RuntimeDNSRule**](RuntimeDNSRule.md) |  | [optional] 
**filesystem** | [**RuntimeFilesystemRule**](RuntimeFilesystemRule.md) |  | [optional] 
**kubernetes_enforcement** | **bool** | Detects containers that attempt to compromise the orchestrator.  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**network** | [**RuntimeContainerNetworkRule**](RuntimeContainerNetworkRule.md) |  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**processes** | [**RuntimeProcessesRule**](RuntimeProcessesRule.md) |  | [optional] 
**wild_fire_analysis** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


