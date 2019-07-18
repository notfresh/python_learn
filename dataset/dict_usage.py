# coding=utf-8
# 如何使用dict,字典呢？
dict1 = {'a': 1, 'b': 2}
for i in dict1.items():
    print(i[0], i[1])
# 评， 一定要使用 dict1.items(), item是方法不是属性。


# https://blog.csdn.net/JavaMoo/article/details/77652395
# 默认值使用, setdefault
# test
print('*'*100)
d = {}
d[1] = d.setdefault(1, 0) + 1
print(d)

print('*'*100)
d1 = ['*'] * 10
print(d1)

print('*'*100)
print("测试[]的默认值设置")
a = {}
# print(a['b', 1])
print(a.get('b', 1))
print(a.get('b'))

