# SharedProgress

Progress represents the scanning progress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery** | **bool** | Discovery indicates whether the scan is in discovery phase.  | [optional] 
**error** | **str** | Error is the error that happened during scan.  | [optional] 
**hostname** | **str** | Hostname is the hostname for which the progress apply.  | [optional] 
**id** | **str** | ID is the ID of the entity being scanned.  | [optional] 
**scan_time** | **datetime** | ScanTime is the time of scan.  | [optional] 
**scanned** | **int** | Scanned is the number of entities for which the scan completed.  | [optional] 
**title** | **str** | Title is the progress title (set by the scanning process).  | [optional] 
**total** | **int** | Total is the total amount of entities that should be scanned.  | [optional] 
**type** | [**SharedScanType**](SharedScanType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


