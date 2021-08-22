# SharedVaultSecret

VaultSecret represents a secret held by a secret store

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | Folder is one of the following: Cyberark: Name of the folder for secrets held in Cyberark store Hashicorp: The directory path for secrets held in Hashicorp store AWS: The name of the secret in AWS Secrets Manager or AWS Parameter Store.  | [optional] 
**key** | **str** | Key is the secret&#39;s identifier in the secrets store.  | [optional] 
**name** | **str** | Name is the name of the secret as input from the user.  | [optional] 
**safe** | **str** | Safe is the name of the safe, for secrets held in Cyberark store.  | [optional] 
**store** | **str** | Store is the name of the secrets store where the secret is held.  | [optional] 
**value** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**version** | **str** | Version is the Azure secret version.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


