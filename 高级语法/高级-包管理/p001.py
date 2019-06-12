# 包含一个学生类
# 一个sayhello函数
# 一个打印语句

class Student():
    def __init__(self, name="Noname", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayhello():
    print("Hi")

print("我是模块p001")