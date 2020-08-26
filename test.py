print(124)
m, n = [ int(item) for item in input().split(' ')]
matrix = []
for i in range(m):
    line = [int(item) for item in input().split(' ')]
    matrix.append(line)

top_score = []
for i in range(n):
    tmp = -1
    for j in range(m):  # 遍历列
        tmp = max(tmp, matrix[j][i])
    top_score.append(tmp)

res = set()
for i in range(m):
    for j in range(n):
        if matrix[i][j] == top_score[j]:
            res.add(i)
print(len(res))