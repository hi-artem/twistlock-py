# IstioAuthorizationPolicy

AuthorizationPolicy is a compact version of Istio AuthorizationPolicy resource See https://istio.io/docs/reference/config/security/authorization-policy/#AuthorizationPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | [**CommonEffect**](CommonEffect.md) |  | [optional] 
**name** | **str** | Name is the authorization policy name.  | [optional] 
**namespace** | **str** | Namespace is the namespace of the authorization policy.  | [optional] 
**rules** | [**list[IstioAuthorizationPolicyRule]**](IstioAuthorizationPolicyRule.md) | Rules are the access rules this authorization policy defines.  | [optional] 
**target_services** | [**list[IstioAuthorizationPolicyService]**](IstioAuthorizationPolicyService.md) | TargetServices is the list of services the authorization policy applies on.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


