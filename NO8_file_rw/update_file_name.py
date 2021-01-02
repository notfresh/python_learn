# coding=utf-8

# 为了批量更改markdown时间的文件命名

import os, json


class SimpleSerialize:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            self.dump({}) # init方法可以调用其他方法

    def dump(self, data):
        # 使用内置库 json
        with open(self.file_path, 'w+', encoding='utf-8') as f:
            json.dump(data, f)

    def load(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def append(self, k, v):
        data = self.load()
        data[k] = v
        self.dump(data)


file_name = '13.md'

def new_name_with_line1(file_name):
    pesistence_file_name = 'markdown_rename.txt'

    # get the 1st line
    file = open(file_name, 'r', encoding='utf-8')
    txt = file.readline().strip()
    file.close()

    # filter the unwanted chars
    txt_new = []
    length = len(txt)
    for i in range(length):
        if txt[i] not in ('#', ' '):
            txt_new.append(txt[i] )

    try: # remove the  chars before '|'
        _index = txt_new.index('|')
        print(_index)
        txt_new = txt_new[_index+1:]
    except:
        pass

    # make the new name
    txt_new = ''.join(txt_new)
    dot_index = file_name.index('.')
    new_file_name = file_name[:dot_index] + txt_new + file_name[dot_index:]
    print(new_file_name)

    # persistence in case of error
    s = SimpleSerialize(pesistence_file_name)
    s.append(file_name, new_file_name)

    # update the name
    os.rename(file_name, new_file_name)


names = [str(item) + '.md' for item in range(1,100) ]
for item in names:
    if os.path.exists(item):
        new_name_with_line1(item)

