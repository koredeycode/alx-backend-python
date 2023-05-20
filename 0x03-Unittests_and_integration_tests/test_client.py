#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
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

    def test_public_repos_url(self):
        """
        test the _public_repos_url function
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_fun:
            mock_fun.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos"}
            self.assertEqual(GOC("google")._public_repos_url,
                             "https://api.github.com/users/google/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        test the public_repos function
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_fun:
            mock_fun.return_value = test_payload["repos_url"]
            self.assertEqual(GOC("google").public_repos(),
                             ["episodes.dart", "kratu"],)
            mock_fun.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, dic, st, ret):
        """
        test the has_licence function
        """
        self.assertEqual(GOC.has_license(dic, st), ret)


if __name__ == "__main__":
    unittest.main()
