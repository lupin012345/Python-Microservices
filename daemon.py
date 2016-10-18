#!/bin/python

#local imports
from modules.worker import Worker
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
  server = Server(config.daemon, worker)
  worker.init(server)
    
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
