# 使用 *** 作为开始, **** 作为结束, 然后看一个文档是否合法


def load_file(file_name):
    res = None
    with open(file_name) as f:
        lines = f.readlines()
        # 确保最后一行换行
        if lines[-1][-1] != '\n':
            lines[-1] += '\n'
        res = [line[:-1] for line in lines]
    return res


def check(lines):
    cnt = 0
    line_num = 0
    i = 0
    for line in lines:
        i += 1
        if cnt == 0 and line == '***':
            cnt = 1
            line_num = i
        elif cnt == 1 and line == '***':
            line_num = i
            print('error line num is ', line_num )
            return False
        elif cnt == 1 and line == '****':
            cnt = 0
        elif cnt == 0 and line == '****':
            line_num = i
            print('error line num is ', line_num)
            return False
    if cnt > 0:
        print('error line num is ', line_num)
        return False
    return True


if __name__ == '__main__':
    lines = load_file('DA16-优秀代码收录-原创与少数整理.md')
    print(check(lines))


