a = b = c = 1
print(a, b, c)

class A:
    aaa = 1

    def __init__(self):
        print("abcd")

a1 = a2 = a3 = A()
print(a1 is a2)
print(a1, a2, a3)
a4 = None

# def f1(a1, a2):
#     return a2 or a1
#
# print(a4 or a4)