# coding: utf-8

"""
    qg_api

    qualys guard rest api  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from api.report_api import ReportApi  # noqa: E501
from swagger_client.rest import ApiException


class TestReportApi(unittest.TestCase):
    """ReportApi unit test stubs"""

    def setUp(self):
        self.api = api.report_api.ReportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_report(self):
        """Test case for create_report

        Create report  # noqa: E501
        """
        pass

    def test_get_report(self):
        """Test case for get_report

        Get report by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()