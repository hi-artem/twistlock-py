# TypesSettings

Settings are the global system settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_ca_cert** | **str** | AccessCACert is a custom CA certificate.  | [optional] 
**address** | **str** | Address is the intelligence service address.  | [optional] 
**alerts** | [**ApiAlertSettings**](ApiAlertSettings.md) |  | [optional] 
**cert_settings** | [**TypesCertSettings**](TypesCertSettings.md) |  | [optional] 
**certificate_period_days** | **int** | CertificatePeriodDays is the certificates period in days.  | [optional] 
**check_revocation** | **bool** | CheckRevocation indicates whether cert revocation status is required.  | [optional] 
**code_repo_settings** | [**SharedCodeRepoSettings**](SharedCodeRepoSettings.md) |  | [optional] 
**communication_port** | **int** | MgmtPortHttp is the console http port.  | [optional] 
**console_ca_cert** | **str** | ConsoleCACert is a custom CA certificate for the console.  | [optional] 
**console_custom_cert** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**console_names** | **list[str]** | ConsoleNames is a list of names to use when generating the console SAN certificate.  | [optional] 
**custom_endpoint** | **str** | CustomEndpoint is the user defined custom endpoint.  | [optional] 
**custom_endpoint_ca_cert** | **str** | CustomEndpointCACert is the custom CA cert bundle for trusting the custom endpoint.  | [optional] 
**custom_endpoint_credential_id** | **str** | CustomEndpointCredentialID is the custom endpoint credential ID.  | [optional] 
**custom_endpoint_enabled** | **bool** | CustomEndpointEnabled indicates that the user custom endpoint is enabled.  | [optional] 
**custom_labels** | [**SharedCustomLabelsSettings**](SharedCustomLabelsSettings.md) |  | [optional] 
**defender_settings** | [**DefenderSettings**](DefenderSettings.md) |  | [optional] 
**enabled** | **bool** | Enabled indicates whether intelligence service is enabled.  | [optional] 
**forensic** | [**SharedForensicSettings**](SharedForensicSettings.md) |  | [optional] 
**has_admin** | **bool** | HasAdmin indicates whether the admin account is initialized.  | [optional] 
**host_auto_deploy** | [**list[SharedHostAutoDeploySpecification]**](SharedHostAutoDeploySpecification.md) | HostAutoDeploySpecifications is a list of host auto-deploy specifications | [optional] 
**hpkp** | [**TypesHPKPSettings**](TypesHPKPSettings.md) |  | [optional] 
**identity_settings** | [**IdentitySettings**](IdentitySettings.md) |  | [optional] 
**kubernetes_audit** | [**SharedKubernetesAuditSettings**](SharedKubernetesAuditSettings.md) |  | [optional] 
**ldap_enabled** | **bool** | LdapEnabled indicates whether ldap is enabled.  | [optional] 
**license_key** | **str** | LicenseKey is the license key.  | [optional] 
**logging** | [**SharedLoggingSettings**](SharedLoggingSettings.md) |  | [optional] 
**logon** | [**TypesLogonSettings**](TypesLogonSettings.md) |  | [optional] 
**oauth_enabled** | **bool** | OauthEnabled indicates whether Oauth is enabled.  | [optional] 
**oidc_enabled** | **bool** | OidcEnabled indicates whether OpenID connect is enabled.  | [optional] 
**projects** | [**ApiProjectSettings**](ApiProjectSettings.md) |  | [optional] 
**proxy** | [**CommonProxySettings**](CommonProxySettings.md) |  | [optional] 
**registry** | [**SharedRegistrySettings**](SharedRegistrySettings.md) |  | [optional] 
**saml_enabled** | **bool** | SamlEnabled indicates whether saml is enabled.  | [optional] 
**scan** | [**SharedScanSettings**](SharedScanSettings.md) |  | [optional] 
**secrets_stores** | [**SharedSecretsStores**](SharedSecretsStores.md) |  | [optional] 
**secured_console_port** | **int** | MgmtPortHttps is the console https port.  | [optional] 
**serverless_auto_deploy** | [**list[SharedServerlessAutoDeploySpecification]**](SharedServerlessAutoDeploySpecification.md) | ServerlessAutoDeploySpecifications is a list of serverless auto-deploy specifications | [optional] 
**serverless_scan** | [**list[SharedServerlessScanSpecification]**](SharedServerlessScanSpecification.md) | ServerlessScan is the serverless scanning settings.  | [optional] 
**tas_droplets** | [**list[SharedTASDropletSpecification]**](SharedTASDropletSpecification.md) | TASDropletsSpecification is the TAS droplets scanning settings.  | [optional] 
**telemetry** | [**TypesTelemetrySettings**](TypesTelemetrySettings.md) |  | [optional] 
**token** | **str** | Token is the token used to access intelligence service.  | [optional] 
**trusted_certs** | [**list[SharedTrustedCertSignature]**](SharedTrustedCertSignature.md) | TrustedCerts is the list of trusted cert to allow in docker access scenarios.  | [optional] 
**trusted_certs_enabled** | **bool** | TrustedCertsEnabled indicates whether to enable the trusted certificate feature.  | [optional] 
**upload_disabled** | **bool** | UploadDisabled indicates whether logs uploading is disabled.  | [optional] 
**version** | **str** | Version is the current console version.  | [optional] 
**vms** | [**list[SharedVMSpecification]**](SharedVMSpecification.md) | VMSpecifications is a list of VM specifications | [optional] 
**wild_fire_settings** | [**SharedWildFireSettings**](SharedWildFireSettings.md) |  | [optional] 
**windows_feed_enabled** | **bool** | WindowsFeedEnabled indicates whether windows feed is enabled.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

