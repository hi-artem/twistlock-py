# SharedFileIntegrityEvent

FileIntegrityEvent represents a single file integrity event detected according to the file integrity monitoring rules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the cloud account ID.  | [optional] 
**cluster** | **str** | Cluster is the cluster on which the event was found.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this event applies.  | [optional] 
**description** | **str** | Description is a human readable description of the action performed on the path.  | [optional] 
**event_type** | [**SharedFileIntegrityEventType**](SharedFileIntegrityEventType.md) |  | [optional] 
**file_type** | **int** | FSFileType represents the file type | [optional] 
**fqdn** | **str** | FQDN is the current fully qualified domain name used in audit alerts.  | [optional] 
**hostname** | **str** | Hostname is the hostname on which the event was found.  | [optional] 
**metadata** | [**SharedFileMetadata**](SharedFileMetadata.md) |  | [optional] 
**path** | **str** | Path is the absolute path of the event.  | [optional] 
**process_name** | **str** | ProcessName is the name of the process initiated the event.  | [optional] 
**rule_name** | **str** | RuleName is the name of the applied rule for auditing file integrity rules.  | [optional] 
**time** | **datetime** | Time is the time of the event.  | [optional] 
**user** | **str** | User is the user initiated the event.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


