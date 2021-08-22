# ForensicContainerEvent

ContainerEvent holds forensic event information (in flat structure)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_ports** | **bool** | AllPorts indicates all listening ports are allowed.  | [optional] 
**attack** | [**SharedRuntimeAttackType**](SharedRuntimeAttackType.md) |  | [optional] 
**category** | [**SharedIncidentCategory**](SharedIncidentCategory.md) |  | [optional] 
**command** | **str** | Command is the event command.  | [optional] 
**container_id** | **str** | ContainerID is the event container id.  | [optional] 
**dst_ip** | **str** | DstIP is the destination IP of the connection.  | [optional] 
**dst_port** | **int** | DstPort is the destination port.  | [optional] 
**dst_profile_id** | **str** | DstProfileID is the profile ID of the connection destination.  | [optional] 
**effect** | **str** | Effect is the runtime audit effect.  | [optional] 
**listening_start_time** | **datetime** | listeningStartTime is the port listening start time.  | [optional] 
**message** | **str** | Message is the runtime audit message.  | [optional] 
**network_collection_type** | **str** | NetworkCollection describe the different types of collection of network events | [optional] 
**outbound** | **bool** | Outbound indicates if the port is outbound.  | [optional] 
**path** | **str** | Path is the event path.  | [optional] 
**pid** | **int** | Pid is the event process id.  | [optional] 
**port** | **int** | Port is the listening port.  | [optional] 
**ppid** | **int** | PPid is the event parent process id.  | [optional] 
**process** | **str** | Process is the event process.  | [optional] 
**src_ip** | **str** | SrcIP is the source IP of the connection.  | [optional] 
**src_profile_id** | **str** | SrcProfileID is the profile ID of the connection source.  | [optional] 
**static** | **bool** | Static indicates the event was added to the profile without behavioral indication.  | [optional] 
**timestamp** | **datetime** | Timestamp is the event timestamp.  | [optional] 
**type** | [**ForensicContainerEventType**](ForensicContainerEventType.md) |  | [optional] 
**user** | **str** | User is the event user.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


