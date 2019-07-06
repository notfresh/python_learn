import sys

input = sys.stdin.readline
a = input().strip()
b = input().strip()
out = []

def strsplit_in8(str_in):
    length = len(str_in)
    if length < 8:
        return [str_in + '0' * (8 - length)]
    else:
        out = []
        i = 0
        while length > 8:
            i += 8
            substr = str_in[i - 8:i]
            out.append(substr)
            length -= 8
        out.append(str_in[i:] + '0' * (8 - length))
        return out


out.extend(strsplit_in8(a))
out.extend(strsplit_in8(b))
for i in out:
    print(i)




