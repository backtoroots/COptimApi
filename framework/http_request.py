import requests


class HttpRequest:
    """Wrapper for requests library"""

    @staticmethod
    def http_post(url, params=None, data=None, json=None, headers=None):
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    @staticmethod
    def http_get(url: str, params: dict):
        return requests.get(
            url=url,
            params=params,
            allow_redirects=False
        )
