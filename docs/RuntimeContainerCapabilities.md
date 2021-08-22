# RuntimeContainerCapabilities

ContainerCapabilities are a set of static capabilities for a given container

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ci** | **bool** | CI indicates the container allowed to write binaries to disk and run them.  | [optional] 
**cloud_metadata** | **bool** | CloudMetadata indicates the given container can query cloud metadata api.  | [optional] 
**dns_cache** | **bool** | DNSCache are DNS services that are used by all the pods in the cluster.  | [optional] 
**dynamic_dns_query** | **bool** | DynamicDNSQuery indicates capped behavioral dns queries.  | [optional] 
**dynamic_file_creation** | **bool** | DynamicFileCreation indicates capped behavioral filesystem paths.  | [optional] 
**dynamic_process_creation** | **bool** | DynamicProcessCreation indicates capped behavioral processes.  | [optional] 
**k8s** | **bool** | Kubernetes indicates the given container can perform k8s networking tasks (e.g., contact to api server).  | [optional] 
**proxy** | **bool** | Proxy indicates the container can listen on any port and perform multiple outbound connection.  | [optional] 
**sshd** | **bool** | Sshd indicates whether the container can run sshd process.  | [optional] 
**unpacker** | **bool** | Unpacker indicates the container is allowed to write shared libraries to disk.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


