'''
抽象工厂例子
定义一个工厂类接口，然后多个子工厂实现不同的差异
一个工厂生产一套产品
优点：
客户端与类的具体实现相分离
每个工厂创建了一个完整的产品系列，易于交换产品系列
产品的一致性
缺点：
难以支持新品类的产品

'''

from abc import ABCMeta,abstractmethod
#
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_shell(self):
        pass
class PhoneOS(metaclass=ABCMeta):
    @abstractmethod
    def show_OS(self):
        pass
class PhoneCpu(metaclass=ABCMeta):
    @abstractmethod
    def show_Cpu(self):
        pass
#
class littlePhoneShell(PhoneShell):
    def show_shell(self):
        print('Little Phone Shell')

class middlePhoneShell(PhoneShell):
    def show_shell(self):
        print('Middle Phone Shell')
class ApplePhoneShell(PhoneShell):
    def show_shell(self):
        print('Apple Phone Shell')
#
class Android(PhoneOS):
    def show_OS(self):
        print('Android')
class IOS(PhoneOS):
    def show_OS(self):
        print('IOS')
#
class SnapDragon(PhoneCpu):
    def show_Cpu(self):
        print('骁龙')
class AppleCpu(PhoneCpu):
    def show_Cpu(self):
        print('Apple Cpu')
class littleCpu(PhoneCpu):
    def show_Cpu(self):
        print('Normal Cpu')

# 抽象工厂
class PhoneMakeFac(metaclass=ABCMeta):
    @abstractmethod
    def make_phone_shell(self):
        pass

    @abstractmethod
    def make_phone_cpu(self):
        pass

    @abstractmethod
    def make_phone_OS(self):
        pass
class OppoMake(PhoneMakeFac):
    def make_phone_OS(self):
        return Android()
    def make_phone_cpu(self):
        return  SnapDragon()
    def make_phone_shell(self):
        return middlePhoneShell()
class AppleMake(PhoneMakeFac):
    def make_phone_shell(self):
        return ApplePhoneShell()
    def make_phone_OS(self):
        return IOS()
    def make_phone_cpu(self):
        return AppleCpu()

# 具体的组装和流程
def makephone(factory):
    cpu = factory.make_phone_cpu()
    shell = factory.make_phone_shell()
    os = factory.make_phone_OS()
    return Phone(os,shell,cpu)
# appliction-实际的逻辑
class Phone:
    def __init__(self,os,shell,cpu):
        self.os = os
        self.cpu = cpu
        self.shell = shell
    def show_info(self):
        print('phone info:')
        self.cpu.show_Cpu()
        self.shell.show_shell()
        self.os.show_OS()


phone1 = makephone(AppleMake())
phone1.show_info()


phone2 = makephone(OppoMake())
phone2.show_info()