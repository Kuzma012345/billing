import logging
from http import HTTPStatus

import pytest
import requests

from testsuite.BaseAssertions import BaseAssertions
from testsuite.conftest import _customer_data


@pytest.fixture(scope="function")
def customer_data():
    def fixture(**kwargs):
        return _customer_data(**kwargs)
    return fixture


class TestCustomer(BaseAssertions):
    def setup(self):
        self.url = "http://0.0.0.0:9000/customer"

    def test_customer(self, customer_data):
        data = customer_data()
        pytest.exist_customer = data['name']
        response = requests.post(url=self.url, data=data)
        pytest.secret = data['secret']
        pytest.id = response.json()['customer']['customer_id']
        BaseAssertions.check_HTTPcode(response_code=response.status_code)
        BaseAssertions.check_value(actual_result=response.json()['customer']['customer_name'],
                                   expected_value=data['name'])
        BaseAssertions.check_JSONkey(responseJSON=response.json()['customer'],
                                     expected_key="customer_id")

    def test_customer_exists(self, customer_data):
        data = customer_data(name=pytest.exist_customer)
        response = requests.post(url=self.url, data=data)
        BaseAssertions.check_HTTPcode(response_code=response.status_code,
                                      expected_code=HTTPStatus.BAD_REQUEST)
        BaseAssertions.check_value(response.json()['status'],
                                   expected_value="error")
        BaseAssertions.check_value(response.json()['message'],
                                   expected_value=f"Customer with name {data['name']}, already exists")
