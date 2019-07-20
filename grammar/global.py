a = 1
def f1():
    global a
    # 使用global修饰的变量必须在函数外定义好
    # try:
    #     b = 0
    #     global b
    #     b = 2
    # except Exception as e:
    #     print(e)
    a = 3


print(a)
# print(b)

a1 = 3

def f2():
    global a1
    a1 += 3

f2()
f2()
print(a1)

