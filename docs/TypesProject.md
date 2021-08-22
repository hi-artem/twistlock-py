# TypesProject

Project represent the project details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the project name (primary index).  | [optional] 
**address** | **str** | Address is the project address.  | [optional] 
**ca** | **list[str]** | CACertificate is the remote console CA certificate.  | [optional] 
**creation_time** | **datetime** | CreationTime is the remote project creation time.  | [optional] 
**err** | **str** | Err are errors that happened during project synchronization / setup.  | [optional] 
**password** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**skip_certificate_verification** | **bool** | SkipCertificateVerification indicates that the connection to the secondary project is done on insecure channel, this is used when secondary project is behind a proxy or when customer is using custom certs.  | [optional] 
**username** | **str** | Username is the remote project username.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


