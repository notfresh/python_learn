# coding=utf-8
# map是个什么函数呢？
# 对一个列表的每个元素进行相同的操作

def f1(x):
    return x**2


list1 = [1, 2, 3, 4]
list2 = map(f1, list1) # map不改变原有参数
print(list1) # [1, 2, 3, 4]
print(list2) # [1, 4, 9, 16]

list1 = map(lambda x: x*2,range(1, 100))
print(type(range(1, 100)))
print(type(list1))
print(list1)