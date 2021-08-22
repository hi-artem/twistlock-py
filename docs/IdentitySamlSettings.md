# IdentitySamlSettings

SamlSettings are the saml connectivity settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | AppID is the Azure application ID.  | [optional] 
**app_secret** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**audience** | **str** | Audience specifies the SAML audience used in the verification of the SAML response.  | [optional] 
**cert** | **str** | Cert is idp certificate in PEM format.  | [optional] 
**console_url** | **str** | ConsoleURL is the external Console URL that is used by the IDP for routing the browser after login.  | [optional] 
**enabled** | **bool** | Enabled indicates whether saml settings are enabled.  | [optional] 
**issuer** | **str** | Issuer is idp issuer id.  | [optional] 
**provider_alias** | **str** | ProviderAlias is the provider alias used for display.  | [optional] 
**skip_authn_context** | **bool** | SkipAuthnContext indicates whether request authentication contexts should be skipped.  | [optional] 
**tenant_id** | **str** | TenantID is the Azure Tenant ID.  | [optional] 
**type** | [**IdentitySamlType**](IdentitySamlType.md) |  | [optional] 
**url** | **str** | Url is idp sso url.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


