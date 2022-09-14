
from testsuite.generator import random_string


def _customer_data(**kwargs):
    data = {
        "name": kwargs.pop('name', random_string()),
        "company": kwargs.pop('company', random_string()),
        "secret": kwargs.pop('secret', random_string())
    }
    return data
