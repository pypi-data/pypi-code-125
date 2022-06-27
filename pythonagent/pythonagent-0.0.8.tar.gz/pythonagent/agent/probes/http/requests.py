
"""Intercept requests to ensure that HTTPS is reported correctly.

"""

from __future__ import unicode_literals

from .urllib3 import intercept_urllib3


def intercept_requests(agent, mod):
    #print("intercept_requests")
    # requests ships with its own version of urllib3, so we need to manually intercept it.
    intercept_urllib3(agent, mod.packages.urllib3)
