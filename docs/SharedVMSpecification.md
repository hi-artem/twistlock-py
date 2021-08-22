# SharedVMSpecification

VMSpecification contains information for setting up and connecting to the image

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cap** | **int** | Specifies the maximum number of images to fetch and scan, ordered by most recently modified.  | [optional] 
**collections** | [**list[CollectionCollection]**](CollectionCollection.md) | List of collections. Scopes the images to be scanned.  | [optional] 
**console_addr** | **str** | Network-accessible address that Defender can use to publish scan results to Console.  | [optional] 
**credential_id** | **str** | ID of the credentials in the credentials store to use for authenticating with the cloud provider.  | [optional] 
**excluded_images** | **list[str]** | Images to exclude from scanning.  | [optional] 
**region** | **str** | Cloud provider region.  | [optional] 
**scanners** | **int** | Number of Defenders that can be utilized for each scan job.  | [optional] 
**version** | **str** | VM image type/format (e.g., AWS AMI).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


