# SharedServerlessAutoDeploySpecification

ServerlessAutoDeploySpecification contains the information for auto-deploying serverless functions protection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | Collections is a list of collections the rule applies to.  | [optional] 
**console_addr** | **str** | ConsoleAddr represents the hostname of the console to connect to.  | [optional] 
**credential_id** | **str** | CredentialID is the service provider authentication data.  | [optional] 
**last_modified** | **datetime** | LastModified is the last modified time of the specification.  | [optional] 
**name** | **str** | Name is the name of the spec.  | [optional] 
**region** | **str** | Region is the region where the serverless function is deployed.  | [optional] 
**runtimes** | **list[str]** | Runtimes is the list of runtimes to which the spec applies.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


