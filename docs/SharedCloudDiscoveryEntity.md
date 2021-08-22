# SharedCloudDiscoveryEntity

CloudDiscoveryEntity holds data about a discovered entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_services_count** | **int** | ActiveServicesCount is the number of active services in ecs cluster.  | [optional] 
**arn** | **str** | The Amazon Resource Name (ARN) assigned to the entity.  | [optional] 
**container_group** | **str** | ContainerGroup is the azure aci container group the container belongs to.  | [optional] 
**created_at** | **datetime** | CreatedAt is the time when the entity was created.  | [optional] 
**defended** | **bool** | Defended indicates if the entity is defended.  | [optional] 
**image** | **str** | Image is the image of an aci container.  | [optional] 
**last_modified** | **datetime** | LastModified is the modification time of the function.  | [optional] 
**name** | **str** | Name is the name of the entity.  | [optional] 
**nodes_count** | **int** | NodesCount is the number of nodes in the cluster (aks, gke).  | [optional] 
**resource_group** | **str** | ResourceGroup is the the azure resource group containing the entity.  | [optional] 
**running_tasks_count** | **int** | RunningTasksCount is the number of running tasks in ecs cluster.  | [optional] 
**runtime** | **str** | Runtime is runtime environment for the function, i.e. nodejs.  | [optional] 
**status** | **str** | Status is the current status of entity.  | [optional] 
**version** | **str** | Version is the version of the entity.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


