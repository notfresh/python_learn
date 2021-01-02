def f1(a, *b): #
    print(a)
    print(b)

def f2(a, *b, **c): # f2(1,2,2,3,5,a1=3,b=4,c=5) # @param_pack @pack
    print(a) # 1
    print(b) # (2, 2, 3, 5)
    print(c) # {'a1': 3, 'b': 4, 'c': 5}

if __name__ == '__main__':
    # f2(1,2,2,3,5,a1=3,b=4,c=5)
    f2(1,2,3,4, {'a':1,'b':2})