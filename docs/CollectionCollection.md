# CollectionCollection

Collection is a collection of resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **list[str]** | List of account IDs.  | [optional] 
**app_ids** | **list[str]** | List of application IDs.  | [optional] 
**clusters** | **list[str]** | List of Kubernetes cluster names.  | [optional] 
**code_repos** | **list[str]** | List of code repositories.  | [optional] 
**color** | **str** | Color is a color code for a collection | [optional] 
**containers** | **list[str]** | List of containers.  | [optional] 
**description** | **str** | Free-form text.  | [optional] 
**functions** | **list[str]** | List of functions.  | [optional] 
**hosts** | **list[str]** | List of  hosts.  | [optional] 
**images** | **list[str]** | List of images.  | [optional] 
**labels** | **list[str]** | List of labels.  | [optional] 
**modified** | **datetime** | Datetime when the collection was last modified.  | [optional] 
**name** | **str** | Collection name. Must be unique.  | [optional] 
**namespaces** | **list[str]** | List of Kubernetes namespaces.  | [optional] 
**owner** | **str** | User who created or last modified the collection.  | [optional] 
**prisma** | **bool** | Indicates whether this collection originates from Prisma Cloud.  | [optional] 
**system** | **bool** | Indicates whether this collection was created by the system (i.e., a non user) (true) or a real user (false).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


