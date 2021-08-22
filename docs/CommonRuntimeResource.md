# CommonRuntimeResource

RuntimeResource represents on which resource in the system a rule applies (e.g., specific host or image) Empty resource or wildcard (*) represents all resources of a given type

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **list[str]** | List of account IDs.  | [optional] 
**app_ids** | **list[str]** | List of application IDs.  | [optional] 
**clusters** | **list[str]** | List of Kubernetes cluster names.  | [optional] 
**code_repos** | **list[str]** | List of code repositories.  | [optional] 
**containers** | **list[str]** | List of containers.  | [optional] 
**functions** | **list[str]** | List of functions.  | [optional] 
**hosts** | **list[str]** | List of  hosts.  | [optional] 
**images** | **list[str]** | List of images.  | [optional] 
**labels** | **list[str]** | List of labels.  | [optional] 
**namespaces** | **list[str]** | List of Kubernetes namespaces.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


