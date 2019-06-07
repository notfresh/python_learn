# coding=utf-8

# 请仔细阅读这篇文章
# https://blog.csdn.net/weixin_41666747/article/details/79942847

class A:
    def __new__(cls, *args, **kwargs):
        print('AAA')
        return object.__new__(cls)

    pass


class A1(A):

    def __init__(self):
        print(111)
        pass

    def __new__(cls, *args, **kwargs):
        print(222)
        # super代表的父类
        # 调用父类new对象，但是这个东西在python里很少用到，啰嗦的很。
        return super().__new__(cls)


class A2:

    def __init__(self):
        print(1113)
        pass

    def __new__(cls, *args, **kwargs):
        print(2223)
        return object()


class A3:

    def __init__(self):
        print(1114)
        pass

    def __new__(cls, *args, **kwargs):
        print(2224)
        return object.__new__(cls)


if __name__ == '__main__':
    a = A1()
    print(type(a))
    # a2 = A2()
    # print(a2)
    # a3 = A3()
    # print(a3)