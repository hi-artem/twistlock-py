# CodereposScanResult

ScanResult holds a specific repository data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Scan report ID in the database.  | [optional] 
**collections** | **list[str]** | List of matching code repo collections.  | [optional] 
**compliance_risk_score** | **float** | Code repository&#39;s compliance risk score. Used for sorting.  | [optional] 
**files** | [**list[CodereposManifestFile]**](CodereposManifestFile.md) | Scan result for each manifest file in the repository.  | [optional] 
**_pass** | **bool** | Indicates whether the scan passed or failed.  | [optional] 
**repository** | [**CodereposRepository**](CodereposRepository.md) |  | [optional] 
**scan_time** | **datetime** | Date/time when this repository was last scanned. The results might be from the DB and not updated if the repository contents have not changed.  | [optional] 
**type** | [**SharedCodeRepoProviderType**](SharedCodeRepoProviderType.md) |  | [optional] 
**update_time** | **datetime** | Date/time when this repository was last updated.  | [optional] 
**vuln_info** | [**SharedImageInfo**](SharedImageInfo.md) |  | [optional] 
**vulnerability_risk_score** | **float** | Code repository&#39;s CVE risk score. Used for sorting.  | [optional] 
**vulnerable_files** | **int** | Counts how many files have vulnerabilities. Vulnerability info is calculated on demand.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


