import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rc("font",family='Adobe Heiti Std')


def load_data():
    DIR='/Users/zxzx/建模资料/2020年中国研究生数学建模竞赛赛题/2020年F题2020年F题--飞行器质心平衡供油策略优化/2020年F题--飞行器质心平衡供油策略优化'
    EXCEL2="附件2-问题1数据.xlsx"
    #
    fly=pd.read_excel("{}/{}".format(DIR, EXCEL2),sheet_name=[1])[1]
    fly.columns=['A','B']
    return fly


FLY = load_data()

# plt.title('附件2：飞行器随时间俯仰角变化数据')
# plt.xlabel('时间(s)')
# plt.ylabel('飞行器俯仰角(度)')
# plt.plot(FLY['A'],FLY['B'], FLY['A'], FLY['A']*0)
# plt.show()

EADGE_ANGLES = [11.3102]
FLAYING_ANGLES = FLY['B']
INDEX = FLY['A']
INDEX_LEN = len(INDEX)

def find(ls, value):
    res = []
    res2 = []
    length = len(ls)
    for i in range(length-1):
        if ls[i] < value and ls[i + 1] >= value:
            res.append(i)
            continue
        if ls[i] >= value and ls[i + 1] < value:
            res2.append(i)
            continue
    return res,res2


def single_find(ls, value):
    res = []
    length = len(ls)
    for i in range(length-1):
        if ls[i] < value and ls[i + 1] >= value:
            res.append(i)
            continue
        if ls[i] >= value and ls[i + 1] < value:
            res.append(i)
            continue
    return res


def find_batch(ls, values):
    res = []
    for value in values:
        res.extend(single_find(ls, value))
    return res

# np.arange()

if __name__ == '__main__':
    # ls = [0, 1, 2, 3, 4, 5, 6, 8, 10, 5]
    # value = [7]
    value = EADGE_ANGLES
    ls = FLAYING_ANGLES
    res = find_batch(ls, value)
    y = pd.Series([[res[0]] * INDEX_LEN ])

    # print(res)
    print([0]*10)


