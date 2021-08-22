# ApiUserAuthMetadata

UserAuthMetadata represents the authenticated user, including its roles, groups and projects

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **list[str]** | Groups holds the user groups.  | [optional] 
**permissions** | [**list[ApiPermission]**](ApiPermission.md) | Permissions is a list of permissions | [optional] 
**prisma_role_name** | **str** | PrismaRoleName is the unique user defined name given to the role in Prisma Cloud.  | [optional] 
**role** | **str** | Role is the role of the user in the system e.g. Admin, DevOps etc..  | [optional] 
**role_perms** | **list[str]** | BitMap holds permissions set as a bitmap each byte in the slice hold access bits of several permissions | [optional] 
**user** | **str** | User is the identifier.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


