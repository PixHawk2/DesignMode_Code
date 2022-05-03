'''
代理模式

'''

from abc import ABCMeta,abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def set_content(self):
        pass
    def get_content(self):
        pass

class RealSubject(Subject):
    def __init__(self,filename):
        self.filename = filename
        with open(self.filename,encoding='utf-8') as f:
            print('prepare to read')
            self.content = f.read()
    def get_content(self):
        print(self.content)
        return self.content
    def set_content(self,content):
        with open(self.filename,'a',encoding='utf-8') as file:
            print('prepare to wirte')
            file.write(content)
# 虚代理
class VirtualProxy(Subject):
    def __init__(self,filename):
        self.filename = filename
        self.subject = None

    def get_content(self):
        if not self.subject:
            self.subject = RealSubject(self.filename)
        return self.subject.get_content()
    def set_content(self,contents):
        if not self.subject:
            self.subject = RealSubject(self.filename)
        return self.subject.set_content(contents)
# 保护代理
class ProtectProxy(Subject):
    def __init__(self,filename):
        self.sub = RealSubject(filename)
    def get_content(self):
        return self.sub.get_content()

    def set_content(self):
        raise PermissionError('no peimission')
sub1 = VirtualProxy('test.txt')
sub1.get_content()
sub1.set_content('python designmode')


sub_protect = ProtectProxy('test.txt')
sub_protect.get_content()
# sub_protect.set_content()
