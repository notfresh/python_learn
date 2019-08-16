import os

path1 = '/users/zxzx/todo/left_notebook/'
path2 = '/users/zxzx/todo/right_notebook/'
path3 = '/users/zxzx/todo/notebook/'

lefts = [item for item in os.listdir(path1) if not item.startswith('\.')]
lefts.sort()
print(lefts)

rights = [item for item in os.listdir(path2) if not item.startswith('\.')]
rights.sort()
print(rights)

i = 0
left_iter = iter(lefts)
right_iter = iter(rights)
prefix = 'page-{:0>3}.jpg'
while True:
    try:
        if i >= 2:
            i += 1
            left = next(left_iter)
            os.rename(path1 + left, path3 + prefix.format(i))
            print('rename {} to {}'.format(path1 + left, path3 + prefix.format(i)))
        i += 1
        right = next(right_iter)
        os.rename(path2 + right, path3 + prefix.format(i))
        print('rename {} to {}'.format(path2 + right, path3 + prefix.format(i)))
    except StopIteration as e:
        break
