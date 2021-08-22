# IstioAuthorizationPolicyDestination

AuthorizationPolicyDestination is a compact version of Istio Operation resource See https://istio.io/docs/reference/config/security/authorization-policy/#Operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | **list[str]** | Methods are the destination endpoint HTTP methods, such as: \&quot;GET\&quot;, \&quot;POST\&quot;.  | [optional] 
**paths** | **list[str]** | Paths are the destination HTTP paths.  | [optional] 
**ports** | **list[int]** | Ports are the destination endpoint ports.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


