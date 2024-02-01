#!/usr/bin/env python3
"""this class to Unittests and integration tests"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """this class to test github org client"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock_val):
        """Test to GithubOrgClient.org returns correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()

        mock_val.called_with_once(test_class.ORG_URL.format(org=input))

    def test_public_repos_url(self):
        """func to test result of _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_val:
            payload = {"repos_url": "Hello World"}
            mock_val.return_value = payload

            test_class = GithubOrgClient('test')
            res = test_class._public_repos_url
            self.assertEqual(res, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """this func to test method unit-test GithubOrgClient"""
        payload = [{"name": "Google"}, {"name": "Twitter"}]

        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pulc:

            mock_pulc.return_value = "hello world"
            test_class = GithubOrgClient('test')
            res = test_class.public_repos()

            expec = [item["name"] for item in payload]
            self.assertEqual(res, expec)

            mock_pulc.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expect):
        """func to unit-test for GithubOrgClient.has_license """
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expect)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """this class to test Integration test of fixtures"""
    @classmethod
    def setUpClass(clss):
        """func method called before tests in an individual class"""
        config = {'return_value.json.side_effect':
                  [
                      clss.org_payload, clss.repos_payload,
                      clss.org_payload, clss.repos_payload
                  ]
                  }
        clss.get_patcher = patch('requests.get', **config)
        clss.mock = clss.get_patcher.start()

    def test_public_repos(self):
        """func to  Integration test: public repos"""
        test_cl = GithubOrgClient("google")

        self.assertEqual(test_cl.org, self.org_payload)
        self.assertEqual(test_cl.repos_payload, self.repos_payload)

        self.assertEqual(test_cl.public_repos(), self.expected_repos)
        self.assertEqual(test_cl.public_repos("XLICENSE"), [])

        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """func to Integration test for public repos with License """
        test_cl = GithubOrgClient("google")

        self.assertEqual(test_cl.public_repos(), self.expected_repos)
        self.assertEqual(test_cl.public_repos("XLICENSE"), [])

        self.assertEqual(test_cl.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(clss):
        """func method called after tests in an individual class"""
        clss.get_patcher.stop()
