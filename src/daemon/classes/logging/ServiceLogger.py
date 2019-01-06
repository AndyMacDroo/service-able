import logging


class ServiceLogger:

    def __init__(self):
        logging.basicConfig(filename='serviceable.log', level=logging.DEBUG)
        logging.getLogger().addHandler(logging.StreamHandler())
        pass

    def log_at_info(self, service_status):
        logging.info(service_status)

    def log_at_debug(self, request_result):
        logging.debug(request_result)
