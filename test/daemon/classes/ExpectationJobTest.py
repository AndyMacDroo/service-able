import unittest
from src.daemon.classes import ExpectationJob as ej


class ExpectationJobTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_ExpectationJob_with_healthy_http_job_makes_request_and_returns_true(self):
        job = ej.ExpectationJob('job', { 'a_http_response': {'code' : 200}}, { 'url' : 'https://www.google.com'})
        self.assertTrue(job.run_and_return_results())

    def test_ExpectationJob_with_unhealthy_http_job_makes_request_and_returns_false(self):
        job = ej.ExpectationJob('job', { 'a_http_response': {'code' : 200}}, { 'url' : 'https://www.google.blah'})
        self.assertFalse(job.run_and_return_results())

    def test_ExpectationJob_with_unhealthy_http_job_with_expect_json_makes_request_and_returns_false(self):
        job = ej.ExpectationJob('job', { 'a_http_response': {'code' : 200, 'json': "{ \"STATUS\" :  \"UP\"}"}}, { 'url' : 'https://www.google.com'})
        self.assertFalse(job.run_and_return_results())

    def test_ExpectationJob_with_healthy_http_job_with_expect_json_makes_request_and_returns_true(self):
        job = ej.ExpectationJob('job', { 'a_http_response': {'code' : 200, 'json': "{ \"userId\": 1, \"id\" : 1, \"title\": \"delectus aut autem\", \"completed\": false }"}}, { 'url' : 'https://jsonplaceholder.typicode.com/todos/1'})
        self.assertTrue(job.run_and_return_results())

    def test_ExpectationJob_with_healthy_http_job_with_expect_contains_makes_request_and_returns_true(self):
        job = ej.ExpectationJob('job', { 'a_http_response': {'code' : 200, 'contains': "google"}}, { 'url' : 'https://www.google.com'})
        self.assertTrue(job.run_and_return_results())

    def test_ExpectationJob_with_unhealthy_http_job_with_expect_contains_makes_request_and_returns_false(self):
        job = ej.ExpectationJob('job', { 'a_http_response': {'code' : 200, 'contains': "potato-y"}}, { 'url' : 'https://www.microsoft.com'})
        self.assertFalse(job.run_and_return_results())

if __name__ == '__main__':
    unittest.main()