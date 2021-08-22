# IdentityLdapSettings

LdapSettings are the ldap connectivity settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_password** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**account_upn** | **str** | AccountUpn is the user principle name used to connect to the active directory server.  | [optional] 
**ca_cert** | **str** | CaCert is cert in PEM format (optional, if not specified, skip_verify flag will be used).  | [optional] 
**enabled** | **bool** | Enabled indicates whether LDAP is enabled.  | [optional] 
**group_search_base** | **str** | GroupSearchBase is the LDAP search pattern for groups.  | [optional] 
**search_base** | **str** | SearchBase is the LDAP search pattern.  | [optional] 
**type** | **str** | Type specifies the LDAP server type (AD or OpenLDAP).  | [optional] 
**url** | **str** | Url is the ldap server url.  | [optional] 
**user_search_base** | **str** | UserSearchBase is the LDAP search pattern for users.  | [optional] 
**user_search_identifier** | **str** | UserSearchIdentifier is the user identifier to use for querying open ldap (e.g., cn -&gt; cn&#x3D;user).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


