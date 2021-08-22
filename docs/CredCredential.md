# CredCredential

Credential contains external provider authentication data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID for the credential.  | [optional] 
**account_guid** | **str** | Unique ID for an IBM Cloud account.  | [optional] 
**account_id** | **str** | Account identifier (e.g., username, access key, account GUID, etc.).  | [optional] 
**api_token** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**ca_cert** | **str** | CA certificate for certificate-based authentication.  | [optional] 
**description** | **str** | Description of the credential.  | [optional] 
**external** | **bool** | Indicates if the credential is external (true) or not (false).  | [optional] 
**last_modified** | **datetime** | Datetime when the credential was last modified.  | [optional] 
**owner** | **str** | User who created or modified the credential.  | [optional] 
**role_arn** | **str** | Amazon Resource Name (ARN) of the role to assume.  | [optional] 
**secret** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**tokens** | [**CredTemporaryToken**](CredTemporaryToken.md) |  | [optional] 
**type** | [**CredType**](CredType.md) |  | [optional] 
**use_aws_role** | **bool** | Indicates if authentication should be done with the instance&#39;s attached credentials (EC2 IAM Role).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


