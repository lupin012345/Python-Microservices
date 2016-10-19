from modules.utils import check_config, git_clone
from modules.service import Service
from importlib import reload
import logging as log
import config

class Worker():
    def __init__(self):
        self.services = []
        self.lastId = 0

    def getService(self, id):
        for service in self.services:
            if service.id == id:
                return service
        log.warning("There is no service with id %i" %id)
        return None

    def start(self):
        for service in self.services:
            log.info("Starting service %s" %service.name)
            service.start()

    def init(self, server):
        self.__init__()
        self.server = server
        check_config()
        for service_name in config.run.keys():
            service_conf = config.run[service_name]
            self.add(Service(service_name, service_conf, self.server))
        return

    def stop(self):
        for service in self.services:
            self.kill(service.id)
    
    def restart(self):
        self.stop()
        reload(config)
        self.init(self.server)
        self.start()
            
    def add(self, service):
        log.info("Added service %s" %service.name)
        self.lastId += 1
        service.setId(self.lastId)
        self.services.append(service)
      
    def kill(self, id):
        service = self.getService(id)
        if service is None:
            log.warning("There is no service with id %i" %id)
            return
        service.stop()
