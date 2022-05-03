'''
外观模式：外观类和子系统类
'''
import time


class CPU:
    def run(self):
        print('CPU start run')
    def stop(self):
        print('CPU stop run')

class DISK:
    def run(self):
        print('DISK start run')
    def stop(self):
        print('DISK stop run')

class Memory:
    def run(self):
        print('Memory start run')
    def stop(self):
        print('Memory stop run')
class PC:
    def __init__(self):
        self.cpu = CPU()
        self.disk = DISK()
        self.memory = Memory()
    def run(self):
        print('PC is going to run......')
        self.cpu.run()
        self.disk.run()
        self.memory.run()
        print('PC is running!!!!!!!')
    def stop(self):
        print('*************PC is going to stop************')
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()
        print('**************PC power off*******************')
pc1 = PC()
pc1.run()
time.sleep(1)
pc1.stop()