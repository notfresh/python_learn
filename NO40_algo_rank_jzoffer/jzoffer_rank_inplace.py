#coding=utf-8
import os

# file_name_num = 0
g_rank_dir_ = '/Users/zxzx/projects/interview/算法/algo_rank_jzoffer'
file_num_file = os.path.join(g_rank_dir_, '.file_number.txt')

g_rank_factor = """
$$${
实用性:
难度: 
标签: 
兴趣:
名称:
完整程度:
不完整程度:
重要程度:
代码难度:
代码量: 
$$$}
        """
g_weight = {
        '实用性': 10,
        '难度': -10,
        '兴趣': 30,
        '熟悉程度': -10,
        '滞后': -100,
        '练习次数': -50,
        '不完整程度': -10,
        '重要程度': 15,
        '代码难度': -25,
        '代码量': -10,
        '代表性': 40,
        '待办': 100,

    }

g_tag_weight = {
        '排序': 10,
        '查找': 100,
        '树': 1000,
        'TODO': 500
    }

g_rank_num_factor = [
        '实用性','难度','熟悉程度', '兴趣' ,'滞后', '练习次数',
        '不完整程度','重要程度', '熟悉程度', '代码难度', '代表性'
    ]


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


def load_file_num():
    if not os.path.exists(file_num_file):
        return 0
    with open(file_num_file) as f:
        lines = f.readlines()
    number = int(lines[0].strip())
    return number

file_name_num = load_file_num()

def set_file_num(new_num):
    with open(file_num_file, 'w+') as f:
        f.write(str(new_num))


def split_file(file_name, output_file_dir, spliter):
    if file_name == file_num_file: return  # 免去
    if not os.path.exists(file_name): return  # 跳过不存在的文件
    if os.path.isdir(file_name): return  # 跳过文件夹


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
    print("删除文件{} ".format(file_name))
    os.remove(file_name)

def split_algo_file_1():
    output_file_dir = g_rank_dir_
    splitter = "$$$$$"
    file_names = os.listdir
    file_names = [item for item in file_names if not item.startwith('.')]
    file_names = [os.path.join(g_rank_dir_, item) for item in file_names]
    for file_name in file_names:
        split_file(file_name, output_file_dir, splitter)


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
重要程度:
代码难度:
代码量: 
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
    dir_ =  g_rank_dir_
    files = os.listdir(dir_)
    files = [file for file in files if not file.startswith('.')]
    for file_name in files:
        file = os.path.join(dir_, file_name)
        if not os.path.exists(file): continue  # 跳过不存在的文件
        if os.path.isdir(file): continue  # 跳过文件夹
        if has_rank_factor(os.path.join(dir_, file_name)):
            print('file_name: {} 跳过'.format(file_name))
            continue
        insert_rank_factor(os.path.join(dir_, file_name))



left_c = '$$${\n'
right_c = '$$$}\n'

cur_file = ''
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
    global cur_file
    cur_file = filename
    if os.path.isdir(filename): return None
    try:
        with open(filename, encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(e)
        print(filename)
        import sys
        sys.exit(2)
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
            if not line: continue # 空白行,跳过
            kv = line.split(':')
            try:
                dict_[kv[0].strip()] = kv[1].strip()
            except:
                print('@100, error:', line, cur_file)
    return dict_


def cal(vdict):
    """
    根据 rank因子 计算复杂度和实用性
    :param vdict:
    :return:
    """
    score = 0
    weight = g_weight
    tag_weight = g_tag_weight
    value_attrs= g_rank_num_factor
    for k, v in vdict.items():
        try:
            if k in value_attrs:
                if v == '': continue
                v = int(v)
                v1 = weight.get(k) * v
                score += v1
            elif k == '标签':
                tags = v.split(',')
                tags = [item.strip() for item in tags if item.strip()]
                for tag in tags:
                    score += tag_weight.get(tag, 0)
        except Exception as e:
            print(cur_file)
            raise e

    return (score if score > 0 else 0)


def getNumber(str_):
    number = 0
    for chr in str_:
        if chr.isdigit():
            number = number*10 + int(chr)
        else:
            break
    return number


def rank_dir(dir_, count=50, rank_by='SCORE'):
    if count<0: count = 0
    # 输入待排序的文件名字,输出排序后的结果
    files = os.listdir(dir_)
    filenames = sorted(files, key=lambda x: getNumber(x) )[:count]
    # print(filenames)
    filenames = [os.path.join(dir_, file) for file in filenames] # 完整路径
    res = []
    for file in filenames:
        if not os.path.exists(file): continue # 跳过不存在的文件
        if os.path.isdir(file): continue  # 跳过不存在的文件
        if file.split('/')[-1].startswith('.'): continue  # 跳过.开头的文件
        factor = extract_rank_factor(file)
        factor_dict = parse_rank_factor(factor)
        score = cal(factor_dict)
        origin_file_name = file.split('/')[-1]
        try:
            file0sufix =  int(origin_file_name.split('.')[0].split('_')[-1])
        except:
            print(origin_file_name)
        res.append([score, file, factor_dict, file0sufix])
    if rank_by == 'SCORE':
        res.sort(key=lambda x: -x[0])
    elif rank_by == 'FILE_NUM':
        res.sort(key=lambda x: x[3])
    return res

def make_valid_name(vname):
    """
    根据传入的名称,去掉不合法的字符串,当做文件的名称
    :param vname:
    :return:
    """
    # vname = vname.split('.')[0]
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

def rank_and_copy(rank_count=10, rank_by='SCORE'):
    from shutil import copyfile
    rank_dir_ = g_rank_dir_ # 全局目录
    res = rank_dir(rank_dir_, rank_count,rank_by)
    ranked_files = []
    rank_num = 0
    for line in res:
        # filename = '/Users/zxzx/projects/interview/cpp-interview/Algo_rank/47_0_位运算实现加法_61.md'
        filename = line[1]  # 文件名称
        score = line[0]
        relative = filename.split('/')[-1]
        relative = relative.split('.')[0] # 47_0_位运算实现加法_61
        parts = relative.split('_')
        file_origin_num = parts[-1]
        content_name = line[2].get('名称','')  # 名称, 如果这里多写了个逗号 , 那么content_name就变成了一个tuple,需要绕开
        new_name = '{}_{}_{}_{}.md'.format(rank_num, score, content_name, file_origin_num)
        full_new_name = os.path.join(rank_dir_, new_name)
        if(line[1] == full_new_name):
            print('{} 排名相同,跳过'.format(full_new_name))
            pass
        else:
            ranked_files.append(line[1])
            copyfile(filename,full_new_name)
        rank_num += 1

    for old_file in ranked_files:
        os.remove(old_file)


if __name__ == '__main__':
    g_weight = {
        '实用性': 10,
        '难度': 100,
        '兴趣': 30,
        '熟悉程度': -10,
        '滞后': -100,
        '练习次数': -50,
        '不完整程度': -10,
        '重要程度': 15,
        '代码难度': -25,
        '代码量': -10,
        '代表性': 40,
        '待办': 100,

    }

    g_rank_num_factor = [
        '实用性', '难度', '熟悉程度', '兴趣', '滞后', '练习次数',
        '不完整程度', '重要程度', '熟悉程度', '代码难度', '代表性'
    ]

    g_tag_weight = {
        '排序': 0,
        '查找': 0,
        '树': 0,
        'TODO': 0,
        '会':0,
        '不会': 1000,
        '不确定会': 0,
        '难': -10,
    }

    # rank_and_copy(100, rank_by='FILE_NUM')
    rank_and_copy(100, rank_by='SCORE')

    # insert_rank_factor_for_all()


