#coding=utf-8
"""
@version: ??
@author: Muyi
@Mail: 768322192@qq.com
@file: 静态方法.py
@time: 2021/2/5 15:51
"""
"""
@staticmethod  静态方法
def 方法名称（参数列表）
    方法体 
"""

class Vector2:
    """
    向量
    """
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    #  @staticmethod 将函数转移到类中，就是静态方法
    @staticmethod
    def right():
        return Vector2(0,1)

    @staticmethod
    def up():
        return Vector2(-1,0)

    @staticmethod
    def down():
        return Vector2(1,0)

    @staticmethod
    def left():
        return Vector2(0,-1)

    @staticmethod
    def right_up():
        return Vector2(-1,1)

class DoubleListHelper:
    """
        二位列表助手类：
            在开发过程中，对所有二位列表的常用操作
    """
    @staticmethod
    def get_elements(list_target,v_pos,v_dir,count):
        result=[]
        for i in range(count):
        #x代表行，y代表列
        #位置 1 0  --> 方向 0  1
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result
list01 = [
    ["00","01","02","03"],
    ["30","11","12","13"],
    ["20","21","22","23"]
]
#30 向右   3   ---->11 12 13  行不变，列加1
re01 = DoubleListHelper.get_elements(list01,Vector2(1,0),Vector2.right(),3)
print(re01)
#21         向上   2      ---------->11 01 列不变，行减1

re02 = DoubleListHelper.get_elements(list01,Vector2(2,1,),Vector2.up(),2)
print(re02)
