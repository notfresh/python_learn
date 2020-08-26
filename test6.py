# 第一行一个数n，代表有n个数
#
# 接下来n个数，描述这n个数a1, a2 , .. ,an
#
# 1≤n≤100      1≤ai≤10000
# 输出
# 一个数，最大的汉明距离
#
#
# 样例输入
# 3
# 1 2 3
# 2
n = int(input())
line = [int(item) for item in input().split(' ')]
# def count1(num):
#     res = 0
#     while num != 0:
#         tmp = num & 1
#         if tmp:
#             res += 1
#         num = num >> 1
#     return res
#
# counter = [[count1(item), item] for item in line]
# print(counter)
# counter.sort(key=lambda x:x[0])


def hamming_distance(m, n):
    res = 0
    while m or n:
        a = m & 1
        b = n & 1
        if a != b:
            res += 1
        m = m >> 1
        n = n >> 1
    return res


res = 0
for i in range(n):
    for j in range(i+1, n):
        res = max(res, hamming_distance(line[i], line[j]))
print(res)

