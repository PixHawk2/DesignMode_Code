'''
建造者模式
需要精细调整流程的时候
'''
from abc import ABCMeta,abstractmethod
class Player:
    def __init__(self,arm=None,face=None,leg=None,body=None):
        self.arm = arm
        self.face = face
        self.leg = leg
        self.body = body

    def __str__(self):
        return '%s %s %s %s'%(self.face,self.arm,self.body,self.leg)

class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_arm(self):
        pass

    @abstractmethod
    def make_leg(self):
        pass

    @abstractmethod
    def make_face(self):
        pass

    @abstractmethod
    def make_body(self):
        pass
class GirlBuilder(Builder):
    def __init__(self):
        self.player = Player()
    def make_arm(self):
        self.player.arm = 'little'
    def make_leg(self):
        self.player.leg = '大长腿'
    def make_body(self):
        self.player.body = '好身材'
    def make_face(self):
        self.player.face = '俊俏脸'
class MonsterBuilder(Builder):
    def __init__(self):
        self.player = Player()
    def make_arm(self):
        self.player.arm = 'big'
    def make_leg(self):
        self.player.leg = '节肢动物'
    def make_body(self):
        self.player.body = '大象'
    def make_face(self):
        self.player.face = '猴子'

# Director是用来控制流程的，所以传入的一定是builder
class BuilderDirector:
    def build_player(self,builder):
        builder.make_face()
        builder.make_body()
        builder.make_arm()
        builder.make_leg()
        return builder.player

#client
builder = MonsterBuilder()
director = BuilderDirector()
character = director.build_player(builder)
print(character)