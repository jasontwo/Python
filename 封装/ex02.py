#coding=utf-8
"""
@version: ??
@author: Muyi
@Mail: 768322192@qq.com
@file: ex02.py
@time: 2021/2/25 9:52
"""
"""
    使用方法封装
"""
class Wife01:
    def __init__(self,name='',age=0):
        # self.__name = name
        self.ser_name(name)
        #私有成员：障眼法（解释器会改变双下划綫开头的变量名）
        #self.__age = age
        self.set_age(age)
    def get_name(self):
        return self.__name
    def ser_name(self,value):
        self.__name=value
    def get_age(self):
        return self.__age
    def set_age(self,value):
        self.__age=value


w03 = Wife01()
w03.set_age(30)
print(w03.get_age())

"""
    使用属性封装
"""
class Wife01:
    def __init__(self,name='',age=0):
        self.name=name #调用@name.setter 修饰的方法
        self.age=age #调用@age.setter 修饰的方法
    @property#拦截读取变量的操作
    def name(self):
        return self.__name
    @name.setter#拦截写入变量的操作
    def name(self,value):
        self.__name=value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        self.__age=value
w01 = Wife01("张三",25)
print(w01.name)
