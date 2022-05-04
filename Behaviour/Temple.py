'''
模板策略
'''
import time
from abc import ABCMeta,abstractmethod

class Window(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
    @abstractmethod
    def repaint(self):
        pass

    def run(self):#模板方法
        self.start()
        while True:
            try:
                self.repaint()
                time.sleep(2)
            except KeyboardInterrupt:
                break
        self.stop()

class ClientWin(Window):
    def __init__(self,info):
        self.info = info
    def start(self):
        print('start running...')
    def stop(self):
        print('stop!!!!')
    def repaint(self):
        print('repeat paint {data}'.format(data=self.info))

ClientWin('huditest').run()


