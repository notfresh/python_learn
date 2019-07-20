try:
    a = 1/0
except Exception as e:
    print(e)

try:
    a = [1, 2, 3]
    print(a[3])
except Exception as e:
    print(e)


try:
    def f1():
        global x
        x = 3
    f1()
    print(x)
except Exception as e:
    print(e)

# 注意!!
# try catch只能捕获运行错误, 不能捕获语法错误!!!!!!!!!!
