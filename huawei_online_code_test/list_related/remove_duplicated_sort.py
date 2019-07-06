import sys

while True:
    try:
        input = sys.stdin.readline
        n = int(input())
        arr = []
        i = 0
        while i < n:
            i += 1
            arr.append(int(input()))
        arr = list(set(arr))
        arr.sort()
        for i in arr:
            print(i)
    except:
        break
