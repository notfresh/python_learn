# coding=utf-8

# question1: python的传参问题
#

list1 = [1, 2, 3, 4]

def f1(listx):
    listy = listx
    listy.append(5)

f1(list1)
print(list1) # [1, 2, 3, 4, 5]

# 下面这个用例更说明了这个问题：
print('*'*100)
def f1(i, list1):
    if i > 2:
        return

    print(list1)
    list1.pop()
    f1(i+1, list1)
    print("***",list1)

i = 0
list1 = [1, 2, 3, 4, 5]
f1(i, list1)
print(list1)

# [1, 2, 3, 4, 5]
# [1, 2, 3, 4]
# ('***', [1, 2, 3])
# ('***', [1, 2, 3])
# [1, 2, 3]
# 这个测试例子说明了什么？
# 说明了list是一个对象，在递归中被改变了，那么即使退出某一层，也是被永久改变了，内存中只有一份！！
# 这就是对象引用传参的方式。为了节省内存。