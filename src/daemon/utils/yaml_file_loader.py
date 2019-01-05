# -*- coding: utf-8 -*-
import yaml
from src.daemon.classes import ServiceableService

DEFAULT_FILE_NAME = "services.yml"


# Read YAML file
def get_service_list_from_parsed_yaml(filename):
    if filename is None:
        filename = DEFAULT_FILE_NAME
    with open(filename, 'r') as stream:
        data_loaded = yaml.load(stream)
        return map_service_dict_to_service_list(data_loaded.get('service_health'))


def map_service_dict_to_service_list(service_dict):
    service_list = []
    for key, value in service_dict.items():
        service_list.append(extract_from_value_dictionary_and_map_to_class(key, value))
    return service_list


def extract_from_value_dictionary_and_map_to_class(key, value_dictionary):
    return ServiceableService.ServiceableService(key)\
        .set_log(value_dictionary.get('log'))\
        .set_expect(value_dictionary.get('expect'))\
        .set_available_at(value_dictionary.get('available_at'))\
        .set_check_me(value_dictionary.get('check_me'))