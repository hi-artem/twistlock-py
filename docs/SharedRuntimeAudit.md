# SharedRuntimeAudit

RuntimeAudit represents a runtime audit event (fires when a runtime policy is violated)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal ID (used for in-place updates).  | [optional] 
**account_id** | **str** | ID of the cloud account where the audit was generated.  | [optional] 
**app** | **str** | Name of the service which violated the host policy.  | [optional] 
**app_id** | **str** | Application ID.  | [optional] 
**attack_techniques** | [**list[MitreTechnique]**](MitreTechnique.md) | MITRE attack techniques.  | [optional] 
**attack_type** | [**SharedRuntimeAttackType**](SharedRuntimeAttackType.md) |  | [optional] 
**cluster** | **str** | Cluster name.  | [optional] 
**collections** | **list[str]** | Collections to which this audit applies.  | [optional] 
**container** | **bool** | Indicates if this is a container audit (true) or host audit (false).  | [optional] 
**container_id** | **str** | ID of the container that violates the rule.  | [optional] 
**container_name** | **str** | Container name.  | [optional] 
**count** | **int** | Attack type audits count.  | [optional] 
**country** | **str** | Outbound country for outgoing network audits.  | [optional] 
**effect** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**err** | **str** | Unknown error in the audit process.  | [optional] 
**fqdn** | **str** | Current full domain name used in audit alerts.  | [optional] 
**function** | **str** | Name of the serverless function that caused the audit.  | [optional] 
**function_id** | **str** | ID of the function invoked.  | [optional] 
**hostname** | **str** | Current hostname.  | [optional] 
**image_id** | **str** | Container image ID.  | [optional] 
**image_name** | **str** | Container image name.  | [optional] 
**interactive** | **bool** | Indicates if the audit was triggered from a process that was spawned in interactive mode (e.g., docker exec ...) (true) or not (false).  | [optional] 
**label** | **str** | Container deployment label.  | [optional] 
**labels** | **dict(str, str)** | Custom labels which augment the audit data.  | [optional] 
**msg** | **str** | Blocking message text.  | [optional] 
**namespace** | **str** | K8s deployment namespace.  | [optional] 
**os** | **str** | Operating system distribution.  | [optional] 
**pid** | **int** | ID of the process that caused the audit event.  | [optional] 
**process_path** | **str** | Path of the process that caused the audit event.  | [optional] 
**profile_id** | **str** | Profile of the audit.  | [optional] 
**raw_event** | **str** | Unparsed function handler event input.  | [optional] 
**region** | **str** | Name of the region in which the serverless function is located.  | [optional] 
**request_id** | **str** | ID of the lambda function invocation request.  | [optional] 
**rule_name** | **str** | Name of the rule that was applied, if blocked.  | [optional] 
**runtime** | [**SharedLambdaRuntimeType**](SharedLambdaRuntimeType.md) |  | [optional] 
**severity** | [**SharedRuntimeSeverity**](SharedRuntimeSeverity.md) |  | [optional] 
**time** | **datetime** | Time of the audit event (in UTC time).  | [optional] 
**type** | [**SharedRuntimeType**](SharedRuntimeType.md) |  | [optional] 
**user** | **str** | Service user.  | [optional] 
**version** | **str** | Defender version.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


