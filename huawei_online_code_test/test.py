import re

ins = input()
ls = ins.split(';')

rem = re.compile(r'[ADWS]\d{1,2}')
lsf = filter(lambda x:rem.match(x), ls)
lsf_2 = [ (item[0], int(item[1:])) for item in lsf]
p = [0, 0]
for k,v in lsf_2:
    if k == 'A':
        p[0] -= v
    elif k == 'D':
        p[0] += v
    elif k == 'W':
        p[1] += v
    elif k == 'S':
        p[1] -= v
print(p[0],p[1], sep=',')

in_ls = []
d = {}
while True:
    try:
        inv = input().split()
        inv[0] = inv[0].split('\\')[-1][-16:]
        k = ' '.join(inv)
        if d.get(k):
            d[k] += 1
        else:
            d[k] = 1
    except:
        break
for item in d.keys()[-8:]:
    print(item + ' ' + d[item])


