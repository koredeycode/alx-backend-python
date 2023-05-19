#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map as anm
from utils import get_json, memoize
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


class TestMemoize(unittest.TestCase):
    """
    The test class for the function
    """
    def test_memoize(self):
        """
        test the memoize function
        """
        class TestClass:
            def a_method(self):
                return 43

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method",
                          return_value=lambda: 43) as apatch:
            test = TestClass()
            self.assertEqual(test.a_property(), 43)
            self.assertEqual(test.a_property(), 43)
            apatch.assert_called_once()


if __name__ == "__main__":
    unittest.main()
