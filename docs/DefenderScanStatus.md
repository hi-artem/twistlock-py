# DefenderScanStatus

ScanStatus represents the status of current scan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** | Indicates if scanning has successfully completed (true) or not (false).  | [optional] 
**errors** | **list[str]** | List of errors that occurred during the last scan.  | [optional] 
**hostname** | **str** | Name of the host where Defender runs.  | [optional] 
**scan_time** | **datetime** | Datetime of the last completed scan.  | [optional] 
**scanning** | **bool** | Indicates whether scanning is in progress (true) or not (false).  | [optional] 
**selective** | **bool** | Indicates if the scan is for a specific resource (true) or not (false).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


