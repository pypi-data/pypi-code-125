#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2018
#

__version__ = '0.0.44'

from .ftp import FTPStorage
from .oss import OSSStorage
from .obs import OBSStorage
from .s3 import S3Storage
from .azure import AzureStorage
from .ceph import CEPHStorage
from .jms import JMSReplayStorage, JMSCommandStorage
from .es import ESStorage
from .multi import MultiObjectStorage


def get_object_storage(config):
    if config.get("TYPE") in ["s3", "ceph", "swift", "cos"]:
        return S3Storage(config)
    elif config.get("TYPE") == "oss":
        return OSSStorage(config)
    elif config.get("TYPE") == "server":
        return JMSReplayStorage(config)
    elif config.get("TYPE") == "azure":
        return AzureStorage(config)
    elif config.get("TYPE") == "ceph":
        return CEPHStorage(config)
    elif config.get("TYPE") == "ftp":
        return FTPStorage(config)
    elif config.get("TYPE") == "obs":
        return OBSStorage(config)
    else:
        return JMSReplayStorage(config)


def get_log_storage(config):
    if config.get("TYPE") in ("es", "elasticsearch"):
        return ESStorage(config)
    elif config.get("TYPE") == "server":
        return JMSCommandStorage(config)
    else:
        return JMSCommandStorage(config)


def get_multi_object_storage(configs):
    return MultiObjectStorage(configs)
