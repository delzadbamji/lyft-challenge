import pytest
import unittest
import requests


# import json

class Test(unittest.TestCase):
    @classmethod
    def test_route(self):
        url = "http://127.0.0.1:5000"
        test_string = "iamyourlyftdriver"
        param_data = {"string_to_cut": test_string}

        request = requests.post(url + "/test", params=param_data)
        assert request.status_code == 200


if __name__ == '__main__':
    Test()

