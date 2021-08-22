# RuntimeHostProfile

HostProfile represents a host runtime profile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is the profile ID (hostname).  | [optional] 
**account_id** | **str** | AccountID is the cloud account ID associated with the profile.  | [optional] 
**apps** | [**list[RuntimeApp]**](RuntimeApp.md) | Apps are the host&#39;s apps metadata.  | [optional] 
**collections** | **list[str]** | Collections is a list of collections to which this profile applies.  | [optional] 
**created** | **datetime** | Created is the profile creation time.  | [optional] 
**geoip** | [**RuntimeProfileNetworkGeoIP**](RuntimeProfileNetworkGeoIP.md) |  | [optional] 
**hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**labels** | **list[str]** | Labels are the labels associated with the profile.  | [optional] 
**ssh_events** | [**list[RuntimeSSHEvent]**](RuntimeSSHEvent.md) | SSHEvents represents a list SSH events occurred on the host.  | [optional] 
**time** | **datetime** | Time is the last time when this profile was modified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


