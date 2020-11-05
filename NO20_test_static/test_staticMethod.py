class T:
    @staticmethod
    def f1():
        print(11)

    @staticmethod
    def f1(a,b):
        print(2222)

class T2:

    def f1(self,a,b):
        print(2222)

    # 无法重载
    def f1(self):
        print(11)

if __name__ == '__main__':
    t2 = T2()
    t2.f1(1,2)

