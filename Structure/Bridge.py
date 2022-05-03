'''
桥模式实现：
把一个食物的两个维度分离，使其可以独立变化
'''
from abc import ABCMeta,abstractmethod
class Shape:
    def __init__(self,color):
        self.color = color
    @abstractmethod
    def draw(self):
        pass

class Color:
    @abstractmethod
    def paint(self):
        pass
class Circle(Shape):
    _name = '圆形'
    def draw(self):
        self.color.paint(self)
class Square(Shape):
    _name = '方形'
    def draw(self):
        self.color.paint(self)
class Line(Shape):
    _name = '直线'
    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self,shape):
        print('红色的%s'%shape._name)

class Blue(Color):
    def paint(self,shape):
        print('蓝色的%s'%shape._name)

class Black(Color):
    def paint(self,shape):
        print('黑色的%s'%shape._name)

pic1 = Circle(Blue())
pic1.draw()

pic2 = Line(Red())
pic2.draw()