import sys

input = sys.stdin.readline
inv1 = int(input().strip())

dict1 = {}
index = 0
while index < inv1:
    inv_kv = list(map(lambda x: int(x), input().strip().split()))
    if dict1.get(inv_kv[0]):
        dict1[inv_kv[0]] += inv_kv[1]
    else:
        dict1[inv_kv[0]] = inv_kv[1]
    index += 1
# output
dict1_k = list(dict1.keys())
dict1_k.sort()
for item in dict1_k:
    print(item, dict1[item], sep=' ')


# 248
# 32 2411
# 184 72567
# 106 32959
