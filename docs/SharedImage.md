# SharedImage

Image represents a container image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Date/time when the image was created.  | [optional] 
**entrypoint** | **list[str]** | Combined entrypoint of the image (entrypoint + CMD).  | [optional] 
**env** | **list[str]** | Image environment variables.  | [optional] 
**healthcheck** | **bool** | Indicates if health checks are enabled (true) or not (false).  | [optional] 
**history** | [**list[SharedImageHistory]**](SharedImageHistory.md) | Holds the image history.  | [optional] 
**id** | **str** | ID of the image.  | [optional] 
**labels** | **dict(str, str)** | Image labels.  | [optional] 
**layers** | **list[str]** | Image filesystem layers.  | [optional] 
**os** | **str** | Image os type.  | [optional] 
**repo_digest** | **list[str]** | Image repo digests.  | [optional] 
**repo_tags** | **list[str]** | Image repo tags.  | [optional] 
**user** | **str** | Image user.  | [optional] 
**working_dir** | **str** | Base working directory of the image.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


