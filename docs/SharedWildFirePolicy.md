# SharedWildFirePolicy

WildFirePolicy is the global wildfire usage policy, set by the client

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_enabled** | **bool** | ComplianceEnabled indicates whether compliance malware scan will consult WF.  | [optional] 
**grayware_as_malware** | **bool** | GraywareAsMalware indicates whether files with WF verdict of Grayware will be treated as malware.  | [optional] 
**region** | **str** | Region is the WF server region to query.  | [optional] 
**runtime_enabled** | **bool** | RuntimeEnabled indicates whether runtime malware scan will consult WF.  | [optional] 
**upload_enabled** | **bool** | UploadEnabled indicates whether files will be uploaded to WF.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


