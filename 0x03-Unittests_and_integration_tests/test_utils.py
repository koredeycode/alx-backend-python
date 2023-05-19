#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map
"""
import unittest
from utils import access_nested_map as anm
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


if __name__ == "__main__":
    unittest.main()
