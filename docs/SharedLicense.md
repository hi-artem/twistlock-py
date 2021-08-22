# SharedLicense

License represent the customer license

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | AccessToken is the customer access token.  | [optional] 
**contract_id** | **str** | ContractID is the customer contract ID.  | [optional] 
**contract_type** | [**SharedLicenseContractType**](SharedLicenseContractType.md) |  | [optional] 
**credits** | **int** | Credits the total amount of credits purchased by the customer.  | [optional] 
**customer_id** | **str** | CustomerID is the customer ID.  | [optional] 
**defender_details** | [**list[SharedDefenderLicenseDetails]**](SharedDefenderLicenseDetails.md) | DefenderDetails represents the defenders license details.  | [optional] 
**defenders** | **int** | Deprecated: Defenders is the maximum number of defender allowed in this license. Use DefenderDetails field instead.  | [optional] 
**expiration_date** | **datetime** | ExpirationDate is the license expiration date.  | [optional] 
**issue_date** | **datetime** | IssueDate is the license issue date.  | [optional] 
**type** | [**SharedLicenseTier**](SharedLicenseTier.md) |  | [optional] 
**workloads** | **int** | Deprecated: Workloads is the number of workloads per license kept for backward compatibility. Use Credits instead.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


