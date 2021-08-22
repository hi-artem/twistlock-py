# TypesBaseImagesRule

BaseImagesRule holds the base images defined by a single scope

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Pattern is the scope configuration identification, e.g. image name regex pattern.  | [optional] 
**description** | **str** | Description is the base images scope description.  | [optional] 
**images** | [**list[TypesBaseImage]**](TypesBaseImage.md) | Images holds the base images which matches the scope configuration, capped to 50 image digests per scope.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


