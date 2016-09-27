#!/bin/python
#local imports
import modules.commands as commands
from modules.worker import Worker
from modules.service import Service
#
import logging as log
from importlib import import_module
import services
import config


LOG_FILENAME = 'python_manager.log'
dynamic_imports = []
worker = Worker()

def __init__():
  i = 0
  global dynamic_imports
  log.basicConfig(filename=LOG_FILENAME,level=log.DEBUG)
  for service in config.run.keys():
    dynamic_imports.append(import_module('services.%s' %service))
  for service_name in config.run.keys():
    worker.add(Service(service_name, i))
    i += 1
    
def handle_input(command):
  command = command.strip()
  command = command.split(" ")
  if command[0] not in commands.commands:
    commands.help(worker, command)
  else:
    output = eval("commands.%s" %command[0])(worker, command)
    if output is not None:
      return False
  return True
    
def	main():
  __init__()
  worker.start()
  while handle_input(input()) is True:
    continue
  log.info('All tasks done. Stopping')
  return 0

if __name__ == '__main__':
  main()
