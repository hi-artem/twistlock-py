# ForensicHostEvent

HostEvent holds host forensic event information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** | App is the application associated with the event.  | [optional] 
**attack** | [**SharedRuntimeAttackType**](SharedRuntimeAttackType.md) |  | [optional] 
**category** | [**SharedIncidentCategory**](SharedIncidentCategory.md) |  | [optional] 
**command** | **str** | Command is the event command.  | [optional] 
**country** | **str** | Country is the country associated with the event.  | [optional] 
**effect** | **str** | Effect is the runtime audit effect.  | [optional] 
**interactive** | **bool** | Interactive indicates if the event is interactive.  | [optional] 
**ip** | **str** | IP is the IP address associated with the event.  | [optional] 
**listening_start_time** | **datetime** | ListeningStartTime is the listening port start time.  | [optional] 
**message** | **str** | Message is the runtime audit message.  | [optional] 
**path** | **str** | Path is the event path.  | [optional] 
**pid** | **int** | Pid is the event process id.  | [optional] 
**port** | **int** | Port is the listening port.  | [optional] 
**ppath** | **str** | Path is the event parent path.  | [optional] 
**ppid** | **int** | PPid is the event parent process id.  | [optional] 
**process** | **str** | Process is the event process.  | [optional] 
**timestamp** | **datetime** | Timestamp is the event timestamp.  | [optional] 
**type** | [**ForensicHostEventType**](ForensicHostEventType.md) |  | [optional] 
**user** | **str** | User is the event user.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


