import sys
sys.path.append("..")
import unittest
from src.daemon.utils.yaml_file_loader import *
from src.daemon.classes import ServiceableService as sm


class YamlFileLoaderTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_map_service_dict_to_service_list_with_service_dict_returns_service_list(self):
        service_dict = { 'myService': { 'log': {}, 'expect': {}, 'available_at': {}, 'check_me': {}} }
        expected = sm.ServiceableService('myService').set_available_at({}).set_check_me({}).set_expect({}).set_log({})
        actual = map_service_dict_to_service_list(service_dict)[0]
        self.assertEqual(expected, actual)

    def test_map_service_dict_to_service_list_with_empty_service_dict_returns_emptyservice_list(self):
        service_dict = {}
        expected = []
        actual = map_service_dict_to_service_list(service_dict)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()