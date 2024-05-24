# coding: utf-8

"""
    DNS Configuration API

    The DNS application is a BloxOne DDI service that provides cloud-based DNS configuration with on-prem host serving DNS protocol. It is part of the full-featured BloxOne DDI solution that enables customers the ability to deploy large numbers of protocol servers in the delivery of DNS and DHCP throughout their enterprise network.   

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from dns_config.api.forward_zone_api import ForwardZoneApi


class TestForwardZoneApi(unittest.TestCase):
    """ForwardZoneApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ForwardZoneApi()

    def tearDown(self) -> None:
        pass

    def test_copy(self) -> None:
        """Test case for copy

        Copies the __ForwardZone__ object.
        """
        pass

    def test_create(self) -> None:
        """Test case for create

        Create the ForwardZone object.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Move the Forward Zone object to Recyclebin.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        List Forward Zone objects.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        Read the Forward Zone object.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        Update the Forward Zone object.
        """
        pass


if __name__ == '__main__':
    unittest.main()
