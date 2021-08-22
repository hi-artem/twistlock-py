# ApiPermission

Permission represents a user or group's permission to access a specific resource. Currently supported resources are: - Project - Access to a specific project (if empty, the Master Project by default) - Collection - The set of collections in the project that may be accessed (all if empty) If no permissions are assigned, all projects and collections may be accessed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | **list[str]** | List of collections the user can access.  | [optional] 
**project** | **str** | Names of projects which the user can access.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


