# WaasHeaderSpec

HeaderSpec is specification for a single header and its allowed or blocked values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **bool** | Indicates if the flow is to be allowed (true) or blocked (false).  | [optional] 
**effect** | [**WaasEffect**](WaasEffect.md) |  | [optional] 
**name** | **str** | Header name.  | [optional] 
**required** | **bool** | Indicates if the header must be present (true) or not (false).  | [optional] 
**values** | **list[str]** | Wildcard expressions that represent the header value.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


