import config
import logging as log
from sys import exit
from git import Repo
    
def check_config():
    mandatory_in_services = ["restart", "directory", "main_method"]
    mandatory_in_daemon = ["host", "port"]
    try:
        for mandatory in mandatory_in_daemon:
            if mandatory not in config.daemon.keys():
                log.error("Your daemon configuration must containes the attributes %s. %s is missing" %(mandatory_in_daemon, mandatory))
        for service_name in config.run.keys():
            service_conf = config.run[service_name]
            for mandatory in mandatory_in_services:
                if mandatory not in service_conf.keys():
                    log.error("Your service configuration must contain the attributes %s. %s is missing %s" %(mandatory_in_services, service_name, mandatory))
                    exit(-1)
        
    except AttributeError as e:
        log.error("Your config.py hasn't a correct format : [%s]" %str(e))
        exit(-1)

def git_clone(url, name):
    Repo.clone_from(url, config.daemon['services_directory'] + "/" + name)
