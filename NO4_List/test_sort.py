a = ['a', 'abc', 'aa', 'ab', 'bb', 'ba']
print(sorted(a)) # 跟普通排序没有区别

def f1(a):
    a[1] += 1
    print(1)

def f2(a):
    f1(a)
    print(2)


def f3(a):
    f2(a)
    print(3)


if __name__ == '__main__':
    import pdb
    pdb.set_trace()
    f3({1:1})
