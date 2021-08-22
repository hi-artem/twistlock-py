# SharedAppFirewallAudit

AppFirewallAudit represents a firewall audit event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID is internal id representation.  | [optional] 
**account_id** | **str** | AccountID is the cloud account ID where the audit was generated.  | [optional] 
**app_id** | **str** | AppID is the  application ID.  | [optional] 
**attack_techniques** | [**list[MitreTechnique]**](MitreTechnique.md) | AttackTechniques are the MITRE attack techniques.  | [optional] 
**cluster** | **str** | Cluster is the cluster on which the audit was originated.  | [optional] 
**collections** | **list[str]** | Collections are collections to which this audit applies.  | [optional] 
**connecting_ips** | **list[str]** | ConnectingIPs are the requests connecting IPs such as proxy and load-balancer.  | [optional] 
**container_id** | **str** | ContainerId is the firewall container id.  | [optional] 
**container_name** | **str** | ContainerName is the firewall container name.  | [optional] 
**count** | **int** | Count is the number of audit occurrences.  | [optional] 
**country** | **str** | Country is the source IP country.  | [optional] 
**effect** | [**WaasEffect**](WaasEffect.md) |  | [optional] 
**fqdn** | **str** | FQDN is the current hostname&#39;s FQDN.  | [optional] 
**function** | **str** | Function is the name of the serverless function that caused the audit.  | [optional] 
**function_id** | **str** | FunctionID is the id of the function called.  | [optional] 
**host** | **bool** | Host indicates this audit if for a host firewall.  | [optional] 
**hostname** | **str** | Hostname is the current hostname.  | [optional] 
**image_name** | **str** | ImageName is the firewall image name.  | [optional] 
**labels** | **dict(str, str)** | Labels are the custom labels associated with the container.  | [optional] 
**method** | **str** | HTTPMethod is the request HTTP method.  | [optional] 
**msg** | **str** | Message is the blocking message text.  | [optional] 
**ns** | **list[str]** | Namespaces are the k8s namespaces.  | [optional] 
**os** | **str** | OS is the operating system distribution.  | [optional] 
**profile_id** | **str** | ProfileID is the profile of the audit.  | [optional] 
**protection** | [**WaasProtection**](WaasProtection.md) |  | [optional] 
**raw_event** | **str** | RawEvent contains unparsed function handler event input.  | [optional] 
**region** | **str** | Region is the name of the region in which the serverless function is located.  | [optional] 
**request_header_names** | **list[str]** | RequestHeaderNames are the request header names.  | [optional] 
**request_headers** | **str** | RequestHeaders represent the request headers.  | [optional] 
**request_host** | **str** | RequestHost is the request host.  | [optional] 
**request_id** | **str** | RequestID is lambda function invocation request id.  | [optional] 
**resource** | [**CommonRuntimeResource**](CommonRuntimeResource.md) |  | [optional] 
**response_header_names** | **list[str]** | ResponseHeaderNames are the response header names.  | [optional] 
**rule_app_id** | **str** | RuleAppID is the ID of the rule&#39;s app that was applied.  | [optional] 
**rule_name** | **str** | RuleName is the name of the rule that was applied.  | [optional] 
**runtime** | [**SharedLambdaRuntimeType**](SharedLambdaRuntimeType.md) |  | [optional] 
**status_code** | **int** | StatusCode is the response status code.  | [optional] 
**subnet** | **str** | Subnet is the source IP subnet.  | [optional] 
**time** | **datetime** | Time is the UTC time of the audit event.  | [optional] 
**type** | [**WaasAttackType**](WaasAttackType.md) |  | [optional] 
**url** | **str** | URL is the requests full URL (partial on server side - path and query only).  | [optional] 
**url_path** | **str** | URLPath is the requests url path.  | [optional] 
**url_query** | **str** | URLQuery is the requests url query.  | [optional] 
**user_agent_header** | **str** | UserAgentHeader is the requests User-Agent header.  | [optional] 
**version** | **str** | Version is the defender version.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


