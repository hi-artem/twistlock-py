# RuntimeFileIntegrityRule

FileIntegrityRule represents a single file integrity monitoring rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dir** | **bool** | Dir indicates that the path is a directory.  | [optional] 
**exclusions** | **list[str]** | Exclusions are filenames that should be ignored while generating audits These filenames may contain a wildcard regex pattern, e.g. foo*.log, *.cache.  | [optional] 
**metadata** | **bool** | Metadata indicates that metadata changes should be monitored (e.g. chmod, chown).  | [optional] 
**path** | **str** | Path is the path to monitor.  | [optional] 
**proc_whitelist** | **list[str]** | ProcWhitelist are the processes to ignore Filesystem events caused by these processes DO NOT generate file integrity events.  | [optional] 
**read** | **bool** | Read indicates that reads operations should be monitored.  | [optional] 
**recursive** | **bool** | Recursive indicates that monitoring should be recursive.  | [optional] 
**write** | **bool** | Write indicates that write operations should be monitored.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


