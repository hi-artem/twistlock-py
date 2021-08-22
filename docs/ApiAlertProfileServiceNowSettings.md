# ApiAlertProfileServiceNowSettings

AlertProfileServiceNowSettings represents the ServiceNow provider alert profile settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | [**ApiServiceNowApp**](ApiServiceNowApp.md) |  | [optional] 
**assignee** | **str** | Assignee is the ServiceNow user to whom will assign ServiceNow incidents\\items.  | [optional] 
**assignment_group** | **str** | AssignmentGroup is the ServiceNow group of users handling security incidents.  | [optional] 
**audit_priority** | **str** | AuditPriority is the priority at which to set audit alerts in security incidents.  | [optional] 
**ca_cert** | **str** | CA certificate for on-premise ssl (optional).  | [optional] 
**credential_id** | **str** | CredentialID is the ServiceNow authentication credentials id.  | [optional] 
**enabled** | **bool** | Enabled is the ServiceNow provider enabled/disabled indicator.  | [optional] 
**project** | **str** | Project is the name of the prisma compute project that was used to generate this configuration. It&#39;s required as secondary consoles do not store their project name.  | [optional] 
**security_incident_base_url** | **str** | SecurityIncidentBaseURL is the ServiceNow address, used to send security incidents.  | [optional] 
**vulnerability_endpoint_url** | **str** | VulnerabilityEndpointURL to report ServiceNow vulnerabilities, customer defined scripted REST API, see: https://docs.servicenow.com/bundle/orlando-application-development/page/integrate/custom-web-services/concept/c_CustomWebServices.html.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


