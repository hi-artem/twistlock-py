# SharedSecretsRule

SecretsRule defines distribution of secrets to containers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | Collections is a list of collections the rule applies to.  | [optional] 
**disabled** | **bool** | Indicates if the rule is currently disabled (true) or not (false).  | [optional] 
**injection** | [**SharedSecretsInjectionType**](SharedSecretsInjectionType.md) |  | [optional] 
**modified** | **datetime** | Datetime when the rule was last modified.  | [optional] 
**name** | **str** | Name of the rule.  | [optional] 
**notes** | **str** | Free-form text.  | [optional] 
**owner** | **str** | User who created or last modified the rule.  | [optional] 
**previous_name** | **str** | Previous name of the rule. Required for rule renaming.  | [optional] 
**read_all_perm** | **bool** | ReadAllPerm indicates whether file permissions of injected secrets allow read by root only or by all users.  | [optional] 
**secrets** | [**list[SharedVaultSecret]**](SharedVaultSecret.md) | Secrets are the encrypted secrets to inject.  | [optional] 
**target_dir** | **str** | TargetDir is the target directory to inject secret files to if we choose filesystem injection.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


