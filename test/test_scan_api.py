# coding: utf-8

"""
    qg_api

    qualys guard rest api  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.scan_api import ScanApi  # noqa: E501
from openapi_client.rest import ApiException


class TestScanApi(unittest.TestCase):
    """ScanApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.scan_api.ScanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_scan(self):
        """Test case for create_scan

        Create scan  # noqa: E501
        """
        pass

    def test_get_scan(self):
        """Test case for get_scan

        Get user by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()