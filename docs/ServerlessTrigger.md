# ServerlessTrigger

Trigger contains function triggers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**list[SharedKeyValues]**](SharedKeyValues.md) | Properties are the trigger properties. There may be multiple values per key, for example AWS S3 event types: ObjectCreatedByPost, ObjectCreatedByCopy, ObjectCreatedByPut.  | [optional] 
**source_id** | **str** | SourceID is the id of the service instance that caused the trigger. For example AWS S3 bucket ARN, AWS apigateway ARN, etc.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


