import jieba, os

if __name__ == '__main__':
    key_word = ('epoll', '进程', '线程', '编译', '共享内存', '对象', '洗牌', 'extern', '面向对象',
                '模板', '多线程', '通信', '设计模式', '锁', '内核', 'linux', '哈希', 'stl', 'STL', 'vector',
                'map','Linux', 'B+树','TCP', '虚函数', '纯虚函数', '哈希表','构造函数','CAS', '红黑树',
                '地址空间','智能指针','调度','调度算法','析构函数', '红黑树', 'avl'
                )
    dir_ = '/Users/zxzx/projects/nowcoder_exp/字节跳动-实习面经/'
    files = os.listdir(dir_)
    files = [item for item in files if not item.startswith('.')]
    # files = [
    #     os.path.join(dir_,'{}.txt'.format(num)) for num in range(0, 305)
    # ]
    files = [
        os.path.join(dir_, file) for file in files
    ]
    # file = "/Users/zxzx/projects/nowcoder_exp/字节跳动-实习面经/0.txt"
    map_ = {}
    for file in files:
        with open(file, encoding="utf-8") as f:

            file_content = f.read()
        # print(file_content)
        jieba.load_userdict('dict.txt')
        seg_list = jieba.cut(file_content, cut_all=False)
        # print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
        for word in seg_list:
            if word not in key_word: continue
            if map_.get(word):
                map_[word]+=1
            else:
                map_[word] = 1
    res = []
    for k,v in map_.items():
        res.append([k,v])
    res.sort(key=lambda x:-x[1])
    print(res)




