# SharedHostRadarIncomingConnection

HostRadarIncomingConnection is the incoming connection between two apps in two hosts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_host** | **str** | DstHost is the src hostname.  | [optional] 
**policy_rules** | [**list[CnnfRadarPolicyRule]**](CnnfRadarPolicyRule.md) | PolicyRules are the policy rules that are applicable for source/dest. Used for radar display of connections deduced from policy rules.  | [optional] 
**ports** | [**list[CommonPortData]**](CommonPortData.md) | Ports are the destination ports.  | [optional] 
**src_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**src_host** | **str** | SrcHost is the src hostname.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


