import json

import allure
import pytest
from hamcrest import assert_that, equal_to, has_key, is_, is_not

from framework.contants import ApiConstants
from framework.utils import reverse_line, is_valid_uuid


class TestPost:
    @pytest.mark.parametrize(
        "palindrome",
        [
            True,
            False
        ]
    )
    def test_post_palindrome_request_(self, api_client, palindrome):
        response = api_client.post_palindrome_request(
            path=ApiConstants.URL_POST,
            palindrome=palindrome
        )

        with allure.step("Check status code"):
            assert_that(response.status_code, equal_to(ApiConstants.STATUS_CODE_200_OK), response.content)

        with allure.step("Check response body"):
            response_content = json.loads(response.content)

            assert_that(response_content, has_key('id'))
            response_id_value = response_content['id']
            assert_that(is_valid_uuid(response_id_value), is_(True), "Value of 'id' is not UUID")

            assert_that(response_content, has_key('result'))
            response_result_value = response_content['result']

            if palindrome:
                assert_that(response_result_value, equal_to(reverse_line(response_result_value)),
                            "Result str isn't palindrome")
            else:
                assert_that(response_result_value, is_(str),
                            f"Value of 'result' is not instance_of str. Real type: {type(response_result_value)}")

    @pytest.mark.parametrize(
        "palindrome",
        [
            123
        ]
    )
    def test_post_with_incorrect_palindrome_param(self, api_client, palindrome):
        response = api_client.post_palindrome_request(
            path=ApiConstants.URL_POST,
            palindrome=palindrome
        )

        with allure.step("Check status code"):
            assert_that(response.status_code, equal_to(ApiConstants.STATUS_CODE_422_UNPROCESSABLE_ENTITY),
                        response.content)

        with allure.step("Check response body"):
            response_content = json.loads(response.content)

            assert_that(response_content, is_not(has_key('id')))
            assert_that(response_content, is_not(has_key('result')))
