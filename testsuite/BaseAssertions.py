from http import HTTPStatus

import requests
from requests import Response
from json import JSONDecodeError


class BaseAssertions:
    @classmethod
    def check_HTTPcode(self, response_code, expected_code=HTTPStatus.OK):
            assert response_code == expected_code, f"Ожидаемый результат {expected_code} не соответсвует реальному {response_code}"

    @classmethod
    def check_value(self, actual_result, expected_value):
            assert actual_result == expected_value, f"Ожидаемый результат {expected_value} не соответствует реальному {actual_result}"

    @classmethod
    def check_JSONkey(self, response: Response = None, responseJSON: dict = None, expected_key=None):
            if response is not None:
                try:
                    response = response.json()
                except JSONDecodeError:
                    assert False, f"Ответ не json, тело ответа {response.text}"

                assert expected_key in response, f"Json не имеет ключ {expected_key}"
            else:
                try:
                    response = responseJSON
                except JSONDecodeError:
                    assert False, f"Ответ не json, тело ответа {response.text}"

                assert expected_key in responseJSON, f"Json не имеет ключ {expected_key}"
