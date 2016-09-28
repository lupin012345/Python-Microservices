from importlib import import_module
import run

class Service():
    def __init__(self, name, directory, id):
        self.name = name
        self.directory = directory
        self.id = id

    def run(self):
        self.start()
        
    def start(self):
        import_module("run.%s.%s" %(self.directory, self.name))
        command = "run.%s.%s.main()" %(self.directory, self.name)
        eval(command)
                
