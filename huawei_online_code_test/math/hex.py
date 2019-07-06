import sys

input = sys.stdin.readline


def f1(arg1):
    arg1 = arg1[2:]
    dict1 = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    dict1_k = dict1.keys()
    ls1 = list(arg1)[::-1]
    v1 = 0
    index = 0
    for item in ls1:
        if item in dict1_k:
            v1 += dict1[item] * (16**index)
        else:
            v1 += int(item) * (16**index)
        index += 1

    out = str(v1)
    return out

in1 = input().strip() #     0xC460
out = f1(in1)
print(out)

