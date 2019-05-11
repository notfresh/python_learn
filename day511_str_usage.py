# coding=utf-8

# question1: 如何从字符串里删掉一个指定唯一字符？
a = '12345'
print(a.index('2'))
print(a[:a.index('2')]+a[a.index('2')+1:])
# 注意，字符串没有remove方法
# 但是可以把字符串抓化成list来做

print(list(a).remove('1'))
# 经过尝试失败， 因为remove方法执行正常是不会返回原值的。