#coding=utf-8
import os
file = os.path.join(os.environ['HOME'], ".md-tool-config.yml")


def size(vlist):
    return len(vlist)


def split(vlist, spliter):
    pos = []
    i = 0
    for item in vlist:
        if item == spliter+'\n':
            pos.append(i)
        i += 1
    pos.insert(0, -1)
    pos.append( len(vlist))

    # [0,1,2]
    print('pos',pos)
    res = []
    for j in range(len(pos)-1):
        part = vlist[pos[j]+1: pos[j+1]]

        # 去掉前面的空行
        for i in range(len(part)):
            if part[i].strip() != '':
                break
        part = part[i:]
        # print(part)
        res.append(part)
    return res


def write_file(vlist, file):
    with open(file, mode='w+', encoding='utf-8') as f:
        f.writelines(vlist)


# file_name_num = 0
file_num_file = '/Users/zxzx/projects/interview/算法/Algo/.file_number.txt'

def load_file_num():
    with open(file_num_file) as f:
        lines = f.readlines()
    number = int(lines[0].strip())
    return number

file_name_num = load_file_num()


def set_file_num(new_num):
    with open(file_num_file, 'w+') as f:
        f.write(str(new_num))


def split_file(file_name, output_file_dir, spliter):

    if not os.path.exists(output_file_dir):
        os.mkdir(output_file_dir)

    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()

    res = split(lines, spliter)

    global file_name_num
    for item in res:
        write_file(item, output_file_dir + '/' + str(file_name_num) + '.txt')
        file_name_num += 1
    set_file_num(file_name_num)


def split_algo_file_1():
    algo = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-排序.md'
    algo_file_dir = '/Users/zxzx/projects/interview/算法/Algo'

    # file_name = algo
    output_file_dir = algo_file_dir
    spliter = '$$$$$'

    algo1 = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-排序.md'
    algo2 = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-查询.md'
    algo3 = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-链表.md'
    algo4 = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-树.md'
    algo5 = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理.md'
    file_names = [algo1, algo2, algo3, algo4, algo5]

    for file_name in file_names:
        split_file(file_name, output_file_dir, spliter)


def split_algo_file_2():
    algo = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-排序.md'
    algo_file_dir = '/Users/zxzx/projects/interview/算法/Algo'
    # file_name = algo
    output_file_dir = algo_file_dir
    spliter = '$$$$$'
    algo1 = '/Users/zxzx/projects/interview/算法/DA16-优秀代码收录-原创与少数整理-动态规划/DA16-优秀代码收录-原创与少数整理-动态规划.md'
    file_names = [algo1]

    for file_name in file_names:
        split_file(file_name, output_file_dir, spliter)


def split_algo_file_3():

    algo_file_dir = '/Users/zxzx/projects/interview/算法/Algo'
    # file_name = algo
    output_file_dir = algo_file_dir
    spliter = '$$$$$'
    algo1 = '/Users/zxzx/projects/interview/算法/面试准备-面经算法收集.md'
    file_names = [algo1]

    for file_name in file_names:
        split_file(file_name, output_file_dir, spliter)

# def update_suffix():
#     algo_file_dir = '/Users/zxzx/projects/interview/算法/Algo'
#     for file in os




def insert_rank_factor(file_name):
    print('file_name: {}'.format(file_name))
    # file =
    # file_name = '/Users/zxzx/projects/interview/算法/Algo/32.txt'
    rank_factor = """
    
$$${
实用性:
难度: 
标签: 
兴趣:
名称:
完整程度:
不完整程度:
$$$}

        """
    with open(file_name, encoding='utf-8') as f:
        lines = f.readlines()

    # 去掉前面的空行
    k = 0
    for i in range(len(lines)):
        if lines[k].strip() == '':
            break
        k+=1

    lines.insert(k, rank_factor)

    with open(file_name, encoding='utf-8', mode='w+') as f:
        f.writelines(lines)
    print('file_name: {} 插入完成'.format(file_name))


def insert_rank_factor_for_all():
    dir_ = '/Users/zxzx/projects/interview/算法/Algo/'
    files = os.listdir(dir_)
    files = [file for file in files if not file.startswith('.')]
    for file_name in files:
        if has_rank_factor(os.path.join(dir_, file_name)):
            print('file_name: {} 跳过'.format(file_name))
            continue
        insert_rank_factor(os.path.join(dir_, file_name))



left_c = '$$${\n'
right_c = '$$$}\n'


def extract_rank_factor(filename):
    """
    提取一个文件中的排序因子
    类似于这种格式:

    $$${
    实用性: 3
    难度: 3
    标签: 查找
    名称: 两个数组中的中位数,lt4
    $$$}

    :param filename:
    :return:
    """
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    ls = lines[:50]
    stack = []
    pos = []
    k = 0
    for item in ls:
        if item == left_c:
            stack.append(item)
            pos.append(k)
        elif item == right_c:
            if stack[-1] == left_c:
                stack.pop()
            pos.append(k)
        k += 1
    res = []
    # print('pos', pos)
    if stack == []:
        # print('合法')
        k2 = 0
        while k2 < len(pos):
            res.append(ls[pos[k2] + 1:pos[k2 + 1]])
            k2 += 2
    else:
        # print('不合法')
        pass
    return res

def has_rank_factor(filename):
    """
    检测是否已经有rank因子了
    """
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    ls = lines[:50]
    stack = []
    pos = []
    k = 0
    for item in ls:
        if item == left_c:
            stack.append(item)
            pos.append(k)
            return True
        elif item == right_c:
            if stack[-1] == left_c:
                stack.pop()
            pos.append(k)
        k += 1
    return False





def parse_rank_factor(res):

    dict_ = {}
    for item in res:
        for line in item:
            # print(line)
            line = line.strip()
            kv = line.split(':')
            try:
                dict_[kv[0].strip()] = kv[1].strip()
            except:
                print('@100, error:',line)
    return dict_



def cal(vdict):
    """
    根据 rank因子 计算复杂度和实用性
    :param vdict:
    :return:
    """
    score = 0
    weight = {
        '实用性': 10,
        '难度': 20,
        '兴趣': 30,
        '熟悉程度': 10,
        '滞后': -5,
        '练习次数': -5,
        '不完整程度': -10
    }
    for k, v in vdict.items():
        if k == '实用性':
            if v == '': v = 0
            v = int(v)
            v1 = weight.get(k) * v
            score += v1
        elif k == '难度':
            if v == '': continue
            v = int(v)
            v1 =  (weight.get(k) * (10-v))// 5
            score += v1
        elif k == '熟悉程度':
            if v == '': continue
            v = int(v)
            v1 =  (weight.get(k) * (10-v))
            score += v1
        elif k == '兴趣':
            if v == '': v=0
            v = int(v)
            v1 =  weight.get(k) * v
            score += v1
        elif k == '滞后':
            if v == '': continue
            v = int(v)
            v1 =  weight.get(k) * v
            score += v1
        elif k == '练习次数':
            if v == '': continue
            v = int(v)
            v1 =  weight.get(k) * v
            score += v1
        elif k == '不完整程度':
            if v == '': continue
            v = int(v)
            v1 =  weight.get(k) * v
            score += v1
    return (score if score > 0 else 0)



def rank(filenames):
    res = []
    for file in filenames:
        if not os.path.exists(file): continue # 跳过不存在的文件
        factor = extract_rank_factor(file)
        factor_dict = parse_rank_factor(factor)
        score = cal(factor_dict)
        res.append([score, file, factor_dict])
    res.sort(key=lambda x: -x[0])
    return res

def make_valid_name(vname):
    vname = vname.split(',')[0]
    return vname

def get_source_name(vname):
    vname = vname.split('/')[-1]
    vname = vname.split('.')[0]
    return vname


def del_files(path_file):
    ls = os.listdir(path_file)
    for i in ls:
        f_path = os.path.join(path_file, i)
        # 判断是否是一个目录,若是,则递归删除
        if os.path.isdir(f_path):
            del_files(f_path)
        else:
            os.remove(f_path)

def rank_and_copy(files):
    from shutil import copyfile
    rank_dir_ = '/Users/zxzx/projects/interview/算法/Algo_rank/'
    del_files(rank_dir_)
    res = rank(files)
    rank_num = 0
    for line in res:
        copyfile(line[1],
                 '{}{}_{}_{}_{}.md'.format(rank_dir_,
                                    str(rank_num),
                                    line[0], # 分数
                                    make_valid_name(line[2].get('名称','')), # 名称
                                    get_source_name(line[1])
                                      )
                 )
        print('@200', line)
        rank_num += 1

if __name__ == '__main__':
    # file_name = '.md-tool-config.yml'
    # output_file_dir = 'abc'
    # spliter = '$$$'
    # with open(file, "w+") as f:
    #     f.write("111")
    # set_file_num(1000)
    # split_algo_file_3()
    # insert_rank_factor_for_all()


    files = [ '/Users/zxzx/projects/interview/算法/Algo/{}.txt'.format(i)
        for i in range(20)
    ]
    rank_and_copy(files)
















