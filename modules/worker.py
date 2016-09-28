from threading import Thread

class Worker():
    def __init__(self):
        self.threads = []
        self.services = []
            
    def start(self):
        for service in self.services:
            t = Thread(target=service.run, args=[])
            self.threads.append(t)
            t.start()

    def add(self, service):
        self.services.append(service)
      
    def kill(self, id):
        self.threads[id].interrupt_main()
        self.services.pop(id)
        self.threads.pop(id)

    def get_service(self, id):
        for service in self.services:
            if service.id == id:
                return service
        return None
