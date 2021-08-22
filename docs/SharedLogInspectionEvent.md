# SharedLogInspectionEvent

LogInspectionEvent is a log inspection event detected according to the log inspection rules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the cloud account ID.  | [optional] 
**cluster** | **str** | Cluster is the cluster on which the event was found.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this event applies.  | [optional] 
**hostname** | **str** | Hostname is the hostname on which the event was found.  | [optional] 
**line** | **str** | Line is the matching log line.  | [optional] 
**logfile** | **str** | Logfile is the log file which triggered the event.  | [optional] 
**rule_name** | **str** | RuleName is the name of the applied rule for auditing log inspection events.  | [optional] 
**time** | **datetime** | Time is the time of the event.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


