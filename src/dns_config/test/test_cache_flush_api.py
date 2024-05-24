# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.api.cache_flush_api import CacheFlushApi


class TestCacheFlushApi(unittest.TestCase):
    """CacheFlushApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CacheFlushApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the Cache Flush object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
