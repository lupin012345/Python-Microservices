from modules.commands import handle_input
import socket
import select

class Server():
    def __init__(self, config, worker):
        self.config = config
        self.is_running = True
        self.port = config['port']
        self.host = config['host']
        self.inputs = []
        self.outputs = []
        self.BUFFER_SIZE = 1024
        self.worker = worker
        self.hello = "### Python Manager\nHello !\n#> "
        self.socket = None
        
    def start(self):
        print("Server starting")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.inputs.append(self.socket)
        while self.is_running:
            _in, _out, exception = select.select(self.inputs,
                                                 self.outputs,
                                                 [])
            for sock in _in:
                if sock == self.socket:
                    client, address = sock.accept()
                    print(address)
                    self.inputs.append(client)
                    client.send(self.hello.encode())
                else:
                    data = sock.recv(self.BUFFER_SIZE)
                    if data:
                        command = data.decode("UTF-8")
                        success, output = handle_input(command, self.worker, self)
                        sock.send(output.encode()+b"\n#> ")
                    else:
                        if sock in self.outputs:
                            self.outputs.remove(sock)
                        if sock in self.inputs:
                            self.inputs.remove(sock)
                    if sock not in self.outputs:
                        self.outputs.append(sock)
                    
    def stop(self):    
        print("Exiting...")
        if self.socket is not None:
            try:
                self.socket.shutdown(socket.SHUT_RDWR)
            except OSError as e:
                pass
            self.socket.close()

    def restart(self):
        print("Restarting...")
        if self.socket is not None:
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        self.__init__(self.config, self.worker)
        self.stop()
