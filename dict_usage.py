# coding=utf-8
# 如何使用dict,字典呢？
dict1 = {'a': 1, 'b': 2}
for i in dict1.items():
    print(i[0], i[1])
# 评， 一定要使用 dict1.items(), item是方法不是属性。