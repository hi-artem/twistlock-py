# TrustPolicyRule

PolicyRule represents an trust policy rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_groups** | **list[str]** | AllowedGroups are the ids of the groups that are whitelisted by this rule.  | [optional] 
**block_msg** | **str** | PolicyBlockMsg represent the block message in a Policy | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | Collections is a list of collections the rule applies to.  | [optional] 
**denied_groups** | **list[str]** | DeniedGroups are the ids of the groups that are blacklisted by this rule.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**effect** | [**VulnEffect**](VulnEffect.md) |  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


