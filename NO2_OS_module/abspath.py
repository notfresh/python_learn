#! /usr/local/bin/python3
import sys, os

try:
    import pyperclip
except:
    print("please use `pip3 install pyperclip` to install the pyperclip module dependency")
    sys.exit(1)

try:
    file_path = sys.argv[1]
except:
    print('use abspath.py THE_FILE_YOU_WANTO_HANDLE to get abspath')
cwd = os.getcwd()
abs_path = os.path.join(cwd, file_path)
pyperclip.copy(abs_path)
print(abs_path)
print('the abspath has copied to the clipboard')