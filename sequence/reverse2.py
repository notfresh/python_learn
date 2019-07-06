ls1 = [2, 4, 8, 0]
ls1.sort(key=lambda x, y:abs(x)-abs(y))
print(ls1)