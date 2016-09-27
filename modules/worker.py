from threading import Thread
import services

class Worker():
    def __init__(self):
        self.threads = []
        self.services = []
        
    def run_service(self, service):
        eval("services.%s.main()" %service.name)
            
    def start(self):
        for service in self.services:
            t = Thread(target=self.run_service, args=[service])
            self.threads.append(t)
            t.start()

    def add(self, service):
        self.services.append(service)

      
