# SharedContainerRuntimeProfile

ContainerRuntimeProfile represents the image runtime profile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id is the profile ID.  | [optional] 
**account_ids** | **list[str]** | AccountIDs are the cloud account IDs associated with the container runtime profile.  | [optional] 
**archived** | **bool** | Archive indicates whether this profile is archived.  | [optional] 
**capabilities** | [**RuntimeContainerCapabilities**](RuntimeContainerCapabilities.md) |  | [optional] 
**cluster** | **str** | Cluster is the provided cluster name.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this profile applies.  | [optional] 
**created** | **datetime** | Created is the profile creation time.  | [optional] 
**entrypoint** | **str** | Entrypoint is the image entrypoint.  | [optional] 
**events** | [**list[SharedContainerHistoryEvent]**](SharedContainerHistoryEvent.md) | Events are the last historical interactive process events for this profile, they are updated in a designated flow.  | [optional] 
**filesystem** | [**RuntimeProfileFilesystem**](RuntimeProfileFilesystem.md) |  | [optional] 
**hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**host_network** | **bool** | HostNetwork whether the instance share the network namespace with the host.  | [optional] 
**host_pid** | **bool** | HostPid indicates whether the instance share the pid namespace with the host.  | [optional] 
**image** | **str** | Image is the image name that represents the image.  | [optional] 
**image_id** | **str** | ImageID is the profile&#39;s image ID.  | [optional] 
**infra** | **bool** | InfraContainer indicates this is an infrastructure container.  | [optional] 
**istio** | **bool** | Istio states whether it is an istio-monitored profile.  | [optional] 
**k8s** | [**SharedProfileKubernetesData**](SharedProfileKubernetesData.md) |  | [optional] 
**label** | **str** | Label is the profile&#39;s label.  | [optional] 
**last_update** | **datetime** | Modified is the last time when this profile was modified.  | [optional] 
**learned_startup** | **bool** | LearnedStartup indicates that startup events were learned.  | [optional] 
**namespace** | **str** | Namespace is the k8s deployment namespace.  | [optional] 
**network** | [**RuntimeProfileNetwork**](RuntimeProfileNetwork.md) |  | [optional] 
**os** | **str** | OS is the profile image OS.  | [optional] 
**processes** | [**RuntimeProfileProcesses**](RuntimeProfileProcesses.md) |  | [optional] 
**relearning_cause** | **str** | RelearningCause is a string that describes the reasoning for a profile to enter the learning mode after being activated.  | [optional] 
**remaining_learning_duration_sec** | **float** | RemainingLearningDurationSec represents the total time left that the system need to finish learning this image.  | [optional] 
**state** | [**SharedRuntimeProfileState**](SharedRuntimeProfileState.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


