'''
责任链
'''
from abc import ABCMeta,abstractmethod
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handler_event(self):
        pass
class CEO(Handler):
    def handler_event(self,day):
        if day <=10:
            print('CEO 批准假期%s天'%day)
        else:
            print('No!!!')

class DepartmentLeader(Handler):
    def __init__(self):
        self.next = CEO()
    def handler_event(self,day):
        if day <=5:
            print('DepartmentLeader 批准假期%s天'%day)
        else:
            print('DepartmentLeader no Peimission!')
            self.next.handler_event(day)

class TeamHeader(Handler):
    def __init__(self):
        self.next = DepartmentLeader()
    def handler_event(self,day):
        if day <=3:
            print('TeamHeader 批准假期%s天'%day)
        else:
            print('TeamHeader no Peimission!')
            self.next.handler_event(day)
vacation = TeamHeader()
vacation.handler_event(12)