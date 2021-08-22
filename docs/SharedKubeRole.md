# SharedKubeRole

KubeRole is a compact version of Kubernetes Role See https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.11/#role-v1-rbac-authorization-k8s-io

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | [**list[SharedKubeLabel]**](SharedKubeLabel.md) | Labels are the labels associated with the role.  | [optional] 
**name** | **str** | Name is the kubernetes role name.  | [optional] 
**namespace** | **str** | Namespace is the namespace associated with the role.  | [optional] 
**role_binding** | **str** | RoleBinding is the name of the role binding used for display.  | [optional] 
**rules** | [**list[SharedKubePolicyRule]**](SharedKubePolicyRule.md) | Rules are the policy rules associated with the role.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


