import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def cal_box_angle(a, c):
    d = math.sqrt(a * a + c * c)
    angle_360 = math.asin(a/d) * 360 / (math.pi * 2)
    return angle_360


from load_data2 import OIL_INIT_DATA

OIL_BOX = [
    [1,1,1],
    [1,1,1],
    [1,1,1],
    [1,1,1],
    [1,1,1],
    [1,1,1],
]

for item in OIL_BOX:
    item[0] = OIL_INIT_DATA
    item[1] =
    item[2] =
    item.append(cal_box_angle(item[0],item[1])) # 角度
    item.append(item[0], item[1], item[2]) # 体积


def load_data():
    DIR='/Users/zxzx/建模资料/2020年中国研究生数学建模竞赛赛题/2020年F题2020年F题--飞行器质心平衡供油策略优化/2020年F题--飞行器质心平衡供油策略优化'
    EXCEL2="附件2-问题1数据.xlsx"
    #
    fly=pd.read_excel("{}/{}".format(DIR, EXCEL2),sheet_name=[1])[1]
    fly.columns=['A','B']
    return fly


def i_critical_value(i, box_angle, fly_angle, a, b, c):
    """

    :param i: 第i个供油箱
    :param box_angle:  邮箱长宽比
    :param fly_angle:
    :param a:
    :param b:
    :param c:
    :return:
    """
    if fly_angle < box_angle:
        vi = a * (a * math.tan(fly_angle)) * 0.5 * b
    else:
        vi = c * (c / math.tan(fly_angle)) * 0.5 * b

    return vi

def case_flow(i, second):
    """

    :param i: 第几个邮箱
    :param second: 第几秒
    :return:
    """
    fly = load_data()
    oil_amount = pd.DataFrame()['B'][second] # 不同时间的剩余油量
    vi_critical = i_critical_value(i, OIL_BOX[i][3], fly['B'][second], OIL_BOX[i][0],OIL_BOX[i][1],OIL_BOX[i][2])

    fly_angle = fly['B'][second]
    box_angle = OIL_BOX[i][3] # 邮箱的一边比上对角边

    if fly_angle < box_angle:
        # OIL_BOX[i][4] 邮箱的体积
        if oil_amount > OIL_BOX[i][4] -  vi_critical:
            pass  #case 1
        elif vi_critical <  oil_amount < OIL_BOX[i][4] - vi_critical:
            pass # case2
        elif oil_amount <= vi_critical:
            pass # case5

    elif fly_angle >= box_angle:
        # OIL_BOX[i][4] 邮箱的体积
        if oil_amount > vi_critical:
            pass  #case 1
        elif vi_critical <  oil_amount < OIL_BOX[i][4] - vi_critical:
            pass # case3
        elif oil_amount <= vi_critical:
            pass # case4



def case1():
    Q1 = []


