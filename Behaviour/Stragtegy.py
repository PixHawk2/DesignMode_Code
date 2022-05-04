'''
策略模式
'''
from abc import ABCMeta,abstractmethod
# 角色：上下文、抽象策略，实际策略

class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class FastStrategy(Strategy):
    def execute(self,data):
        print('使用快速策略处理数据%s'%data)
class SlowStrategy(Strategy):
    def execute(self,data):
        print('使用慢速策略处理数据%s'%data)
class Context:
    def __init__(self,data,strategy):
        self.data = data
        self.strategy = strategy

    def switch_strategy(self,strategy):
        self.strategy = strategy

    def run(self):
        self.strategy.execute(self.data)

s1 = FastStrategy()
s2 = SlowStrategy()
data = 'hudi hhhh'
context1 = Context(data,s1)
context1.run()
context1.switch_strategy(s2)
context1.run()


