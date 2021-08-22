# TypesVulnImpactedResources

VulnImpactedResources holds details about the resources impacted by vulnerability

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id is the CVE ID (index for the impacted resources).  | [optional] 
**functions** | **dict(str, str)** | Functions is a map between function id to its details.  | [optional] 
**hosts** | **list[str]** | Hosts is the list of impacted hosts.  | [optional] 
**risk_tree** | **dict(str, list)** | RiskTree is the risk tree associated with the CVE ID.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


