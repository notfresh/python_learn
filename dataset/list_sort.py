ls1 = [1, 2, 3, 5, -1, -9]
ls1.sort(key=lambda x: abs(x))
print(ls1)

# 排序
a = [1, 2, 3, 0, -1]
a.sort()
print(a)


# 双字段排序

ls = ['ab', 'ba', 'a']
# 先按长度排序, 再按字典序排序
ls.sort(reverse=True)
ls.sort(key=len, reverse=True)
print(ls)

ls = [None, 1, 2]
ls.sort()  # 有None会直接报错. 
print(ls)