from molnframework.core.service.base import ServiceBase

class AddService(ServiceBase):
    x = 0
    y = 0
    
    parameters = ['x','y']
    address = 'add'

    def execute(self):
        return self.x + self.y

class MultService(ServiceBase):
    x = 0
    y = 0 

    parameters = ['x','y']
    address = "mult"

    def execute(self):
        return self.x * self.y