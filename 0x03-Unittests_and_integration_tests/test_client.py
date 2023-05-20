#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock, MagicMock
from utils import access_nested_map as anm
from utils import get_json, memoize
from parameterized import parameterized
from client import GithubOrgClient as GOC


class TestGithubOrgClient(unittest.TestCase):
    """
    The test class for the function
    """
    @parameterized.expand([
        ("google", {"site": "google"}),
        ("abc", {"site": "abc"})
        ])
    @patch("client.get_json")
    def test_org(self, param, resp, mock_fun):
        """
        test the org function
        """
        mock_fun.return_value = MagicMock(return_value=resp)
        goc = GOC(param)
        self.assertEqual(goc.org(), resp)
        self.assertEqual(goc.org(), resp)
        mock_fun.assert_called_once()


if __name__ == "__main__":
    unittest.main()
