# IstioAuthorizationPolicyRule

AuthorizationPolicyRule is a compact version of Istio Rule resource See https://istio.io/docs/reference/config/security/authorization-policy/#Rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | [**list[IstioAuthorizationPolicyDestination]**](IstioAuthorizationPolicyDestination.md) | Destinations are the endpoint definitions the rule grants access to.  | [optional] 
**sources** | [**list[IstioAuthorizationPolicySource]**](IstioAuthorizationPolicySource.md) | Sources are the metadatas of the services the rule grants access to.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


