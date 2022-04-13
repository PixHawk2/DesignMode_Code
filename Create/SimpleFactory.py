'''
简单工厂模式
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

class PaymentFactory:
    def createPayment(self,method):
        if method == 'alipay':
            return AliPay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return AliPay(huabei=True)
        else:
            raise TypeError('No Support Method')
consumer = PaymentFactory()
pay = consumer.createPayment('huabei')
pay.payment(100)