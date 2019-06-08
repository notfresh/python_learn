# coding=utf-8

class A:
    attr1 = 1
    def f1(self):
        print('A')


class B(A):
    attr1 = 2
    def f1(self):
        print('B')


class C(A):
    attr1 = 3
    def f1(self):
        print('C')

    def f2(self):
        print('CCCC')


class D(B, C):
    pass

if __name__ == '__main__':
    d = D()
    d.f1()
    # output B, the first father class has priority to keep its attributes and functions
    print(d.attr1)
    d.f2()