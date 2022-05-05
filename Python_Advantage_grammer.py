
# __call__:使得实例能够像函数一样被调用
class Hudi:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print('__init__ was called')
    def __call__(self, *args, **kwargs):
        print('*********')
        self.x = args[0]
        self.y = args[1]
        print('__call__ {}and {}'.format(self.x,self.y))

    def __del__(self):
        del self.x
        del self.y

hudi = Hudi(20,32)
hudi(25,100)
print('hudi value is {}=={}'.format(hudi.x,hudi.y))
# 元类的使用
class MyListMeta(type):
    def __new__(cls, name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return super().__new__(cls,name,bases,attrs)
class Mylist(list,metaclass=MyListMeta):
    pass
list1 = Mylist()
list1.add(1)
list1.add(100)
print(list1)
# 如何限制只能通过工厂类调用
class ManPlayer:
    def play(self):
        print('男玩家在玩游戏')


class WomanPlayer:
    def play(self):
        print('女玩家在玩游戏')

class CatPlayer:
    def play(self):
        print('猫玩家在玩游戏')

class FactoryPlayer:
    players = {'Man':ManPlayer,'woman':WomanPlayer}
    def __new__(cls,kinds):
        if kinds in cls.players:
            return cls.players[kinds]()
        else:
            return CatPlayer()
# 如果不加限制，直接调用玩家类和工厂类均可实现
player = FactoryPlayer('Man')
player1 = ManPlayer()
player.play()
player1.play()



# 如何加限制？使用元类
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        if len(args) == 0 or args[0] != 'factory':
            raise  TypeError('不可以直接实例化类')

class ManPlayer1(metaclass=NoInstance):
    def play(self):
        print('男玩家在玩游戏')


class WomanPlayer1(metaclass=NoInstance):
    def play(self):
        print('女玩家在玩游戏')

class CatPlayer1(metaclass=NoInstance):
    def play(self):
        print('猫玩家在玩游戏')

class FactoryPlayer1:
    players = {'Man':ManPlayer1,'woman':WomanPlayer1}
    def __new__(cls,kinds):
        if kinds in cls.players:
            return cls.players[kinds]()
        else:
            return CatPlayer1()
# player = FactoryPlayer1('Man')
player2 = ManPlayer1('factory')#此处会raise TypeError
# player.play()
player2.play()