# SharedKubeClusterRole

KubeClusterRole is a compact version of Kubernetes ClusterRole See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.11/#clusterrole-v1-rbac-authorization-k8s-io

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**list[SharedKubeLabel]**](SharedKubeLabel.md) | Labels are the labels associated with the role.  | [optional] 
**name** | **str** | Name is the role name.  | [optional] 
**role_binding** | **str** | RoleBinding is the name of the role binding used for display.  | [optional] 
**rules** | [**list[SharedKubePolicyRule]**](SharedKubePolicyRule.md) | Rules are the list of rules associated with the cluster role.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


