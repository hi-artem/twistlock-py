# ServerlessRadarEntity

RadarEntity is the extended serverless radar entity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is unique identifier of the function (for AWS - ARN).  | [optional] 
**account_id** | **str** | AccountID is the cloud account ID.  | [optional] 
**alias** | **bool** | Alias states that the current entity is an alias of the function.  | [optional] 
**application_name** | **str** | ApplicationName is the name of the application the function is associated with.  | [optional] 
**associated_versions** | [**list[ServerlessAssociatedVersion]**](ServerlessAssociatedVersion.md) | AssociatedVersions contain the alias associated versions, or empty if the entity isn&#39;t an alias.  | [optional] 
**collections** | **list[str]** | Collections are the matched function collections.  | [optional] 
**compliance_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 
**credential_id** | **str** | CredentialID is the id reference of the credential used.  | [optional] 
**defended** | **bool** | Defended denotes weather the function is defended by a serverless defender.  | [optional] 
**description** | **str** | Description is the user provided description of the function.  | [optional] 
**incident_count** | **int** | IncidentCount is the number of incidents.  | [optional] 
**last_modified** | **datetime** | LastModified is the modification time of the function.  | [optional] 
**name** | **str** | Name is the name of the function.  | [optional] 
**network_count** | **int** | NetworkCount contain the runtime network events count.  | [optional] 
**permissions** | [**list[ServerlessPermissions]**](ServerlessPermissions.md) | Permissions are the function permissions.  | [optional] 
**permissions_boundary** | [**list[ServerlessPermissions]**](ServerlessPermissions.md) | PermissionsBoundary are limitations of the permissions, acting as AND.  | [optional] 
**processes_count** | **int** | ProcessesCount contain the runtime processes events count.  | [optional] 
**provider** | [**CommonCloudProvider**](CommonCloudProvider.md) |  | [optional] 
**region** | **str** | Region is the region that was scanned, for example: GCP - \&quot;us-east-1\&quot;, Azure - \&quot;westus\&quot;.  | [optional] 
**runtime** | **str** | Runtime is runtime environment for the function, i.e. nodejs.  | [optional] 
**scanned** | **bool** | Scanned indicates if the function was scanned for vulnerabilities and compliance.  | [optional] 
**tags** | [**list[CommonExternalLabel]**](CommonExternalLabel.md) | Tags are the cloud provider metadata tags.  | [optional] 
**triggers** | [**list[ServerlessTriggers]**](ServerlessTriggers.md) | Triggers contain invocation paths for functions.  | [optional] 
**version** | **str** | Version is the version of the function, or the alias name if it&#39;s an alias.  | [optional] 
**vulnerability_distribution** | [**VulnDistribution**](VulnDistribution.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


