# CommonSecret

Secret contains the plain and encrypted version of a value (the plain version is never stored in the DB)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted** | **str** | Encrypted value for the secret.  | [optional] 
**plain** | **str** | Plain text value for the secret. Note: marshalling to JSON will convert to an encrypted value.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


