# coding: utf-8

"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class SharedScanResultType(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _AWS_ECR_AWS_LAMBDA_AWS_EC2_AWS_EKS_AWS_ECS_AWS_S3_AWS_CONFIG_AWS_CLOUD_TRAIL_AWS_KMS_AWS_CLOUD_WATCH_AWS_SNS_AWS_SECURITY_HUB_AWS_SECRETS_MANAGER_AWS_PARAMETER_STORE_AZURE_ACR_AZURE_FUNCTIONS_AZURE_AKS_AZURE_ACI_AZURE_VM_GCP_GCR_GCP_GCF_GCP_GKE_GCP_VM_ = "[\"aws-ecr\",\"aws-lambda\",\"aws-ec2\",\"aws-eks\",\"aws-ecs\",\"aws-s3\",\"aws-config\",\"aws-cloud-trail\",\"aws-kms\",\"aws-cloud-watch\",\"aws-sns\",\"aws-security-hub\",\"aws-secrets-manager\",\"aws-parameter-store\",\"azure-acr\",\"azure-functions\",\"azure-aks\",\"azure-aci\",\"azure-vm\",\"gcp-gcr\",\"gcp-gcf\",\"gcp-gke\",\"gcp-vm\"]"

    allowable_values = [_AWS_ECR_AWS_LAMBDA_AWS_EC2_AWS_EKS_AWS_ECS_AWS_S3_AWS_CONFIG_AWS_CLOUD_TRAIL_AWS_KMS_AWS_CLOUD_WATCH_AWS_SNS_AWS_SECURITY_HUB_AWS_SECRETS_MANAGER_AWS_PARAMETER_STORE_AZURE_ACR_AZURE_FUNCTIONS_AZURE_AKS_AZURE_ACI_AZURE_VM_GCP_GCR_GCP_GCF_GCP_GKE_GCP_VM_]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """SharedScanResultType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SharedScanResultType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SharedScanResultType):
            return True

        return self.to_dict() != other.to_dict()
