# CredTemporaryToken

TemporaryToken is a temporary session token for cloud provider APIs AWS - https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html GCP - https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials Azure - https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_access_key_id** | **str** | Temporary access key.  | [optional] 
**aws_secret_access_key** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**duration** | **int** | Duration of the token.  | [optional] 
**expiration_time** | **datetime** | Expiration time for the token.  | [optional] 
**token** | [**CommonSecret**](CommonSecret.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


