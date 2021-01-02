#! /usr/local/bin/python3
#coding=utf-8

import re


file_path = ''

import sys, os

file_path = sys.argv[1]

cwd = os.getcwd()

if os.path.exists(file_path):
    file_path = file_path
elif os.path.exists(os.path.join(cwd, file_path)):
    file_path = os.path.join(cwd, file_path)
else:
    print("md file not exist")
    sys.exit(1)


def update():
    with open(file_path,encoding='utf-8') as f:
        str1 = f.read()

    pattern = "(\s)(http[s]*://[\.a-zA-Z\?/_0-9\-]+)(\s*)" # \s可以表示换行符,空格
    str1 = re.sub(pattern, r"\1[\2](\2)\3", str1)


    with open(file_path, encoding='utf-8' ,mode='w+') as f:
        f.write(str1)
    print('file url update success')





if __name__ == '__main__':
    # test_what_is_re_sub_example2()
    # str1 = simple_sub()
    update()
    # print(file_path)