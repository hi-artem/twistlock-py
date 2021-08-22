# PrismaIaCScanRequest

IaCScanRequest is the request body for initializing a scan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_name** | **str** | AssetName is the name of the asset performing the scan.  | [optional] 
**asset_type** | **str** | AssetType is the name of the asset performing the scan.  | [optional] 
**failure_criteria** | [**PrismaIaCScanFailureCriteria**](PrismaIaCScanFailureCriteria.md) |  | [optional] 
**scan_attributes** | **dict(str, str)** | ScanAttributes is a map of key value pairs holding attributes of the scan.  | [optional] 
**tags** | **dict(str, str)** | Tags is a map of key value pairs holding information about the scan.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


