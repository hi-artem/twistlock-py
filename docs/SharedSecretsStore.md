# SharedSecretsStore

SecretsStore represents a secret storage entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | AppID is the twistlock application id, as set in Cyberark store.  | [optional] 
**ca_cert** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**client_cert** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**credential_id** | **str** | CredentialID is the authentication credential id.  | [optional] 
**name** | **str** | Name is the name of the secret store defined by the user.  | [optional] 
**region** | **str** | Region is the secrets store&#39;s region.  | [optional] 
**type** | [**SharedSecretStoreType**](SharedSecretStoreType.md) |  | [optional] 
**url** | **str** | URL is the secrets store&#39;s endpoint point.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


