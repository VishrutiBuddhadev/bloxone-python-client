# coding: utf-8

"""
    DDI Keys API

    The DDI Keys application is a BloxOne DDI service for managing TSIG keys and GSS-TSIG (Kerberos) keys which are used by other BloxOne DDI applications. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from keys.api.generate_tsig_api import GenerateTsigApi


class TestGenerateTsigApi(unittest.TestCase):
    """GenerateTsigApi unit test stubs"""

    def setUp(self) -> None:
        self.api = GenerateTsigApi()

    def tearDown(self) -> None:
        pass

    def test_generate_tsig(self) -> None:
        """Test case for generate_tsig

        Generate TSIG key with a random secret.
        """
        pass


if __name__ == '__main__':
    unittest.main()
