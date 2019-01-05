import ServiceCheckJobCollator as scd
import schedule


class ServiceManager:

    services = None

    def __init__(self, services):
        self.services = services
        self.distribute_services_to_service_check_job_collator()

    def distribute_services_to_service_check_job_collator(self):
        for service in self.services:
            if service.expect is not None:
                scd.ServiceCheckJobCollator(service).initialise_service_checks()
        while True:
            schedule.run_pending()

