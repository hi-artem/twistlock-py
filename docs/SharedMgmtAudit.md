# SharedMgmtAudit

MgmtAudit represents a management audit in the system

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api** | **str** | API is the api used in the audit process.  | [optional] 
**diff** | **str** | Diff is the diff between old and new values.  | [optional] 
**failure** | **bool** | Failure states whether the request failed or not.  | [optional] 
**source_ip** | **str** | SourceIP is the request&#39;s source IP.  | [optional] 
**status** | **str** | Status is the request&#39;s response status.  | [optional] 
**time** | **datetime** | Time is the time of the request.  | [optional] 
**type** | [**SharedMgmtType**](SharedMgmtType.md) |  | [optional] 
**username** | **str** | Username is the username of the user who performed the action.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


