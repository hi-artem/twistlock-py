# SharedProfileKubernetesData

ProfileKubernetesData holds Kubernetes data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_roles** | [**list[SharedKubeClusterRole]**](SharedKubeClusterRole.md) | ClusterRoles are the cluster roles of the associated service account.  | [optional] 
**roles** | [**list[SharedKubeRole]**](SharedKubeRole.md) | Roles are the roles of the associated service account.  | [optional] 
**service_account** | **str** | ServiceAccount is the service account used to access Kubernetes apiserver This field will be empty if the container is not running inside of a Pod.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


