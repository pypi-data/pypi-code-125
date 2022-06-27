# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_container
from pulpcore.client.pulp_container.models.paginatedcontainer_container_distribution_response_list import PaginatedcontainerContainerDistributionResponseList  # noqa: E501
from pulpcore.client.pulp_container.rest import ApiException

class TestPaginatedcontainerContainerDistributionResponseList(unittest.TestCase):
    """PaginatedcontainerContainerDistributionResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedcontainerContainerDistributionResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_container.models.paginatedcontainer_container_distribution_response_list.PaginatedcontainerContainerDistributionResponseList()  # noqa: E501
        if include_optional :
            return PaginatedcontainerContainerDistributionResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_container.models.container/container_distribution_response.container.ContainerDistributionResponse(
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        base_path = '0', 
                        repository = '0', 
                        name = '0', 
                        pulp_href = '0', 
                        content_guard = '0', 
                        pulp_labels = pulpcore.client.pulp_container.models.pulp_labels.pulp_labels(), 
                        repository_version = '0', 
                        registry_path = '0', 
                        namespace = '0', 
                        private = True, 
                        description = '0', )
                    ]
            )
        else :
            return PaginatedcontainerContainerDistributionResponseList(
        )

    def testPaginatedcontainerContainerDistributionResponseList(self):
        """Test PaginatedcontainerContainerDistributionResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
