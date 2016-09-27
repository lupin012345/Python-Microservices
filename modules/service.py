import services

class Service():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def run(self):
        self.start()
        
    def start(self):
        eval("services.%s.main()" %self.name)
                
