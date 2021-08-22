# SharedInstalledProducts

InstalledProducts contains data regarding products running in environment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apache** | **str** | Apache indicates the apache server version, empty in case apache not running.  | [optional] 
**aws_cloud** | **bool** | AWSCloud indicates whether AWS cloud is used.  | [optional] 
**crio** | **bool** | CRI indicates whether the container runtime is CRI (and not docker).  | [optional] 
**docker** | **str** | Docker represents the docker daemon version.  | [optional] 
**docker_enterprise** | **bool** | DockerEnterprise indicates whether the enterprise version of Docker is installed.  | [optional] 
**has_package_manager** | **bool** | HasPackageManager indicates whether package manager is installed on the OS.  | [optional] 
**k8s_api_server** | **bool** | K8sApiServer indicates whether a kubernetes api server is running.  | [optional] 
**k8s_controller_manager** | **bool** | K8sControllerManager indicates whether a kubernetes controller manager is running.  | [optional] 
**k8s_etcd** | **bool** | K8sEtcd indicates whether etcd is running.  | [optional] 
**k8s_federation_api_server** | **bool** | K8sFederationApiServer indicates whether a federation api server is running.  | [optional] 
**k8s_federation_controller_manager** | **bool** | K8sFederationControllerManager indicates whether a federation controller manager is running.  | [optional] 
**k8s_kubelet** | **bool** | K8sKubelet indicates whether kubelet is running.  | [optional] 
**k8s_proxy** | **bool** | K8sProxy indicates whether a kubernetes proxy is running.  | [optional] 
**k8s_scheduler** | **bool** | K8sScheduler indicates whether the a kubernetes scheduler is running.  | [optional] 
**kubernetes** | **str** | Kubernetes represents the kubernetes version.  | [optional] 
**openshift** | **bool** | Openshift indicates whether openshift is deployed.  | [optional] 
**os_distro** | **str** | OSDistro specifies the os distribution.  | [optional] 
**serverless** | **bool** | Serverless indicates whether evaluated on a serverless environment.  | [optional] 
**swarm_manager** | **bool** | SwarmManager indicates whether a swarm manager is running.  | [optional] 
**swarm_node** | **bool** | SwarmNode indicates whether the node is part of an active swarm.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


