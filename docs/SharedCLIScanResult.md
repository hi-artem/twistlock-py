# SharedCLIScanResult

CLIScanResult describes a CLI scan result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **list[str]** | ID of the scan result.  | [optional] 
**build** | **str** | CI build.  | [optional] 
**compliance_failure_summary** | **str** | Scan compliance failure summary.  | [optional] 
**entity_info** | [**SharedImageScanResult**](SharedImageScanResult.md) |  | [optional] 
**job_name** | **str** | CI job name.  | [optional] 
**_pass** | **bool** | Indicates if the scan passed (true) or failed (false).  | [optional] 
**time** | **datetime** | Time of the scan.  | [optional] 
**version** | **str** | Scanner version.  | [optional] 
**vuln_failure_summary** | **str** | Scan vulnerability failure summary.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


