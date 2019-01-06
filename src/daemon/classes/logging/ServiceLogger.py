import logging

logging.basicConfig(filename='serviceable.log', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

class ServiceLogger:

    def __init__(self):
        pass

    def log_at_info(self, message):
        print "Invoked"
        logging.info(str(message))

    def log_at_debug(self, message):
        logging.debug(str(message))
