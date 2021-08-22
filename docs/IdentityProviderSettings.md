# IdentityProviderSettings

ProviderSettings are the Oauth/ OpenID Connect connectivity settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** | AuthURL specifies auth URL.  | [optional] 
**cert** | **str** | Cert is idp certificate.  | [optional] 
**client_id** | **str** | ClientID is the client identifier issued to the client during the registration process.  | [optional] 
**client_secret** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**enabled** | **bool** | Enabled indicates whether Auth settings are enabled.  | [optional] 
**group_claim** | **str** | GroupClaim is the name of the group claim property in user info response.  | [optional] 
**group_scope** | **str** | GroupScope specifies name of group scope.  | [optional] 
**open_id_issues_url** | **str** | OpenIDIssuesURL is the base URL for OpenID connect providers.  | [optional] 
**openshift_base_url** | **str** | OpenshiftBaseURL is openshift base URL.  | [optional] 
**provider_alias** | **str** | ProviderAlias is the provider alias used for display.  | [optional] 
**provider_name** | [**IdentityProviderName**](IdentityProviderName.md) |  | [optional] 
**token_url** | **str** | TokenURL specifies token URL.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


