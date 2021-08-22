# TypesRegistryWebhookRequest

RegistryWebhookRequest is a registry scanning webhook request. Schema supports multiple webhook providers: https://docs.docker.com/docker-hub/webhooks/ https://docs.docker.com/registry/notifications/

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action is the webhook action.  | [optional] 
**artifactory** | **object** | ArtifactoryWebhookRequest is an artifactory webhook request Artifactory doesn&#39;t have native webhook support, instead it comes as a plugin https://github.com/jfrog/artifactory-user-plugins/tree/master/webhook The relevant fields in the this struct were reverse engineered from the webhook groovy code and from the fields that were sent by a real artifactory environment | [optional] 
**type** | **str** | Type is the event type (Harbor registry).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


