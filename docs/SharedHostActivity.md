# SharedHostActivity

HostActivity holds information for a user activity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | AccountID is the cloud account ID.  | [optional] 
**affected_services** | **list[str]** | AffectedServices is the affected systemd service.  | [optional] 
**cluster** | **str** | Cluster is the cluster from which the audit originated.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this host activity applies.  | [optional] 
**command** | **str** | Command is the original (with arguments) command the user invoked.  | [optional] 
**hostname** | **str** | Hostname the activity originated from.  | [optional] 
**interactive** | **bool** | Interactive indicates that the target process was spawned in an interactive session.  | [optional] 
**modified_files** | **list[str]** | ModifiedFiles is the related modified files.  | [optional] 
**rule_name** | **str** | RuleName is the name of the rule applied to the host activity.  | [optional] 
**service** | **str** | Service is the owning systemd service.  | [optional] 
**time** | **datetime** | Time is time of the activity.  | [optional] 
**type** | [**SharedActivityType**](SharedActivityType.md) |  | [optional] 
**user** | **str** | Username of the user that triggered the activity.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


