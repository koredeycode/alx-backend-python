#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map as anm
from utils import get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    The test class for the function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, mapping, params, res):
        """
        test access nested map function
        """
        self.assertEqual(anm(mapping, params), res)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(self, mapping, params, exception):
        """
        test the access nested map function for exception
        """
        with self.assertRaises(exception):
            anm(mapping, params)


class TestGetJson(unittest.TestCase):
    """
    The test class for the function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, payload):
        """
        test the get_json function
        """
        attrs = {'json.return_value': payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(url), payload)
            req_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
