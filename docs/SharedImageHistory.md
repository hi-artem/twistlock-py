# SharedImageHistory

ImageHistory represent a layer in the image's history

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_layer** | **bool** | Indicates if this layer originated from the base image (true) or not (false).  | [optional] 
**created** | **int** | Date/time when the image layer was created.  | [optional] 
**empty_layer** | **bool** | Indicates if this instruction didn&#39;t create a separate layer (true) or not (false).  | [optional] 
**id** | **str** | ID of the layer.  | [optional] 
**instruction** | **str** | Docker file instruction and arguments used to create this layer.  | [optional] 
**size_bytes** | **int** | Size of the layer (in bytes).  | [optional] 
**tags** | **list[str]** | Holds the image tags.  | [optional] 
**vulnerabilities** | [**list[VulnVulnerability]**](VulnVulnerability.md) | Vulnerabilities which originated from this layer.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


