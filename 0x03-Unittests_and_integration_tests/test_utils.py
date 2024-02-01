#!/usr/bin/env python3
"""this docs contains test for accessing nested_map function"""
import requests
import unittest
from utils import access_nested_map, memoize, get_json
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Any, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """this class to test access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expect: int) -> None:
        """
        Test to access_nested_map method.
        Args:
            nested_map: dictionary that may have nested dictionaries
            path: the Keys to get to the required value
        """
        resp = access_nested_map(nested_map, path)

        self.assertEqual(resp, expect)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test to access_nested_map method raises error when expected
        args:
            nested_map: dictionary that may have nested dictionaries
            path: the Keys to get to the required value
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """this class to test get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test the get_json method to ensure it returns the expected output.
        Args:
            url: url to send http request to
            payload: expected json response
        """
        mock_get.return_value.json.return_value = test_payload
        res = get_json(test_url)

        self.assertEqual(res, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """this class to test memoization decorator, memoize"""
    def test_memoize(self):
        """func to test utils.memoize decorator works"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_obj:
            testobj = TestClass()

            testobj.a_property()
            testobj.a_property()

            mock_obj.assert_called_once()
