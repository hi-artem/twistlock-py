# RuntimeProfileProcess

ProfileProcess represents a single process data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** | Command is the executed command.  | [optional] 
**md5** | **str** | MD5 is the process binary MD5 sum.  | [optional] 
**modified** | **bool** | Modified indicates the process binary was modified after the container has started.  | [optional] 
**path** | **str** | Path is the process binary path.  | [optional] 
**ppath** | **str** | PPath is the parent process path.  | [optional] 
**time** | **datetime** | Time is the time in which the process was added. If the process was modified, Time is the modification time.  | [optional] 
**user** | **str** | User represents the username that started the process.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


