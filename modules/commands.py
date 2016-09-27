commands = ["quit", "list"]

def quit(worker, args=None):
    return 0

def help(worker, args=None):
    command = args[0]
    print("%s not in commands : %s" %(command, commands))

def list(worker, args=None):
    i = 0
    for thread in worker.threads:
        service = worker.get_service(i)
        print("[%i] | %s | %s" %(service.id, thread, service.name))
        i += 1

def kill(worker, args=None):
    worker.kill(int(args[1]))
