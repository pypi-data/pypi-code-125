
"""Intercept boto to ensure that HTTPS is reported correctly.

"""

from __future__ import unicode_literals

from . import HTTPConnectionInterceptor


def intercept_boto(agent, mod):
    HTTPConnectionInterceptor.https_connection_classes.add(mod.CertValidatingHTTPSConnection)
