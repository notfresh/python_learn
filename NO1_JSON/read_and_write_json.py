import json
import os
# a = {1:2, 3:4, 'b': [1,2,3,4,5,6]}
# json_file = 'test.txt'
# with open(json_file, 'w+' ,encoding='utf-8') as f:
#     json.dump(a, f)
#
# b = None
# with open(json_file, 'r', encoding='utf-8') as f:
#     b = json.load(f)
# print(b)


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


s = SimpleSerialize('new.txt')
s.append('1', '2')
s.append('你好', [1, 2, 3, 4])



