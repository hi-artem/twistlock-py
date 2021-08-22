# TypesGroup

Group represents a console group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Group name.  | [optional] 
**group_id** | **str** | Group identifier in the Azure SAML identification process.  | [optional] 
**group_name** | **str** | Group name.  | [optional] 
**last_modified** | **datetime** | Datetime when the group was created or last modified.  | [optional] 
**ldap_group** | **bool** | Indicates if the group is an LDAP group (true) or not (false).  | [optional] 
**oauth_group** | **bool** | Indicates if the group is an OAuth group (true) or not (false).  | [optional] 
**oidc_group** | **bool** | Indicates if the group is an OpenID Connect group (true) or not (false).  | [optional] 
**owner** | **str** | User who created or modified the group.  | [optional] 
**permissions** | [**list[ApiPermission]**](ApiPermission.md) | Permissions is a list of permissions | [optional] 
**role** | **str** | Role of the group.  | [optional] 
**saml_group** | **bool** | Indicates if the group is a SAML group (true) or not (false).  | [optional] 
**user** | [**list[SharedUser]**](SharedUser.md) | Users in the group.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


