# RuntimeFilesystemRule

FilesystemRule represents restrictions/suppression for filesystem changes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backdoor_files** | **bool** | Monitors files that can create and/or persist backdoors (currently SSH and admin account config files) (true).  | [optional] 
**blacklist** | **list[str]** | List of denied file system path.  | [optional] 
**check_new_files** | **bool** | Detects changes to binaries and certificates (true).  | [optional] 
**effect** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**skip_encrypted_binaries** | **bool** | Indicates that encrypted binaries check should be skipped.  | [optional] 
**suspicious_elf_headers** | **bool** | Indicates whether malware detection based on suspicious ELF headers is enabled.  | [optional] 
**whitelist** | **list[str]** | List of allowed file system path.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


