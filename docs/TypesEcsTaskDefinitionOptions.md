# TypesEcsTaskDefinitionOptions

EcsTaskDefinitionOptions holds the ecs deployment options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | Cluster is the kubernetes or ecs cluster name.  | [optional] 
**collect_pod_labels** | **bool** | CollectPodLabels indicates whether to collect pod related labels resource labels.  | [optional] 
**console_addr** | **str** | ConsoleAddr is the console address for defender communication.  | [optional] 
**credential_id** | **str** | CredentialID is the name of the credential used.  | [optional] 
**cri** | **bool** | CRI indicates defender uses CRI instead of docker.  | [optional] 
**docker_socket_path** | **str** | DockerSocketPath is the path of the docker socket file.  | [optional] 
**image** | **str** | Image is the full daemonset image name.  | [optional] 
**istio** | **bool** | MonitorIstio indicates whether to monitor Istio.  | [optional] 
**namespace** | **str** | Namespace is the target deamonset namespaces.  | [optional] 
**node_selector** | **str** | NodeSelector is a key/value node selector.  | [optional] 
**orchestration** | **str** | Orchestration is the orchestration type.  | [optional] 
**privileged** | **bool** | Privileged indicates whether to run defenders as privileged.  | [optional] 
**proxy** | [**CommonDefenderProxyOpt**](CommonDefenderProxyOpt.md) |  | [optional] 
**region** | **str** | Region is the kubernetes cluster location region.  | [optional] 
**secretsname** | **str** | SecretName is the secret.  | [optional] 
**selinux** | **bool** | SelinuxEnforced indicates whether selinux is enforced on the target host.  | [optional] 
**serviceaccounts** | **bool** | MonitorServiceAccounts indicates whether to monitor service accounts.  | [optional] 
**task_name** | **str** | TaskName is the name used for the task definition.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


