# SharedKubernetesAuditSettings

KubernetesAuditSettings represents the audit kubernetes settings. Separate from Kubernetes audit policy to allow for scale project defined settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** | CredentialID is the credential that is used to fetch k8s audit data from external resources (e.g., Stackdriver).  | [optional] 
**deployment_type** | [**SharedKubernetesDeploymentType**](SharedKubernetesDeploymentType.md) |  | [optional] 
**last_polling_time** | **datetime** | LastPollingTime holds the last time the logs were polled from Stackdriver.  | [optional] 
**project_ids** | **list[str]** | ProjectIDs are the GKE project IDs used to query stackdriver log entries.  | [optional] 
**stackdriver_filter** | **str** | StackdriverFilter is the advanced filter used for Stackdriver querying.  | [optional] 
**webhook_url_suffix** | **str** | WebhookSuffix is the relative path to the webhook http endpoint.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


