import logging as log

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
        service.process.terminate()
