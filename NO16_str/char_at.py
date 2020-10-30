a = "abcd/efg.jpg&a=1"
a = a[:a.index('?')]
c = a.split('/')[-1]
print(c)