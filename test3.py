n = int(input())
line = [int(item) for item in input().split(' ')]
res = [-1 for i in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if res[i] == 1:
            continue
        if line[i] & line[j] == 0:
            res[i] = 1
            res[j] = 1

# res = [1, 2]
for i in res:
    print(i, end=' ')






