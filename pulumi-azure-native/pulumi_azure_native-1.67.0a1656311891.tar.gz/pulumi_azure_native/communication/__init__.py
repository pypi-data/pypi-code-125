# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .communication_service import *
from .domain import *
from .email_service import *
from .get_communication_service import *
from .get_domain import *
from .get_email_service import *
from .list_communication_service_keys import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.communication.v20200820 as __v20200820
    v20200820 = __v20200820
    import pulumi_azure_native.communication.v20200820preview as __v20200820preview
    v20200820preview = __v20200820preview
    import pulumi_azure_native.communication.v20211001preview as __v20211001preview
    v20211001preview = __v20211001preview
else:
    v20200820 = _utilities.lazy_import('pulumi_azure_native.communication.v20200820')
    v20200820preview = _utilities.lazy_import('pulumi_azure_native.communication.v20200820preview')
    v20211001preview = _utilities.lazy_import('pulumi_azure_native.communication.v20211001preview')

