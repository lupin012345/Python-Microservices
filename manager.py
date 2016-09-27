#!/bin/python
import logging as log

LOG_FILENAME = 'python_manager.log'

def __init__():
  log.basicConfig(filename=LOG_FILENAME,level=log.DEBUG)

def	main():
  __init__()
  log.warning("lol")
  return 0

if __name__ == '__main__':
  main()
