the_str = input()
k = int(input())

def is_valid(the_str, k):
    length = len(the_str)
    if length < k*2 + 1:
        return 0
    i = k
    while i <= (length - 1)//2:
        if the_str[:i] == the_str[length-i:]:
            return 1
        i += 1
    return 0

res = 0
length = len(the_str)
for l in range(length):
    for r in range(l, length):
        res += is_valid(the_str[l:r+1], k)

print(res)

