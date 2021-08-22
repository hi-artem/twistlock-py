# PrismaIaCParameters

IaCParameters is prisma's IaC parameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **list[str]** | Files is an optional list of files that should be scan from the repo.  | [optional] 
**folders** | **list[str]** | Folders is an optional list of folders that should be scanned from the repo.  | [optional] 
**policy_id_filters** | **list[str]** | PolicyIDFilters is an optional list of user provided policy IDs that the scan should filter.  | [optional] 
**variable_files** | **list[str]** | VariableFiles is a list of files that can include variables for deducing values inside IaC files {\&quot;variablefiles\&quot; : [\&quot;myvariables.tf\&quot;,...]}.  | [optional] 
**variables** | **dict(str, str)** | Variables represents key value variables used for deducing variable values inside IaC files.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


