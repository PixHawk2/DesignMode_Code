'''
观察者模式
'''
from abc import ABCMeta,abstractmethod
#抽象订阅者
class Subscription(metaclass=ABCMeta):
    @abstractmethod
    def update(self,publish):
        pass

#发布者
class Publisher:
    def __init__(self):
        self.subscriptor = []
    #订阅
    def attach(self,pub):
        self.subscriptor.append(pub)
    #取消订阅
    def deattach(self,pub):
        self.subscriptor.remove(pub)

    #推送
    def notice(self):
        for obj in self.subscriptor:
            obj.update(self)


#具体的信息发布
class StaffPublish(Publisher):
    def __init__(self,company_info):
        super().__init__()
        self.__company_info = company_info
    @property
    def company_info(self):
        return self.__company_info
    @company_info.setter
    def company_info(self,info):
        self.__company_info = info
        self.notice()
'''
obj1 = StaffPublish('abc')
print(obj1.company_info)
obj1.company_info = 'hudi'
print(obj1.company_info)
'''
#具体的订阅者
class Staff(Subscription):
    def __init__(self):
        self.info = None
        self.info_list = []

    def update(self,publish):
        self.info = (publish.company_info)
        self.info_list.append(self.info)

notice = StaffPublish('init information')
client1 = Staff()
client2 = Staff()
print(client1.info)
notice.attach(client2)
notice.attach(client1)
# print(client1.info)
notice.company_info = '好好学习，天天向上'
print(client1.info)
print(client1.info_list)
print(client2.info)
notice.deattach(client2)
print('***************')
notice.company_info = 'This is Second Notice'
print(client1.info)
print(client1.info_list)
print(client2.info)