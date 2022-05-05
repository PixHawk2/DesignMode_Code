'''
单例模式
保证一个类只能有一个实例，并提供一个访问它的全局节点
优点：对唯一实例的受控访问，相当于全局变量，但是防止了命名空间被污染
'''
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    def __init__(self,a):
        self.a = a
a = MyClass(10)
b = MyClass(20)

print(a.a)
print(b.a)
print(id(a))
print(id(b))

#单例模式：懒汉
class SingleTon:
    __instance = None
    def __init__(self):
        if not SingleTon.__instance:
            print('__init__ method was called')
        else:
            print('Instance has already been created',self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = SingleTon()
        return cls.__instance
print('*************')
s =  SingleTon()
print('++++++++++++++')
print('Object created',SingleTon.getInstance())
s1 = SingleTon()


'''
单态模式Monostate
'''
class Brog:
    __shared_state = {'1':'hudi'}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state
        pass
b = Brog()
b1 = Brog()
b.x = 45
b1.x = 85
b.y = 3
key = 'hh'
b.key = 'what'
print('b',b)
print('b1',b1)
print(b.__dict__)
print(b1.__dict__)

# 如何用元类实现单例模式
class MetaSingleTon(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleTon, cls).__call__(*args, **kwargs)
        return cls._instance[cls]