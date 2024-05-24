# coding: utf-8

"""
    Host Activation Service

    Host activation service provides a RESTful interface to manage cert and join token object. Join tokens are essentially a password that allows on-prem hosts to auto-associate themselves to a customer's account and receive a signed cert.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from infra_provision.api.ui_join_token_api import UIJoinTokenApi


class TestUIJoinTokenApi(unittest.TestCase):
    """UIJoinTokenApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UIJoinTokenApi()

    def tearDown(self) -> None:
        pass

    def test_create(self) -> None:
        """Test case for create

        User can create a join token. Join token is random character string which is used for instant validation of new hosts.
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        User can revoke the join token. Once revoked, it can not be used further. The join token record is preserved forever.
        """
        pass

    def test_delete_set(self) -> None:
        """Test case for delete_set

        User can revoke a list of join tokens. Once revoked, join tokens can not be used further. The records are preserved forever.
        """
        pass

    def test_list(self) -> None:
        """Test case for list

        User can list the join tokens for an account.
        """
        pass

    def test_read(self) -> None:
        """Test case for read

        User can get the join token providing its resource id in the parameter.
        """
        pass

    def test_update(self) -> None:
        """Test case for update

        User can modify the tags or expiration time of a join token.
        """
        pass


if __name__ == '__main__':
    unittest.main()
