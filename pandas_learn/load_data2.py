import pandas as pd

DIR = '/Users/zxzx/建模资料/2020年中国研究生数学建模竞赛赛题/2020年F题2020年F题--飞行器质心平衡供油策略优化/2020年F题--飞行器质心平衡供油策略优化'

EXCEL1 = "附件1-飞行器参数.xlsx"
EXCEL2 = "附件2-问题1数据.xlsx"

DENSITY = 850

def load_oil_init_data():
    #
    data=pd.read_excel("{}/{}".format(DIR, EXCEL1),sheet_name=[1])[1] # 第二个sheet页
    data.columns=['A','B','C','D','E','F','G', 'H']
    return data

OIL_INIT_DATA = load_oil_init_data()


def load_flying_data():
    #
    fly=pd.read_excel("{}/{}".format(DIR, EXCEL2),sheet_name=[1])[1]
    fly.columns=['A','B']
    return fly


def load_oil_current_data():
    """
    求出供油曲线
    :return:
    """
    data = pd.read_excel("{}/{}".format(DIR, EXCEL2), sheet_name=[0])[0]  # 第二个sheet页
    data.columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


    # 实际供油
    frame2 = data.copy()
    lenth = len(data['A'])


    for i in range(1, lenth):
        for j in data.columns[1:]: # 从第二项开始累加
            frame2[j][i] = frame2[j][i] + frame2[j][i - 1]


    frame3 = frame2.copy()
    frame3['B'][0] = OIL_INIT_DATA['H'][0]
    # BCDEF
    frame3['C'][0] = OIL_INIT_DATA['H'][1]
    frame3['D'][0] = OIL_INIT_DATA['H'][2]
    frame3['E'][0] = OIL_INIT_DATA['H'][3]
    frame3['F'][0] = OIL_INIT_DATA['H'][4] + frame2['G'][i] / DENSITY
    # G
    frame3['G'][i] = -frame2['G'][i] / DENSITY + OIL_INIT_DATA['H'][5]

    for i in range(1, lenth):
        frame3['B'][i] = -frame2['B'][i]/DENSITY + OIL_INIT_DATA['H'][0]
        # BCDEF
        frame3['C'][i] = -frame2['C'][i]/DENSITY + OIL_INIT_DATA['H'][1] + frame2['B'][i]/DENSITY
        frame3['D'][i] = -frame2['D'][i]/DENSITY + OIL_INIT_DATA['H'][2]
        frame3['E'][i] = -frame2['E'][i]/DENSITY + OIL_INIT_DATA['H'][3]
        frame3['F'][i] = -frame2['F'][i]/DENSITY + OIL_INIT_DATA['H'][4] + frame2['G'][i]/DENSITY
        # G
        frame3['G'][i] = -frame2['G'][i]/DENSITY + OIL_INIT_DATA['H'][5]
    #
    #
    return frame3




if __name__ == '__main__':

    #FLY = load_flying_data()
    # SUPPLY_DATA = load_oil_current_data()
    print(OIL_INIT_DATA['H'][0])
    print(OIL_INIT_DATA['H'][2])
    print( chr(ord('A') + 1))
    # CURRENT_OIL_DATA = load_oil_current_data()
    # print(CURRENT_OIL_DATA)
    print(OIL_INIT_DATA['B'][0], OIL_INIT_DATA['C'][0], OIL_INIT_DATA['D'][0])



