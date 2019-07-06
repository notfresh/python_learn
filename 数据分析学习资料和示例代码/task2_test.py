import json
import pandas as pd
import matplotlib.pyplot as plt


def study_log_stat():
    with open('user_study.json') as f:
        data = json.loads(f.read())
        user_data = pd.DataFrame(data=data, columns=['user_id', 'lab', 'course', 'minutes', 'created_at'])
    # 尽管可以选择多列, 但是根据user_id聚合之后, 只会显示minutes的汇总, 如果有别的字段,比如course和lab都是文字, pandas聪明的排除掉了这两个字段.
    res_df = user_data[['user_id', 'minutes']].groupby('user_id').sum()
    print(res_df.columns)
    print(res_df.index)
    print(type(res_df))
    # print(res_df.head(2))

    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.plot('user_id', 'study_minutes', data=res_df)
    # fig.show()

    # TODO
    # 这个图暂时还画不了, 有些API我不知道怎么去查,

study_log_stat()