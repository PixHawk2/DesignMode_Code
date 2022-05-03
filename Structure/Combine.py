'''
组合模式：
抽象组件
叶子组件
复合组件
'''
from  abc import ABCMeta,abstractmethod

class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

class Point(Graphic):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return '坐标为:%s,%s'%(self.x,self.y)

    def draw(self):
        print(str(self))
class Line(Graphic):
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return '线的起点：%s 终点 %s'%(self.p1,self.p2)

    def draw(self):
        print(str(self))
class Picture(Graphic):
    def __init__(self,iterable):
        self.child = []
        for i in iterable:
            self.add(i)
    def add(self,grapgic):
        self.child.append(grapgic)
    def draw(self):
        print('*************')
        for g in self.child:
            g.draw()
        print('+++++++++++++')

p1 = Point(1,2)
p2 = Point(3,4)
line1 = Line(Point(5,6),Point(7,9))
pic1 = Picture([p1,p2,line1])
# p1.draw()
# line1.draw()
# pic1.draw()

pic2 = Picture([pic1,Point(10,30),Line(Point(50,3),Point(100,83))])
pic2.draw()