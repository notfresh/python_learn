# coding=utf-8

# question1: 如何从字符串里删掉一个指定唯一字符？
a = '12345'
print(a.index('2'))
print(a[:a.index('2')]+a[a.index('2')+1:])
# 注意，字符串没有remove方法
# 但是可以把字符串抓化成list来做

print(list(a).remove('1'))
# 经过尝试失败， 因为remove方法执行正常是不会返回原值的。


# 如何依次切割12345
print("*"*100)
a = '12345'
print(a[0:0]+a[1:])
print(a[0:1]+a[2:])
print(a[0:2]+a[3:])
print(a[0:3]+a[4:])
print(a[0:4]+a[5:])  # 这里很厉害， python可以自己动检测出越界下标，从而忽略掉。
# 比如下面这个
print(a[5:])  # 返回 None

# 如何快速得到字符串的反转？
print("*"*50+'字符串反转'+'*'*50)
a = '12345'
print(a[::-1])

# 如何局部修改一个字符串
print("*"*50+'字符串局部修改'+'*'*50)
a = '12345'
a_list = list(a)
a_list[1] = '9'
print(''.join(a_list))


# 字符串分割
str1 = 'world'
print(str1[-10:])
print(str1[10:])




