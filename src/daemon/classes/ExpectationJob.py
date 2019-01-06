import requests
from requests import ConnectionError
import json

from src.daemon.classes.logging import ServiceLogger as sl

DEFAULT_REQUEST_TIMEOUT = 10

class ExpectationJob:
    service_name = None
    expect = None
    available_at = None

    def __init__(self, name, expect, available_at):
        self.service_name = name
        self.expect = expect
        self.available_at = available_at
        self.service_logger = sl.ServiceLogger()

    def run_and_return_results(self):
        if self.expect.get('a_http_response') is not None:
            try:
                r = self.do_http_request(self.available_at)
            except ConnectionError:
                return False
            return self.http_response_is_good(r)

        return False

    def http_response_is_good(self, response):
        if self.expect.get('a_http_response').get('code') is None:
            status_code_is_good = response.status_code == 200
        else:
            status_code_is_good = response.status_code == self.expect.get('a_http_response').get('code')
        if self.expect.get('a_http_response').get('json') is not None:
            response_content_is_good = self.compare_json_response_with_expected(response.content, self.expect.get('a_http_response').get('json'))
        else:
            response_content_is_good = True
        return status_code_is_good and response_content_is_good

    def do_http_request(self, available_at):
        basic_auth_configuration = available_at.get('basic_auth')
        if basic_auth_configuration is not None:
            r = requests.get(self.available_at.get('url'),
                                auth=(basic_auth_configuration.get('username'),
                                      basic_auth_configuration.get('password')),
                                timeout=DEFAULT_REQUEST_TIMEOUT)
        else:
            r = requests.get(self.available_at.get('url'), timeout=DEFAULT_REQUEST_TIMEOUT)
        self.service_logger.log_at_debug(r)
        return r

    def compare_json_response_with_expected(self, response, expected):
        self.service_logger.log_at_debug("Actual: {} - Expected: {} ".format(str(response), str(expected)))
        try:
            comparison = sorted(json.loads(response)) == sorted(json.loads(expected))
        except ValueError:
            return False
        return comparison
