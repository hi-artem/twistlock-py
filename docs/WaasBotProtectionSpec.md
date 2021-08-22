# WaasBotProtectionSpec

BotProtectionSpec is the bot protections spec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interstitial_page** | **bool** | Indicates if an interstitial page is served (true) or not (false).  | [optional] 
**js_injection_spec** | [**WaasJSInjectionSpec**](WaasJSInjectionSpec.md) |  | [optional] 
**known_bot_protections_spec** | [**WaasKnownBotProtectionsSpec**](WaasKnownBotProtectionsSpec.md) |  | [optional] 
**re_captcha_spec** | [**WaasReCAPTCHASpec**](WaasReCAPTCHASpec.md) |  | [optional] 
**session_validation** | [**WaasEffect**](WaasEffect.md) |  | [optional] 
**unknown_bot_protection_spec** | [**WaasUnknownBotProtectionSpec**](WaasUnknownBotProtectionSpec.md) |  | [optional] 
**user_defined_bots** | [**list[WaasUserDefinedBot]**](WaasUserDefinedBot.md) | Effects to perform when user-defined bots are detected.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


