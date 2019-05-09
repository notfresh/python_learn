# coding=utf-8
# 在一个class中， __repr__方法和__str__方法有什么区别呢？
# 我们来测试一下

class A:
    def __init__(self, name):
        self.name = name

    def __str__(self): # __str__方法一定要有 return 值， 否则print 一个A对象就会报错。
        return '__str__ method: My name is {}'.format(self.name)

    def __repr__(self): # __str__方法一定要有 return 值， 否则print 一个A对象就会报错。
        return '__repr__ method: My name is {}'.format(self.name)


# 若 a = A('tom')
# 经过测试发现， print(a)会调用 __str__方法，而__repr__方法则会在交互解释器中调用。
# repr是 represent的缩写，就是展示的意思。 一般默认会打印内存地址
# 如果没有重写 __str__方法， 而只写了 __repr__, 那么print则会调用 __repr__方法
# 反之则不会

class A2:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '__repr__ method: My name is {}'.format(self.name)

class A3:
    def __init__(self, name):
        self.name = name

    def __str__(self): # __str__方法一定要有 return 值， 否则print 一个A对象就会报错。
        return '__str__ method: My name is {}'.format(self.name)