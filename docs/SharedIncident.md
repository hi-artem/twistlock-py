# SharedIncident

Incident represents an incident

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID of the incident.  | [optional] 
**account_id** | **str** | Cloud account ID.  | [optional] 
**acknowledged** | **bool** | Indicates if the incident has been acknowledged (true) or not (false).  | [optional] 
**app** | **str** | Application that caused the incident.  | [optional] 
**app_id** | **str** | Application ID.  | [optional] 
**audits** | [**list[SharedRuntimeAudit]**](SharedRuntimeAudit.md) | All runtime audits of the incident.  | [optional] 
**category** | [**SharedIncidentCategory**](SharedIncidentCategory.md) |  | [optional] 
**cluster** | **str** | Cluster on which the incident was found.  | [optional] 
**collections** | **list[str]** | Collections to which this incident applies.  | [optional] 
**container_id** | **str** | ID of the container that triggered the incident.  | [optional] 
**container_name** | **str** | Unique container name.  | [optional] 
**custom_rule_name** | **str** | Name of the custom runtime rule that triggered the incident.  | [optional] 
**fqdn** | **str** | Current hostname&#39;s full domain name.  | [optional] 
**function** | **str** | Name of the serverless function.  | [optional] 
**hostname** | **str** | Current hostname.  | [optional] 
**image_id** | **str** | Container image ID.  | [optional] 
**image_name** | **str** | Container image name.  | [optional] 
**labels** | **dict(str, str)** | Custom labels associated with the container.  | [optional] 
**namespace** | **str** | k8s deployment namespace.  | [optional] 
**profile_id** | **str** | Runtime profile ID.  | [optional] 
**region** | **str** | Region of the serverless function.  | [optional] 
**runtime** | **str** | Runtime of the serverless function.  | [optional] 
**serial_num** | **int** | Serial number of the incident.  | [optional] 
**should_collect** | **bool** | Indicates if this incident should be collected (true) or not (false).  | [optional] 
**time** | **datetime** | Time of the incident (in UTC time).  | [optional] 
**type** | [**SharedIncidentType**](SharedIncidentType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


