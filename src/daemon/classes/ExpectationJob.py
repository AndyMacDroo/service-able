import requests
from requests import ConnectionError


class ExpectationJob:
    service_name = None
    expect = None
    available_at = None

    def __init__(self, name, expect, available_at):
        self.service_name = name
        self.expect = expect
        self.available_at = available_at

    def run_and_return_results(self):
        if self.expect.get('a_http_response') is not None:
            try:
                r = self.do_http_request(self.available_at)
            except ConnectionError:
                return False
            return self.http_status_ok_or_as_defined(r.status_code)

        return False

    def http_status_ok_or_as_defined(self, request_status_code):
        if self.expect.get('a_http_response').get('code') is None:
            return request_status_code == 200
        return request_status_code == self.expect.get('a_http_response').get('code')

    def do_http_request(self, available_at):
        basic_auth_configuration = available_at.get('basic_auth')
        if basic_auth_configuration is not None:
            return requests.get(self.available_at.get('url'),
                                auth=(basic_auth_configuration.get('username'),
                                      basic_auth_configuration.get('password')),
                                timeout=10)
        return requests.get(self.available_at.get('url'), timeout=10)
