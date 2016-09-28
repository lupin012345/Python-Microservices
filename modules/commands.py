commands = ["quit", "list", "start"]

def quit(worker, args=None):
    return 0

def help(worker, args=None):
    command = args[0]
    print("%s not in commands : %s" %(command, commands))

def list(worker, args=None):
    for service in worker.services:
        print("[%i] | %s | Alive : %s" %(service.id, service.name, service.isAlive()))

def start(worker, args=None):
    if len(args) > 1:
        id = int(args[1])
        service = worker.getService(id)
        if not service.isAlive():
            service.restart()
        else:
            log.warning("Service %i is already running" %id)
        
def kill(worker, args=None):
    worker.kill(int(args[1]))
