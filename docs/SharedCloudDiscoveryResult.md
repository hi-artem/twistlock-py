# SharedCloudDiscoveryResult

CloudDiscoveryResult represents a cloud scan result for a specific cloud provider, service and region

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the cloud account ID.  | [optional] 
**collections** | **list[str]** | Collections are the matched result collections.  | [optional] 
**credential_id** | **str** | CredentialID is the id reference of the credential used.  | [optional] 
**defended** | **int** | Defended is the number of defended entities (registries, functions, clusters).  | [optional] 
**entities** | [**list[SharedCloudDiscoveryEntity]**](SharedCloudDiscoveryEntity.md) | Entities holds detailed scan results.  | [optional] 
**err** | **str** | Err holds any error found during a scan.  | [optional] 
**project** | **str** | Project is the GCP project that was scanned.  | [optional] 
**provider** | [**CommonCloudProvider**](CommonCloudProvider.md) |  | [optional] 
**region** | **str** | Region is the region that was scanned, for example: GCP - \&quot;us-east-1\&quot;, Azure - \&quot;westus\&quot;.  | [optional] 
**registry** | **str** | Registry is the Azure registry that was scanned, for example: testcloudscanregistry.azurecr.io.  | [optional] 
**service_type** | [**SharedScanResultType**](SharedScanResultType.md) |  | [optional] 
**total** | **int** | Total is total number of entities found in cloud scan.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


