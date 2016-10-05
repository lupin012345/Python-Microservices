#!/bin/python
#local imports
from modules.worker import Worker
from modules.service import Service
from modules.utils import *
from modules.server import Server
from modules.commands import quit
#externam imports
from importlib import import_module
from sys import stdout
import logging as log
import config

LOG_FILENAME = 'python_manager.log'
worker = Worker()
server = None

def __init__():
  global server
  #  log.basicConfig(filename=LOG_FILENAME,level=log.DEBUG)
  log.basicConfig(level=log.DEBUG)
  check_config()
  for service_name in config.run.keys():
    service_conf = config.run[service_name]
    worker.add(Service(service_name, service_conf))
  server = Server(config.daemon, worker)
    
def	main():
  __init__()
  worker.start()
  server.start()
  log.info('All tasks done. Stopping')
  return 0

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt as e:
    quit(worker, [], server)
