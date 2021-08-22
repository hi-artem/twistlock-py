# RuntimeProcessesRule

ProcessesRule represents restrictions/suppression for running processes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklist** | **list[str]** | List of processes to deny.  | [optional] 
**block_all_binaries** | **bool** | Indicates that all processes are blocked except the main process.  | [optional] 
**check_crypto_miners** | **bool** | Detect crypto miners.  | [optional] 
**check_lateral_movement** | **bool** | Indicates whether dectection of processes that can be used for lateral movement exploits is enabled.  | [optional] 
**check_new_binaries** | **bool** | Indicates whether binaries which do not belong to the original image are allowed to run.  | [optional] 
**check_parent_child** | **bool** | Indicates whether checking for parent child relationship when comparing spawned processes in the model is enabled.  | [optional] 
**check_suid_binaries** | **bool** | Indicates whether check for process elevating privileges is enabled (SUID bit).  | [optional] 
**effect** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**skip_modified** | **bool** | Indicates whether to trigger audits/incidents when a modified proc is spawned.  | [optional] 
**skip_reverse_shell** | **bool** | Indicates whether reverse shell detection is disabled.  | [optional] 
**whitelist** | **list[str]** | List of processes to allow.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


