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