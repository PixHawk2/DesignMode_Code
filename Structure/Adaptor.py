'''
适配器模式
'''
'''
工厂方法：约束工厂，抽线工厂
'''
from abc import ABCMeta,abstractmethod

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def payment(self,money):
        pass

class AliPay(Payment):
    def __init__(self,huabei=False):
        self.huabei = huabei

    def payment(self,money):
        if self.huabei:
            print('使用花呗支付 %d 元' % money)
        else:
            print('使用支付宝支付 %d 元'%money)
class WechatPay(Payment):
    def payment(self,money):
        print('使用微信支付 %d 元' % money)
class Bankpayment:
    def cost(self,money):
        print('使用银联支付 %d 元' % money)

class Applepayment:
    def cost(self,money):
        print('使用苹果支付 %d 元' % money)
#类适配器
class Bankpaymentpay(Payment,Bankpayment):
    def payment(self,money):
        self.cost(money)
# 对象适配器
class Adaptor(Payment):
    def __init__(self,pay):
        self.pay = pay
    def payment(self,money):
        self.pay.cost(money)


pay = Adaptor(Applepayment())
pay.payment(100)
