import json
import uuid

import allure
import pytest
from hamcrest import assert_that, has_key, is_not, is_

from framework.contants import ApiConstants


class TestGet:

    def test_get_result_with_random_uuid(self, api_client):
        response = api_client.get_result_request(
            path=ApiConstants.URL_GET,
            request_id=uuid.uuid4()
        )

        with allure.step("Check status code"):
            assert_that(response.status_code, is_(ApiConstants.STATUS_CODE_200_OK), response.content)

        with allure.step("Check response body"):
            response_content = json.loads(response.content)
            assert_that(response_content, has_key('result'))

    @pytest.mark.parametrize(
        "request_id,status_code",
        [
            ("sdfsdf", ApiConstants.STATUS_CODE_422_UNPROCESSABLE_ENTITY),
            (123, ApiConstants.STATUS_CODE_422_UNPROCESSABLE_ENTITY)
        ]
    )
    def test_get_result_with_incorrect_uuid(self, api_client, request_id, status_code):
        response = api_client.get_result_request(
            path=ApiConstants.URL_GET,
            request_id=request_id
        )

        with allure.step("Check status code"):
            assert_that(response.status_code, is_(status_code), response.content)

        with allure.step("Check response body"):
            loaded_result = json.loads(response.content)
            assert_that(loaded_result, is_not(has_key('result')))
