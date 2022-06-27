# coding: utf-8

"""
    printnanny-api-client

    Official API client library forprintnanny.ai print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@printnanny.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.patched_janus_edge_stream_request import PatchedJanusEdgeStreamRequest  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestPatchedJanusEdgeStreamRequest(unittest.TestCase):
    """PatchedJanusEdgeStreamRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedJanusEdgeStreamRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.patched_janus_edge_stream_request.PatchedJanusEdgeStreamRequest()  # noqa: E501
        if include_optional :
            return PatchedJanusEdgeStreamRequest(
                auth = printnanny_api_client.models.janus_auth_request.JanusAuthRequest(
                    admin_secret = '0', 
                    api_token = '0', 
                    config_type = 'cloud', 
                    user = 56, ), 
                api_domain = '0', 
                api_port = 56, 
                admin_port = 56, 
                ws_port = 56, 
                rtp_domain = '0', 
                active = True, 
                secret = '0', 
                pin = '0', 
                info = {
                    'key' : null
                    }, 
                rtp_port = 0, 
                device = 56
            )
        else :
            return PatchedJanusEdgeStreamRequest(
        )

    def testPatchedJanusEdgeStreamRequest(self):
        """Test PatchedJanusEdgeStreamRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
