import ServiceCheckJobCollator as scd
import schedule

from src.daemon.classes.logging import ServiceLogger as sl


class ServiceManager:

    services = None
    config = None

    def __init__(self, services, config):
        self.services = services
        self.config = config

    def distribute_services_to_service_check_job_collator(self):
        unhealthy_services = []
        for service in self.services:
            if service.expect is not None:
                if self.config.active_mode is not "daemon":
                    is_healthy = scd.ServiceCheckJobCollator(service, self.config.active_mode).execute_job()
                    if not is_healthy:
                        unhealthy_services.append(service)
                else:
                    scd.ServiceCheckJobCollator(service, self.config.active_mode).initialise_service_checks_schedule()
        if self.config.active_mode is "daemon":
            while True:
                schedule.run_pending()
        else:
            sl.ServiceLogger().log_at_info(unhealthy_services)
