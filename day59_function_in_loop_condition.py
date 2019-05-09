# coding=utf-8
# for i in range(0, function) 请问这个function执行一次还是很多次呢？
# 我们来做个试验

def len_log(list1):
    print('call the function len_log')
    return len(list1)

list1 = [1, 2, 3, 4]
for i in range(0, len_log(list1)):
    print(list1[i])

# call the function len_log
# 1
# 2
# 3
# 4
# 看来只调用了一次， 我们现在换while试一下

i = 0
while i < len_log(list1):
    print(list1[i])
    i += 1

# 输出结果
# call the function len_log
# 1
# call the function len_log
# 2
# call the function len_log
# 3
# call the function len_log
# 4
# call the function len_log

# 这说明在while判断条件中，函数被调用了4次
# 为了提高代码执行的效率， 应该这么做：

i = 0
length = len_log(list1)
while i < length:
    print(list1[i])
    i += 1

# 这样可以保证循环检查条件只调用一次， 如果循环检查条件不变的话。