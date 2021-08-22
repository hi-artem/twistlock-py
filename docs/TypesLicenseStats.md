# TypesLicenseStats

LicenseStats holds the console license stats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** | Avg is the average number of credits.  | [optional] 
**container_defenders** | **int** | ContainerDefenders is the total number of container defenders.  | [optional] 
**exceeded** | **bool** | Exceeded indicates the number of credits exceeded license.  | [optional] 
**host_defenders** | **int** | HostDefenders is the total number of host defenders.  | [optional] 
**monthly_usage** | [**list[TypesAllDefendersUsage]**](TypesAllDefendersUsage.md) | MonthlyUsage holds the last 24 monthly usage averages.  | [optional] 
**msg** | **str** | Msg is the license exceeded error/warning message to show.  | [optional] 
**on_demand_credits** | **int** | OnDemandCredits is the number of on demand credits used during the current contract.  | [optional] 
**total_credit_usage** | **int** | TotalCreditUsage is the total amount of credits used from the beginning of the current contract.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


