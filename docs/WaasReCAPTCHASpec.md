# WaasReCAPTCHASpec

ReCAPTCHASpec is the reCAPTCHA spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_sessions** | **bool** | Indicates if the reCAPTCHA page is served at the start of every new session (true) or not (false).  | [optional] 
**enabled** | **bool** | Indicates if reCAPTCHA integration is enabled (true) or not (false).  | [optional] 
**secret_key** | [**CommonSecret**](CommonSecret.md) |  | [optional] 
**site_key** | **str** | ReCAPTCHA site key to use when invoking the reCAPTCHA service.  | [optional] 
**success_expiration_hours** | **int** | Duration for which the indication of reCAPTCHA success is kept. Maximum value is 30 days * 24 &#x3D; 720 hours.  | [optional] 
**type** | [**WaasReCAPTCHAType**](WaasReCAPTCHAType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


