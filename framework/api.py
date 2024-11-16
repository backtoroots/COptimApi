from uuid import UUID

from framework.http_request import HttpRequest


class Api:
    """Wrapper for executing HTTP request to certain API"""

    _GET_PARAM_ID = 'id'

    _POST_BODY_PALINDROME = 'palindrome'

    def __init__(self, base_address):
        self.base_address = base_address

    def get_result_request(self, path: str, request_id: UUID):
        """
            Execute get request
        Args:
            path: Additional path to endpoint
            request_id: UUID

        Returns:
            Response of get request
        """
        url = self.base_address + path
        params = {Api._GET_PARAM_ID: request_id}
        response = HttpRequest.http_get(url, params)
        return response

    def post_palindrome_request(self, path: str, palindrome: bool):
        """
            Execute post request
        Args:
            path: Additional path to endpoint
            palindrome: Boolean if response should contain palindrome string

        Returns:
            Response of post request
        """
        url = self.base_address + path
        json_dict = {Api._POST_BODY_PALINDROME: palindrome}
        response = HttpRequest.http_post(url, json=json_dict)
        return response
