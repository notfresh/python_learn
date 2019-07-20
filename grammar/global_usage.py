a = 1

def f1():
    global a
    # 使用global修饰的变量必须在函数外定义好, 或者先声明, 后定义!! 不能定义后再声明.
    # b = 0
    global b
    b = 2
    a = 3
f1()
print(a)
print(b)

a1 = 3

def f2():
    global a1
    a1 += 3

f2()
f2()
print(a1)


try:
    def f1():
        global x
        x = 3
    f1()
    print(x)
except Exception as e:
    print(e)

# d x
