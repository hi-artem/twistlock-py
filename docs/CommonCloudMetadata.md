# CommonCloudMetadata

CloudMetadata is the metadata for an instance running in a cloud provider (AWS/GCP/Azure)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Cloud account ID.  | [optional] 
**image** | **str** | Image name.  | [optional] 
**labels** | [**list[CommonExternalLabel]**](CommonExternalLabel.md) | Cloud provider metadata labels.  | [optional] 
**name** | **str** | Instance name.  | [optional] 
**provider** | [**CommonCloudProvider**](CommonCloudProvider.md) |  | [optional] 
**region** | **str** | Instance region.  | [optional] 
**resource_id** | **str** | Unique ID of the resource.  | [optional] 
**type** | **str** | Instance type.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


