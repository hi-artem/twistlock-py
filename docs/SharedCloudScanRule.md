# SharedCloudScanRule

CloudScanRule a rule for discovery/compliance/serverless radar scanning

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_region_type** | [**SharedAwsRegionType**](SharedAwsRegionType.md) |  | [optional] 
**compliance_check_ids** | **list[int]** | ComplianceCheckIDs are the compliance checks IDs.  | [optional] 
**compliance_enabled** | **bool** | ComplianceEnabled indicates whether compliance scan is enabled.  | [optional] 
**credential_id** | **str** | CredentialID is the id reference of the credential.  | [optional] 
**discovery_enabled** | **bool** | DiscoveryEnabled indicates whether discovery scan is enabled.  | [optional] 
**serverless_radar_enabled** | **bool** | ServerlessRadarEnabled indicates whether serverless radar scan is enabled.  | [optional] 
**vm_tags_enabled** | **bool** | VMTagsEnabled indicates whether fetching VM instance tags is enabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


