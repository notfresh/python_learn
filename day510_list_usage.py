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