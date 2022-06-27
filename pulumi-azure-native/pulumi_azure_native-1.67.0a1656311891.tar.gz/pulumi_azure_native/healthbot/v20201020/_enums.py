# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'SkuName',
    'SkuTier',
]


class SkuName(str, Enum):
    """
    The name of the HealthBot SKU
    """
    F0 = "F0"
    S1 = "S1"


class SkuTier(str, Enum):
    """
    This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
    """
    FREE = "Free"
    STANDARD = "Standard"
