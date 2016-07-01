from molnframework.core.service.base import ServiceBase

class AddService(ServiceBase):
    x = 0
    y = 0
    
    parameters = ['x','y']
    address = 'add'

    def execute(self):
        return x + y