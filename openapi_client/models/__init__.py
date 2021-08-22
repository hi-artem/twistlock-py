# coding: utf-8

# flake8: noqa
"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from openapi_client.models.admission_audit import AdmissionAudit
from openapi_client.models.admission_policy import AdmissionPolicy
from openapi_client.models.admission_rule import AdmissionRule
from openapi_client.models.api_alert_profile import ApiAlertProfile
from openapi_client.models.api_alert_profile_email_settings import ApiAlertProfileEmailSettings
from openapi_client.models.api_alert_profile_gcp_pubsub_settings import ApiAlertProfileGcpPubsubSettings
from openapi_client.models.api_alert_profile_jira_settings import ApiAlertProfileJIRASettings
from openapi_client.models.api_alert_profile_pager_duty_settings import ApiAlertProfilePagerDutySettings
from openapi_client.models.api_alert_profile_security_advisor import ApiAlertProfileSecurityAdvisor
from openapi_client.models.api_alert_profile_security_center_settings import ApiAlertProfileSecurityCenterSettings
from openapi_client.models.api_alert_profile_security_hub_settings import ApiAlertProfileSecurityHubSettings
from openapi_client.models.api_alert_profile_service_now_settings import ApiAlertProfileServiceNowSettings
from openapi_client.models.api_alert_profile_slack_settings import ApiAlertProfileSlackSettings
from openapi_client.models.api_alert_profile_webhook_settings import ApiAlertProfileWebhookSettings
from openapi_client.models.api_alert_profile_xsoar_settings import ApiAlertProfileXSOARSettings
from openapi_client.models.api_alert_rule import ApiAlertRule
from openapi_client.models.api_alert_settings import ApiAlertSettings
from openapi_client.models.api_alert_type import ApiAlertType
from openapi_client.models.api_auth_type import ApiAuthType
from openapi_client.models.api_authentication_request import ApiAuthenticationRequest
from openapi_client.models.api_defender_install_script_options import ApiDefenderInstallScriptOptions
from openapi_client.models.api_impersonated_user_req import ApiImpersonatedUserReq
from openapi_client.models.api_impersonated_user_resp import ApiImpersonatedUserResp
from openapi_client.models.api_init_status import ApiInitStatus
from openapi_client.models.api_jira_dynamic_field import ApiJIRADynamicField
from openapi_client.models.api_jira_dynamic_labels import ApiJIRADynamicLabels
from openapi_client.models.api_license_request import ApiLicenseRequest
from openapi_client.models.api_pager_duty_alert_severity import ApiPagerDutyAlertSeverity
from openapi_client.models.api_permission import ApiPermission
from openapi_client.models.api_project_settings import ApiProjectSettings
from openapi_client.models.api_resolve_functions_req import ApiResolveFunctionsReq
from openapi_client.models.api_resolve_functions_resp import ApiResolveFunctionsResp
from openapi_client.models.api_resolve_images_req import ApiResolveImagesReq
from openapi_client.models.api_resolve_images_resp import ApiResolveImagesResp
from openapi_client.models.api_service_now_app import ApiServiceNowApp
from openapi_client.models.api_user import ApiUser
from openapi_client.models.api_user_auth_metadata import ApiUserAuthMetadata
from openapi_client.models.cnnf_allow_all_connections import CnnfAllowAllConnections
from openapi_client.models.cnnf_container_audit import CnnfContainerAudit
from openapi_client.models.cnnf_host_audit import CnnfHostAudit
from openapi_client.models.cnnf_network_entity import CnnfNetworkEntity
from openapi_client.models.cnnf_network_firewall_attack_type import CnnfNetworkFirewallAttackType
from openapi_client.models.cnnf_policy import CnnfPolicy
from openapi_client.models.cnnf_radar_connection_instance import CnnfRadarConnectionInstance
from openapi_client.models.cnnf_radar_connection_instances import CnnfRadarConnectionInstances
from openapi_client.models.cnnf_radar_policy_rule import CnnfRadarPolicyRule
from openapi_client.models.cnnf_rule import CnnfRule
from openapi_client.models.cnnf_rule_entity_type import CnnfRuleEntityType
from openapi_client.models.cnnf_subnet import CnnfSubnet
from openapi_client.models.coderepos_manifest_file import CodereposManifestFile
from openapi_client.models.coderepos_pkg_dependency import CodereposPkgDependency
from openapi_client.models.coderepos_repository import CodereposRepository
from openapi_client.models.coderepos_scan_result import CodereposScanResult
from openapi_client.models.collection_collection import CollectionCollection
from openapi_client.models.collection_usage import CollectionUsage
from openapi_client.models.collection_usage_type import CollectionUsageType
from openapi_client.models.common_cloud_metadata import CommonCloudMetadata
from openapi_client.models.common_cloud_provider import CommonCloudProvider
from openapi_client.models.common_daemon_set_options import CommonDaemonSetOptions
from openapi_client.models.common_defender_proxy_opt import CommonDefenderProxyOpt
from openapi_client.models.common_effect import CommonEffect
from openapi_client.models.common_external_label import CommonExternalLabel
from openapi_client.models.common_external_label_source_type import CommonExternalLabelSourceType
from openapi_client.models.common_host_forensic_settings import CommonHostForensicSettings
from openapi_client.models.common_network_device_ip import CommonNetworkDeviceIP
from openapi_client.models.common_policy_effect import CommonPolicyEffect
from openapi_client.models.common_port_data import CommonPortData
from openapi_client.models.common_port_range import CommonPortRange
from openapi_client.models.common_profile_port import CommonProfilePort
from openapi_client.models.common_profile_port_data import CommonProfilePortData
from openapi_client.models.common_proxy_settings import CommonProxySettings
from openapi_client.models.common_runtime_resource import CommonRuntimeResource
from openapi_client.models.common_secret import CommonSecret
from openapi_client.models.cred_credential import CredCredential
from openapi_client.models.cred_temporary_token import CredTemporaryToken
from openapi_client.models.cred_type import CredType
from openapi_client.models.cred_usage_type import CredUsageType
from openapi_client.models.customrules_action import CustomrulesAction
from openapi_client.models.customrules_effect import CustomrulesEffect
from openapi_client.models.customrules_ref import CustomrulesRef
from openapi_client.models.customrules_rule import CustomrulesRule
from openapi_client.models.customrules_type import CustomrulesType
from openapi_client.models.defender_category import DefenderCategory
from openapi_client.models.defender_defender import DefenderDefender
from openapi_client.models.defender_feature_status import DefenderFeatureStatus
from openapi_client.models.defender_features import DefenderFeatures
from openapi_client.models.defender_proxy_listener_type import DefenderProxyListenerType
from openapi_client.models.defender_scan_status import DefenderScanStatus
from openapi_client.models.defender_settings import DefenderSettings
from openapi_client.models.defender_status import DefenderStatus
from openapi_client.models.defender_system_info import DefenderSystemInfo
from openapi_client.models.defender_type import DefenderType
from openapi_client.models.defender_upgrade_status import DefenderUpgradeStatus
from openapi_client.models.deployment_command_error import DeploymentCommandError
from openapi_client.models.deployment_daemon_set import DeploymentDaemonSet
from openapi_client.models.forensic_container_event import ForensicContainerEvent
from openapi_client.models.forensic_container_event_type import ForensicContainerEventType
from openapi_client.models.forensic_host_event import ForensicHostEvent
from openapi_client.models.forensic_host_event_type import ForensicHostEventType
from openapi_client.models.identity_ldap_settings import IdentityLdapSettings
from openapi_client.models.identity_provider_name import IdentityProviderName
from openapi_client.models.identity_provider_settings import IdentityProviderSettings
from openapi_client.models.identity_redirect_url_response import IdentityRedirectURLResponse
from openapi_client.models.identity_saml_settings import IdentitySamlSettings
from openapi_client.models.identity_saml_type import IdentitySamlType
from openapi_client.models.identity_settings import IdentitySettings
from openapi_client.models.istio_authorization_policy import IstioAuthorizationPolicy
from openapi_client.models.istio_authorization_policy_destination import IstioAuthorizationPolicyDestination
from openapi_client.models.istio_authorization_policy_rule import IstioAuthorizationPolicyRule
from openapi_client.models.istio_authorization_policy_service import IstioAuthorizationPolicyService
from openapi_client.models.istio_authorization_policy_source import IstioAuthorizationPolicySource
from openapi_client.models.license_spdx_license import LicenseSPDXLicense
from openapi_client.models.log_log_entry import LogLogEntry
from openapi_client.models.mitre_technique import MitreTechnique
from openapi_client.models.prisma_ia_c_attributes import PrismaIaCAttributes
from openapi_client.models.prisma_ia_c_job_result import PrismaIaCJobResult
from openapi_client.models.prisma_ia_c_parameters import PrismaIaCParameters
from openapi_client.models.prisma_ia_c_policy_attributes import PrismaIaCPolicyAttributes
from openapi_client.models.prisma_ia_c_policy_violation import PrismaIaCPolicyViolation
from openapi_client.models.prisma_ia_c_scan_error_details import PrismaIaCScanErrorDetails
from openapi_client.models.prisma_ia_c_scan_failure_criteria import PrismaIaCScanFailureCriteria
from openapi_client.models.prisma_ia_c_scan_info import PrismaIaCScanInfo
from openapi_client.models.prisma_ia_c_scan_job_config import PrismaIaCScanJobConfig
from openapi_client.models.prisma_ia_c_scan_request import PrismaIaCScanRequest
from openapi_client.models.prisma_ia_c_scan_result import PrismaIaCScanResult
from openapi_client.models.prisma_ia_c_scan_results_metadata import PrismaIaCScanResultsMetadata
from openapi_client.models.rbac_perm_name import RbacPermName
from openapi_client.models.rbac_permission import RbacPermission
from openapi_client.models.rbac_role import RbacRole
from openapi_client.models.runtime_anti_malware_rule import RuntimeAntiMalwareRule
from openapi_client.models.runtime_app import RuntimeApp
from openapi_client.models.runtime_app_listening_ports import RuntimeAppListeningPorts
from openapi_client.models.runtime_container_capabilities import RuntimeContainerCapabilities
from openapi_client.models.runtime_container_network_rule import RuntimeContainerNetworkRule
from openapi_client.models.runtime_container_policy import RuntimeContainerPolicy
from openapi_client.models.runtime_container_policy_rule import RuntimeContainerPolicyRule
from openapi_client.models.runtime_dns_query import RuntimeDNSQuery
from openapi_client.models.runtime_dns_rule import RuntimeDNSRule
from openapi_client.models.runtime_deny_list_rule import RuntimeDenyListRule
from openapi_client.models.runtime_file_integrity_rule import RuntimeFileIntegrityRule
from openapi_client.models.runtime_filesystem_rule import RuntimeFilesystemRule
from openapi_client.models.runtime_geo_ip import RuntimeGeoIP
from openapi_client.models.runtime_host_dns_rule import RuntimeHostDNSRule
from openapi_client.models.runtime_host_network_rule import RuntimeHostNetworkRule
from openapi_client.models.runtime_host_policy import RuntimeHostPolicy
from openapi_client.models.runtime_host_policy_rule import RuntimeHostPolicyRule
from openapi_client.models.runtime_host_profile import RuntimeHostProfile
from openapi_client.models.runtime_host_profile_listening_port import RuntimeHostProfileListeningPort
from openapi_client.models.runtime_host_profile_outgoing_port import RuntimeHostProfileOutgoingPort
from openapi_client.models.runtime_log_inspection_rule import RuntimeLogInspectionRule
from openapi_client.models.runtime_processes_rule import RuntimeProcessesRule
from openapi_client.models.runtime_profile_filesystem import RuntimeProfileFilesystem
from openapi_client.models.runtime_profile_filesystem_path import RuntimeProfileFilesystemPath
from openapi_client.models.runtime_profile_network import RuntimeProfileNetwork
from openapi_client.models.runtime_profile_network_behavioral import RuntimeProfileNetworkBehavioral
from openapi_client.models.runtime_profile_network_geo_ip import RuntimeProfileNetworkGeoIP
from openapi_client.models.runtime_profile_network_static import RuntimeProfileNetworkStatic
from openapi_client.models.runtime_profile_process import RuntimeProfileProcess
from openapi_client.models.runtime_profile_processes import RuntimeProfileProcesses
from openapi_client.models.runtime_rule_effect import RuntimeRuleEffect
from openapi_client.models.runtime_ssh_event import RuntimeSSHEvent
from openapi_client.models.serverless_action_resources import ServerlessActionResources
from openapi_client.models.serverless_associated_version import ServerlessAssociatedVersion
from openapi_client.models.serverless_condition import ServerlessCondition
from openapi_client.models.serverless_function_info import ServerlessFunctionInfo
from openapi_client.models.serverless_layer_info import ServerlessLayerInfo
from openapi_client.models.serverless_permissions import ServerlessPermissions
from openapi_client.models.serverless_radar_data import ServerlessRadarData
from openapi_client.models.serverless_radar_entity import ServerlessRadarEntity
from openapi_client.models.serverless_resource import ServerlessResource
from openapi_client.models.serverless_service_api import ServerlessServiceAPI
from openapi_client.models.serverless_trigger import ServerlessTrigger
from openapi_client.models.serverless_triggers import ServerlessTriggers
from openapi_client.models.shared_activity_type import SharedActivityType
from openapi_client.models.shared_alert_threshold import SharedAlertThreshold
from openapi_client.models.shared_allowed_cve import SharedAllowedCVE
from openapi_client.models.shared_app_embedded_embed_request import SharedAppEmbeddedEmbedRequest
from openapi_client.models.shared_app_firewall_audit import SharedAppFirewallAudit
from openapi_client.models.shared_audit import SharedAudit
from openapi_client.models.shared_aws_region_type import SharedAwsRegionType
from openapi_client.models.shared_backup_spec import SharedBackupSpec
from openapi_client.models.shared_binary import SharedBinary
from openapi_client.models.shared_block_threshold import SharedBlockThreshold
from openapi_client.models.shared_cli_scan_result import SharedCLIScanResult
from openapi_client.models.shared_cve_allow_list import SharedCVEAllowList
from openapi_client.models.shared_cve_rule import SharedCVERule
from openapi_client.models.shared_cloud_compliance import SharedCloudCompliance
from openapi_client.models.shared_cloud_discovery_entity import SharedCloudDiscoveryEntity
from openapi_client.models.shared_cloud_discovery_result import SharedCloudDiscoveryResult
from openapi_client.models.shared_cloud_scan_policy import SharedCloudScanPolicy
from openapi_client.models.shared_cloud_scan_rule import SharedCloudScanRule
from openapi_client.models.shared_code_repo_provider_type import SharedCodeRepoProviderType
from openapi_client.models.shared_code_repo_settings import SharedCodeRepoSettings
from openapi_client.models.shared_code_repo_specification import SharedCodeRepoSpecification
from openapi_client.models.shared_conditions import SharedConditions
from openapi_client.models.shared_connection import SharedConnection
from openapi_client.models.shared_container_history_event import SharedContainerHistoryEvent
from openapi_client.models.shared_container_info import SharedContainerInfo
from openapi_client.models.shared_container_network import SharedContainerNetwork
from openapi_client.models.shared_container_network_firewall_profile_audits import SharedContainerNetworkFirewallProfileAudits
from openapi_client.models.shared_container_network_firewall_subtype_audits import SharedContainerNetworkFirewallSubtypeAudits
from openapi_client.models.shared_container_port import SharedContainerPort
from openapi_client.models.shared_container_process import SharedContainerProcess
from openapi_client.models.shared_container_radar_incoming_connection import SharedContainerRadarIncomingConnection
from openapi_client.models.shared_container_runtime_profile import SharedContainerRuntimeProfile
from openapi_client.models.shared_container_scan_result import SharedContainerScanResult
from openapi_client.models.shared_coordinates import SharedCoordinates
from openapi_client.models.shared_custom_compliance_check import SharedCustomComplianceCheck
from openapi_client.models.shared_custom_ip_feed import SharedCustomIPFeed
from openapi_client.models.shared_custom_labels_settings import SharedCustomLabelsSettings
from openapi_client.models.shared_custom_malware_feed import SharedCustomMalwareFeed
from openapi_client.models.shared_cve_type import SharedCveType
from openapi_client.models.shared_defender_install_bundle import SharedDefenderInstallBundle
from openapi_client.models.shared_defender_license_details import SharedDefenderLicenseDetails
from openapi_client.models.shared_docker_network_info import SharedDockerNetworkInfo
from openapi_client.models.shared_encode_serverless_rule_opts import SharedEncodeServerlessRuleOpts
from openapi_client.models.shared_encoded_serverless_rule import SharedEncodedServerlessRule
from openapi_client.models.shared_entity_type import SharedEntityType
from openapi_client.models.shared_file_details import SharedFileDetails
from openapi_client.models.shared_file_integrity_event import SharedFileIntegrityEvent
from openapi_client.models.shared_file_integrity_event_type import SharedFileIntegrityEventType
from openapi_client.models.shared_file_metadata import SharedFileMetadata
from openapi_client.models.shared_forensic_settings import SharedForensicSettings
from openapi_client.models.shared_host_activity import SharedHostActivity
from openapi_client.models.shared_host_auto_deploy_specification import SharedHostAutoDeploySpecification
from openapi_client.models.shared_host_info import SharedHostInfo
from openapi_client.models.shared_host_network_firewall_profile_audits import SharedHostNetworkFirewallProfileAudits
from openapi_client.models.shared_host_network_firewall_subtype_audits import SharedHostNetworkFirewallSubtypeAudits
from openapi_client.models.shared_host_radar_incoming_connection import SharedHostRadarIncomingConnection
from openapi_client.models.shared_image import SharedImage
from openapi_client.models.shared_image_history import SharedImageHistory
from openapi_client.models.shared_image_host import SharedImageHost
from openapi_client.models.shared_image_info import SharedImageInfo
from openapi_client.models.shared_image_instance import SharedImageInstance
from openapi_client.models.shared_image_scan_result import SharedImageScanResult
from openapi_client.models.shared_image_tag import SharedImageTag
from openapi_client.models.shared_incident import SharedIncident
from openapi_client.models.shared_incident_category import SharedIncidentCategory
from openapi_client.models.shared_incident_type import SharedIncidentType
from openapi_client.models.shared_installed_products import SharedInstalledProducts
from openapi_client.models.shared_internet_connections import SharedInternetConnections
from openapi_client.models.shared_j_frog_repo_type import SharedJFrogRepoType
from openapi_client.models.shared_key_values import SharedKeyValues
from openapi_client.models.shared_kube_cluster_role import SharedKubeClusterRole
from openapi_client.models.shared_kube_label import SharedKubeLabel
from openapi_client.models.shared_kube_policy_rule import SharedKubePolicyRule
from openapi_client.models.shared_kube_role import SharedKubeRole
from openapi_client.models.shared_kubernetes_audit import SharedKubernetesAudit
from openapi_client.models.shared_kubernetes_audit_policy import SharedKubernetesAuditPolicy
from openapi_client.models.shared_kubernetes_audit_settings import SharedKubernetesAuditSettings
from openapi_client.models.shared_kubernetes_deployment_type import SharedKubernetesDeploymentType
from openapi_client.models.shared_kubernetes_event_user_info import SharedKubernetesEventUserInfo
from openapi_client.models.shared_lambda_runtime_type import SharedLambdaRuntimeType
from openapi_client.models.shared_license import SharedLicense
from openapi_client.models.shared_license_config import SharedLicenseConfig
from openapi_client.models.shared_license_contract_type import SharedLicenseContractType
from openapi_client.models.shared_license_threshold import SharedLicenseThreshold
from openapi_client.models.shared_license_tier import SharedLicenseTier
from openapi_client.models.shared_log_inspection_event import SharedLogInspectionEvent
from openapi_client.models.shared_logger_setting import SharedLoggerSetting
from openapi_client.models.shared_logging_settings import SharedLoggingSettings
from openapi_client.models.shared_malware import SharedMalware
from openapi_client.models.shared_mgmt_audit import SharedMgmtAudit
from openapi_client.models.shared_mgmt_type import SharedMgmtType
from openapi_client.models.shared_network_info import SharedNetworkInfo
from openapi_client.models.shared_package import SharedPackage
from openapi_client.models.shared_packages import SharedPackages
from openapi_client.models.shared_policy import SharedPolicy
from openapi_client.models.shared_policy_rule import SharedPolicyRule
from openapi_client.models.shared_policy_type import SharedPolicyType
from openapi_client.models.shared_port import SharedPort
from openapi_client.models.shared_profile_kubernetes_data import SharedProfileKubernetesData
from openapi_client.models.shared_progress import SharedProgress
from openapi_client.models.shared_region_data import SharedRegionData
from openapi_client.models.shared_registry_os_type import SharedRegistryOSType
from openapi_client.models.shared_registry_scan_request import SharedRegistryScanRequest
from openapi_client.models.shared_registry_settings import SharedRegistrySettings
from openapi_client.models.shared_registry_specification import SharedRegistrySpecification
from openapi_client.models.shared_runtime_attack_type import SharedRuntimeAttackType
from openapi_client.models.shared_runtime_audit import SharedRuntimeAudit
from openapi_client.models.shared_runtime_profile_state import SharedRuntimeProfileState
from openapi_client.models.shared_runtime_severity import SharedRuntimeSeverity
from openapi_client.models.shared_runtime_type import SharedRuntimeType
from openapi_client.models.shared_scan_result_type import SharedScanResultType
from openapi_client.models.shared_scan_settings import SharedScanSettings
from openapi_client.models.shared_scan_type import SharedScanType
from openapi_client.models.shared_secret_store_type import SharedSecretStoreType
from openapi_client.models.shared_secrets_injection_type import SharedSecretsInjectionType
from openapi_client.models.shared_secrets_policy import SharedSecretsPolicy
from openapi_client.models.shared_secrets_rule import SharedSecretsRule
from openapi_client.models.shared_secrets_store import SharedSecretsStore
from openapi_client.models.shared_secrets_stores import SharedSecretsStores
from openapi_client.models.shared_serverless_auto_deploy_specification import SharedServerlessAutoDeploySpecification
from openapi_client.models.shared_serverless_bundle_request import SharedServerlessBundleRequest
from openapi_client.models.shared_serverless_scan_specification import SharedServerlessScanSpecification
from openapi_client.models.shared_subnet_connections import SharedSubnetConnections
from openapi_client.models.shared_syslog_settings import SharedSyslogSettings
from openapi_client.models.shared_tas_droplet_specification import SharedTASDropletSpecification
from openapi_client.models.shared_tag import SharedTag
from openapi_client.models.shared_tag_rule import SharedTagRule
from openapi_client.models.shared_tag_vuln_metadata import SharedTagVulnMetadata
from openapi_client.models.shared_trust_audit import SharedTrustAudit
from openapi_client.models.shared_trust_audits import SharedTrustAudits
from openapi_client.models.shared_trust_registry_repo_audits import SharedTrustRegistryRepoAudits
from openapi_client.models.shared_trusted_cert_settings import SharedTrustedCertSettings
from openapi_client.models.shared_trusted_cert_signature import SharedTrustedCertSignature
from openapi_client.models.shared_upload_scan_result import SharedUploadScanResult
from openapi_client.models.shared_user import SharedUser
from openapi_client.models.shared_vm_specification import SharedVMSpecification
from openapi_client.models.shared_vault_secret import SharedVaultSecret
from openapi_client.models.shared_wild_fire_policy import SharedWildFirePolicy
from openapi_client.models.shared_wild_fire_settings import SharedWildFireSettings
from openapi_client.models.trust_data import TrustData
from openapi_client.models.trust_group import TrustGroup
from openapi_client.models.trust_host_status import TrustHostStatus
from openapi_client.models.trust_image_result import TrustImageResult
from openapi_client.models.trust_policy import TrustPolicy
from openapi_client.models.trust_policy_rule import TrustPolicyRule
from openapi_client.models.trust_status import TrustStatus
from openapi_client.models.types_access_stats import TypesAccessStats
from openapi_client.models.types_access_stats_count import TypesAccessStatsCount
from openapi_client.models.types_alert_profile_option import TypesAlertProfileOption
from openapi_client.models.types_all_defenders_usage import TypesAllDefendersUsage
from openapi_client.models.types_app_firewall_attack_count import TypesAppFirewallAttackCount
from openapi_client.models.types_audit_timeslice import TypesAuditTimeslice
from openapi_client.models.types_authentication_response import TypesAuthenticationResponse
from openapi_client.models.types_available_vulnerabilities import TypesAvailableVulnerabilities
from openapi_client.models.types_base_image import TypesBaseImage
from openapi_client.models.types_base_images_rule import TypesBaseImagesRule
from openapi_client.models.types_cve_stats import TypesCVEStats
from openapi_client.models.types_cve_vulnerability import TypesCVEVulnerability
from openapi_client.models.types_cert_data import TypesCertData
from openapi_client.models.types_cert_settings import TypesCertSettings
from openapi_client.models.types_certificate_settings import TypesCertificateSettings
from openapi_client.models.types_cluster_radar_info import TypesClusterRadarInfo
from openapi_client.models.types_compliance_category_stats import TypesComplianceCategoryStats
from openapi_client.models.types_compliance_daily_stats import TypesComplianceDailyStats
from openapi_client.models.types_compliance_id_stats import TypesComplianceIDStats
from openapi_client.models.types_compliance_stats import TypesComplianceStats
from openapi_client.models.types_compliance_template_stats import TypesComplianceTemplateStats
from openapi_client.models.types_console_auth_response import TypesConsoleAuthResponse
from openapi_client.models.types_console_certificate_settings import TypesConsoleCertificateSettings
from openapi_client.models.types_container_radar_data import TypesContainerRadarData
from openapi_client.models.types_container_radar_entity import TypesContainerRadarEntity
from openapi_client.models.types_credential_usage import TypesCredentialUsage
from openapi_client.models.types_defender_summary import TypesDefenderSummary
from openapi_client.models.types_defender_usage import TypesDefenderUsage
from openapi_client.models.types_discovered_vm import TypesDiscoveredVM
from openapi_client.models.types_ecs_task_definition_options import TypesEcsTaskDefinitionOptions
from openapi_client.models.types_event_stats import TypesEventStats
from openapi_client.models.types_group import TypesGroup
from openapi_client.models.types_hpkp_settings import TypesHPKPSettings
from openapi_client.models.types_host_auto_deploy_spec_status import TypesHostAutoDeploySpecStatus
from openapi_client.models.types_host_auto_deploy_status import TypesHostAutoDeployStatus
from openapi_client.models.types_host_radar_data import TypesHostRadarData
from openapi_client.models.types_host_radar_entity import TypesHostRadarEntity
from openapi_client.models.types_image_scan_options import TypesImageScanOptions
from openapi_client.models.types_intelligence_settings import TypesIntelligenceSettings
from openapi_client.models.types_intelligence_status import TypesIntelligenceStatus
from openapi_client.models.types_latest_version import TypesLatestVersion
from openapi_client.models.types_license_stats import TypesLicenseStats
from openapi_client.models.types_log_upload_response import TypesLogUploadResponse
from openapi_client.models.types_logon_settings import TypesLogonSettings
from openapi_client.models.types_mgmt_audit_filters import TypesMgmtAuditFilters
from openapi_client.models.types_network_firewall_stats import TypesNetworkFirewallStats
from openapi_client.models.types_profile_state_update import TypesProfileStateUpdate
from openapi_client.models.types_project import TypesProject
from openapi_client.models.types_project_credentials import TypesProjectCredentials
from openapi_client.models.types_registry_webhook_request import TypesRegistryWebhookRequest
from openapi_client.models.types_resource_vulnerability_stats import TypesResourceVulnerabilityStats
from openapi_client.models.types_risk_score_factors import TypesRiskScoreFactors
from openapi_client.models.types_risk_tree_resource import TypesRiskTreeResource
from openapi_client.models.types_rule_compliance_stats import TypesRuleComplianceStats
from openapi_client.models.types_runtime_stats import TypesRuntimeStats
from openapi_client.models.types_secrets_status import TypesSecretsStatus
from openapi_client.models.types_security_advisor_configuration import TypesSecurityAdvisorConfiguration
from openapi_client.models.types_security_advisor_dashboard_resp import TypesSecurityAdvisorDashboardResp
from openapi_client.models.types_security_advisor_notes import TypesSecurityAdvisorNotes
from openapi_client.models.types_serverless_auto_deploy_spec_status import TypesServerlessAutoDeploySpecStatus
from openapi_client.models.types_serverless_auto_deploy_status import TypesServerlessAutoDeployStatus
from openapi_client.models.types_serverless_radar_status import TypesServerlessRadarStatus
from openapi_client.models.types_serverless_usage import TypesServerlessUsage
from openapi_client.models.types_settings import TypesSettings
from openapi_client.models.types_stats import TypesStats
from openapi_client.models.types_status import TypesStatus
from openapi_client.models.types_status_type import TypesStatusType
from openapi_client.models.types_telemetry_settings import TypesTelemetrySettings
from openapi_client.models.types_trends import TypesTrends
from openapi_client.models.types_user_collection import TypesUserCollection
from openapi_client.models.types_user_password import TypesUserPassword
from openapi_client.models.types_user_preferences import TypesUserPreferences
from openapi_client.models.types_user_project import TypesUserProject
from openapi_client.models.types_vuln_impacted_resources import TypesVulnImpactedResources
from openapi_client.models.types_vulnerabilities_stats import TypesVulnerabilitiesStats
from openapi_client.models.types_vulnerability_info import TypesVulnerabilityInfo
from openapi_client.models.types_vulnerability_stats import TypesVulnerabilityStats
from openapi_client.models.types_vulnerability_summary import TypesVulnerabilitySummary
from openapi_client.models.vuln_all_compliance import VulnAllCompliance
from openapi_client.models.vuln_application import VulnApplication
from openapi_client.models.vuln_compliance_template import VulnComplianceTemplate
from openapi_client.models.vuln_condition import VulnCondition
from openapi_client.models.vuln_custom_vulnerabilities import VulnCustomVulnerabilities
from openapi_client.models.vuln_custom_vulnerability import VulnCustomVulnerability
from openapi_client.models.vuln_distribution import VulnDistribution
from openapi_client.models.vuln_effect import VulnEffect
from openapi_client.models.vuln_expiration_date import VulnExpirationDate
from openapi_client.models.vuln_exploit_type import VulnExploitType
from openapi_client.models.vuln_package_type import VulnPackageType
from openapi_client.models.vuln_tag_info import VulnTagInfo
from openapi_client.models.vuln_type import VulnType
from openapi_client.models.vuln_vulnerability import VulnVulnerability
from openapi_client.models.waas_api_model_id import WaasAPIModelID
from openapi_client.models.waas_api_observation import WaasAPIObservation
from openapi_client.models.waas_api_path import WaasAPIPath
from openapi_client.models.waas_api_request import WaasAPIRequest
from openapi_client.models.waas_api_spec import WaasAPISpec
from openapi_client.models.waas_access_controls import WaasAccessControls
from openapi_client.models.waas_application_spec import WaasApplicationSpec
from openapi_client.models.waas_attack_type import WaasAttackType
from openapi_client.models.waas_body_config import WaasBodyConfig
from openapi_client.models.waas_bot_protection_spec import WaasBotProtectionSpec
from openapi_client.models.waas_custom_block_response_config import WaasCustomBlockResponseConfig
from openapi_client.models.waas_do_s_config import WaasDoSConfig
from openapi_client.models.waas_do_s_match_condition import WaasDoSMatchCondition
from openapi_client.models.waas_do_s_rates import WaasDoSRates
from openapi_client.models.waas_effect import WaasEffect
from openapi_client.models.waas_endpoint import WaasEndpoint
from openapi_client.models.waas_exception_field import WaasExceptionField
from openapi_client.models.waas_exception_location import WaasExceptionLocation
from openapi_client.models.waas_file_type import WaasFileType
from openapi_client.models.waas_header_spec import WaasHeaderSpec
from openapi_client.models.waas_intel_gathering_config import WaasIntelGatheringConfig
from openapi_client.models.waas_js_injection_spec import WaasJSInjectionSpec
from openapi_client.models.waas_known_bot_protections_spec import WaasKnownBotProtectionsSpec
from openapi_client.models.waas_malicious_upload_config import WaasMaliciousUploadConfig
from openapi_client.models.waas_method import WaasMethod
from openapi_client.models.waas_network_controls import WaasNetworkControls
from openapi_client.models.waas_network_list import WaasNetworkList
from openapi_client.models.waas_param import WaasParam
from openapi_client.models.waas_param_location import WaasParamLocation
from openapi_client.models.waas_param_style import WaasParamStyle
from openapi_client.models.waas_param_type import WaasParamType
from openapi_client.models.waas_path import WaasPath
from openapi_client.models.waas_policy import WaasPolicy
from openapi_client.models.waas_protection import WaasProtection
from openapi_client.models.waas_protection_config import WaasProtectionConfig
from openapi_client.models.waas_protection_status import WaasProtectionStatus
from openapi_client.models.waas_re_captcha_spec import WaasReCAPTCHASpec
from openapi_client.models.waas_re_captcha_type import WaasReCAPTCHAType
from openapi_client.models.waas_remote_host_forwarding_config import WaasRemoteHostForwardingConfig
from openapi_client.models.waas_request_anomalies import WaasRequestAnomalies
from openapi_client.models.waas_request_anomaly_threshold import WaasRequestAnomalyThreshold
from openapi_client.models.waas_rule import WaasRule
from openapi_client.models.waas_status_code_range import WaasStatusCodeRange
from openapi_client.models.waas_unknown_bot_protection_spec import WaasUnknownBotProtectionSpec
from openapi_client.models.waas_user_defined_bot import WaasUserDefinedBot
from openapi_client.models.wildfire_usage import WildfireUsage
