from src.daemon.utils.yaml_file_loader import get_service_list_from_parsed_yaml
from src.daemon.classes import ServiceableConfig as config, ServiceableConfig
from daemon.classes import ServiceManager as sm
import argparse

def service_able():
    parser = argparse.ArgumentParser("service-able")

    parser.add_argument("-f", "-file",
                        help="absolute location of a file containing service definitions")
    parser.add_argument("-m", "-mode",
                        choices=config.ServiceableConfig.serviceable_modes,
                        help="specify mode of operation",
                        default="daemon")

    config_holder = config.ServiceableConfig().set_active_mode(parser.parse_args().m)
    service_list = get_service_list_from_parsed_yaml(parser.parse_args().f)
    print "Starting service health checks..."
    sm.ServiceManager(service_list, config_holder).distribute_services_to_service_check_job_collator()

if __name__ == '__main__':
    print " ____  ____  ____  _  _  __  ___  ____       __   ____  __    ____"
    print "/ ___)(  __)(  _ \/ )( \(  )/ __)(  __)___  / _\ (  _ \(  )  (  __)"
    print "\___ \ ) _)  )   /\ \/ / )(( (__  ) _)(___)/    \ ) _ (/ (_/\ ) _)"
    print "(____/(____)(__\_) \__/ (__)\___)(____)    \_/\_/(____/\____/(____)"
    service_able()
