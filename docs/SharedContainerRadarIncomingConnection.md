# SharedContainerRadarIncomingConnection

ContainerRadarIncomingConnection is an incoming connection in the network radar

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_rules** | [**list[CnnfRadarPolicyRule]**](CnnfRadarPolicyRule.md) | PolicyRules are the policy rules that are applicable for source/dest. Used for radar display of connections deduced from policy rules.  | [optional] 
**ports** | [**list[CommonPortData]**](CommonPortData.md) | Ports are all the ports used by the sender.  | [optional] 
**profile_hash** | **int** | ProfileHash represents the profile hash It is allowed to contain up to uint32 numbers, and represented by int64 since mongodb does not support unsigned data types | [optional] 
**profile_id** | **str** | ProfileID is the sender&#39;s profile ID.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


