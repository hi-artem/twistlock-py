# RuntimeDNSRule

DNSRule is the DNS runtime rule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blacklist** | **list[str]** | List of deny-listed domain names (e.g., www.bad-url.com, *.bad-url.com).  | [optional] 
**effect** | [**RuntimeRuleEffect**](RuntimeRuleEffect.md) |  | [optional] 
**whitelist** | **list[str]** | List of allow-listed domain names (e.g., *.gmail.com, *.s3.*.amazon.com).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


