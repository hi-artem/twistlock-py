# SharedTrustedCertSignature

TrustedCertSignature represents a trusted cert settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cn** | **str** | CN is the certificate common name.  | [optional] 
**issuer** | **str** | Issuer is the certificate issuer.  | [optional] 
**not_after1** | **datetime** | NotAfter is the certificate expiration time Remark: the 1 suffix required for backward compatibility (previous values were strings and cannot be serialized).  | [optional] 
**not_before1** | **datetime** | NotBefore is the minimum time for which the cert is valid Remark: the 1 suffix required for backward compatibility (previous values were strings and cannot be serialized).  | [optional] 
**raw** | **str** | Raw is the raw certificate (in PEM format).  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


