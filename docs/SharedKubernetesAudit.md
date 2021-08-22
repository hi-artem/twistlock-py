# SharedKubernetesAudit

KubernetesAudit represents a Kubernetes audit - this is the data that is stored for matched audits

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_techniques** | [**list[MitreTechnique]**](MitreTechnique.md) | AttackTechniques are the MITRE attack techniques.  | [optional] 
**authorization_info** | **dict(str, str)** | AuthorizationInfo holds the original event authorization info.  | [optional] 
**event_blob** | **str** | EventBlob is the original event that caused this audit.  | [optional] 
**message** | **str** | Message is the user defined message which appears on audit.  | [optional] 
**request_uri** | **str** | RequestURI is the request URI as sent by the client to a server.  | [optional] 
**resources** | **str** | Resource represents the resource that is impacted by this event.  | [optional] 
**source_ips** | **list[str]** | Source IPs, from where the request originated and intermediate proxies (optional).  | [optional] 
**time** | **datetime** | Time is the time at which the request was generated.  | [optional] 
**user** | [**SharedKubernetesEventUserInfo**](SharedKubernetesEventUserInfo.md) |  | [optional] 
**verb** | **str** | Verb is the kubernetes verb associated with the request.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


