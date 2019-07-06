# coding=utf8

# 字符串切割
# 参考 https://www.cnblogs.com/douzi2/p/5579651.html
str1 = 'Hello  world' # 两个空格, 很神奇, 原因参考上面的解释
print(str1.split())
print(str1.split(' '))


import  sys
s=sys.stdin.readline()
print(len(s.split()[-1]))

