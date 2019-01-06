import schedule
import ExpectationJob as ej
import datetime

from src.daemon.classes.logging import ServiceLogger as sl


class ServiceCheckJobCollator:

    service = None
    expectation_job = None

    def __init__(self, service, mode):
        self.mode = mode
        self.service = service
        self.expectation_job = ej.ExpectationJob(
            self.service.service_name,
            self.service.expect, self.service.available_at)

    def execute_job(self):
        self.service.set_is_healthy(self.expectation_job.run_and_return_results())
        self.log_service_status()
        if self.mode is not "daemon":
            return self.service.is_healthy

    def log_service_status(self):
        sl.ServiceLogger().log_at_info("{} - [service-able/{}] - the service is {}."
                                        .format(str(datetime.datetime.now()),
                      self.service.service_name,
                      "HEALTHY" if self.service.is_healthy else "UNHEALTHY - expected:" + str(self.service.expect)))

    def configure_schedule_for_job(self):
        if self.service.check_me is None:
            return schedule.every(1).seconds

        at_schedule = self.service.check_me.get('at')
        every_schedule = self.service.check_me.get('every')

        if at_schedule is not None:
            return self.configure_at_interval(at_schedule)
        elif every_schedule is not None:
            return self.configure_every_interval(every_schedule)
        return schedule.every(1).seconds

    @staticmethod
    def configure_at_interval(at_schedule):
        if at_schedule.get('time') is None:
            return schedule.every().day.at("00:00")
        return schedule.every().day.at(at_schedule.get('time'))

    @staticmethod
    def configure_every_interval(every_schedule):
        if every_schedule.get('seconds') is not None:
            return schedule.every(every_schedule.get('seconds')).seconds
        elif every_schedule.get('minutes') is not None:
            return schedule.every(every_schedule.get('minutes')).minutes
        elif every_schedule.get('hour') is not None:
            return schedule.every(every_schedule.get('hour')).hours

    def initialise_service_checks_schedule(self):
        self.configure_schedule_for_job().do(self.execute_job)
