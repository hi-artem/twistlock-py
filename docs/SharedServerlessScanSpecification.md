# SharedServerlessScanSpecification

ServerlessScanSpecification contains information for connecting to serverless provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_region_type** | [**SharedAwsRegionType**](SharedAwsRegionType.md) |  | [optional] 
**cap** | **int** | Specifies the maximum number of functions to fetch and scan, ordered by most recently modified.  | [optional] 
**credential** | [**CredCredential**](CredCredential.md) |  | [optional] 
**credential_id** | **str** | ID of the credentials in the credentials store to use for authenticating with the cloud provider.  | [optional] 
**provider** | [**CommonCloudProvider**](CommonCloudProvider.md) |  | [optional] 
**scan_all_versions** | **bool** | Indicates if all image versions should be scanned (by default this option is off and only $LATEST is scanned).  | [optional] 
**scan_layers** | **bool** | Indicates if a function&#39;s layers should be scanned (on by default).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


