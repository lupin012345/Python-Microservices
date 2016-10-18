from importlib import import_module
from multiprocessing import Process
from os import getcwd, chdir
from modules.utils import git_clone
from sys import path
from time import sleep
import run
import sys
import os
import logging as log
import config

class Service():
    def __init__(self, service_name, service_conf, server):
        self.name = service_name
        self.directory = service_conf['directory']
        self.services_directory = config.daemon['services_directory']
        self.keepAlive = service_conf['restart']
        self.main_method = service_conf['main_method']
        self.repository = None
        if "repository" in service_conf.keys():
            self.repository = service_conf['repository']
        self.process = Process(target=self.run, args=[])
        self.server = server
    
    def setId(self, id):
        self.id = id
        
    def run(self):
        try:
            path.insert(0, getcwd()+"/%s/"%self.services_directory+self.directory)
            import_module("%s.%s.%s" %(self.services_directory, self.directory, self.name))
        except ImportError as e:
            log.warn("Module %s not found" %self.name)
            if self.repository is not None:
                git_clone(self.repository, self.directory)
                log.info("Successfully cloned %s. Restarting..." %self.repository)
                self.server.restart()
                sleep(2)
                os.execv(sys.executable, ['python'] + sys.argv)
                import_module("%s.%s.%s" %(self.services_directory, self.directory, self.name))
            else:
                log.err("The module %s is not found cannot be cloned from a repository")
        command = "%s.%s.%s.%s" %(self.services_directory, self.directory, self.name, self.main_method)
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
