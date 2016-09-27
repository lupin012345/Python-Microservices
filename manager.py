#!/bin/python
import logging as log
from importlib import import_module
import services
import config
from modules.worker import Worker

LOG_FILENAME = 'python_manager.log'
dynamic_imports = []
worker = Worker()

class Service():
  def __init__(self, name):
    self.name = name

def __init__():
  global dynamic_imports
  log.basicConfig(filename=LOG_FILENAME,level=log.DEBUG)
  for service in config.run.keys():
    dynamic_imports.append(import_module('services.%s' %service))    

def	main():
  __init__()
  for service_name in config.run.keys():
    worker.add(Service(service_name))
  worker.start()
  log.info('All tasks done. Stopping')
  return 0

if __name__ == '__main__':
  main()
