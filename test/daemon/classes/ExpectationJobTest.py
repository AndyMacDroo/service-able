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


if __name__ == '__main__':
    unittest.main()