# coding=utf-8

# list的几个让人疑惑的语法？
list1 = [1, 2, 3]
try:
    print(list1 + 2)
    # ↑上面的这句话语法对吗？ 不对。 TypeError: can only concatenate list (not "int") to list
except Exception as e:
    print(e)



#  给每个元素加2 只能用列表解析
list2 = [ item +2 for item in list1]
print(list2)

# 列表之间的拼接
list3 = [1]
print(list1 + list3)
print(list1)


# list截取到倒数第一个
print(list1[:-1])
# list截取到倒数第二个，不包含第二个
print(list1[:-2])


#
print('*'*100)
list1 = [1,2]
list2 = [[2,3], [4,5]]
# 如何给list2的每个元素都加上list1的元素
list2 = [list1 + item for item in list2]
print(list2)


# list当栈用
print("*"*100)
ls = [1, 2, 3, 4]
print(ls.pop())
print(ls.pop())
print(ls)
print(ls.pop())
print(ls.pop())
print(ls)
