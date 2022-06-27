# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ServerVersion',
    'SkuTier',
]


class ServerVersion(str, Enum):
    """
    PostgreSQL Server version.
    """
    SERVER_VERSION_13 = "13"
    SERVER_VERSION_12 = "12"
    SERVER_VERSION_11 = "11"


class SkuTier(str, Enum):
    """
    The tier of the particular SKU, e.g. Burstable.
    """
    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"
