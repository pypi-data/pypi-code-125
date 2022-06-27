# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .availability_group_listener import *
from .get_availability_group_listener import *
from .get_sql_virtual_machine import *
from .get_sql_virtual_machine_group import *
from .sql_virtual_machine import *
from .sql_virtual_machine_group import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.sqlvirtualmachine.v20170301preview as __v20170301preview
    v20170301preview = __v20170301preview
    import pulumi_azure_native.sqlvirtualmachine.v20211101preview as __v20211101preview
    v20211101preview = __v20211101preview
    import pulumi_azure_native.sqlvirtualmachine.v20220201 as __v20220201
    v20220201 = __v20220201
    import pulumi_azure_native.sqlvirtualmachine.v20220201preview as __v20220201preview
    v20220201preview = __v20220201preview
else:
    v20170301preview = _utilities.lazy_import('pulumi_azure_native.sqlvirtualmachine.v20170301preview')
    v20211101preview = _utilities.lazy_import('pulumi_azure_native.sqlvirtualmachine.v20211101preview')
    v20220201 = _utilities.lazy_import('pulumi_azure_native.sqlvirtualmachine.v20220201')
    v20220201preview = _utilities.lazy_import('pulumi_azure_native.sqlvirtualmachine.v20220201preview')

