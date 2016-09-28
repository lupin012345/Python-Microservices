from importlib import import_module
from threading import Thread
import run

class Service():
    def __init__(self, service_name, service_conf):
        self.name = service_name
        self.directory = service_conf['directory']
        self.keepAlive = service_conf['restart']
        self.main_method = service_conf['main_method']
        self.thread = Thread(target=self.run, args=[])

    def setId(self, id):
        self.id = id
        
    def run(self):
        import_module("run.%s.%s" %(self.directory, self.name))
        command = "run.%s.%s.%s" %(self.directory, self.name, self.main_method)
        if self.keepAlive:
            while self.keepAlive:
                eval(command)()
        else:
            eval(command)()

    def start(self):
        self.thread.start()

    def restart(self, thread=None):
        if thread is not None:
            self.thread = thread
        else:
            self.thread = Thread(target=self.run, args=[])
        self.thread.start()

    def isAlive(self):
        return self.thread.isAlive()
