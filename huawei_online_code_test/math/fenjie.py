import sys

input = sys.stdin.readline
out = ''
inv = int(input().strip())

for item in range(2, inv // 2 + 1):
    while inv % item == 0:
        out += (str(item) + ' ')
        inv /= item
    if inv < item:
        break

print(out if out else str(inv) + ' ')

# TODO 分值质数的单词怎么写.