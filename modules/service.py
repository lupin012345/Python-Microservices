from importlib import import_module
from multiprocessing import Process
import run

class Service():
    def __init__(self, service_name, service_conf):
        self.name = service_name
        self.directory = service_conf['directory']
        self.keepAlive = service_conf['restart']
        self.main_method = service_conf['main_method']
        self.process = Process(target=self.run, args=[])

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
        self.process.start()

    def stop(self):
        self.process.terminate()

    def restart(self, process=None):
        if process is not None:
            self.process = process
        else:
            self.process = Process(target=self.run, args=[])
        self.process.start()

    def isAlive(self):
        return self.process.is_alive()
