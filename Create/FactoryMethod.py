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

class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def createPayment(self):
        pass
class AlipayFactory(PaymentFactory):
    def createPayment(self):
        return AliPay()
class WechatFactory(PaymentFactory):
    def createPayment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory):
    # @staticmethod
    def createPayment(self):
        return AliPay(huabei=True)
good = HuabeiFactory()
hudi = good.createPayment()
hudi.payment(100)