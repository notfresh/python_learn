import json
import pandas as pd
import matplotlib.pyplot as plt


def study_log_stat():
    with open('apple.csv') as f:
        data = pd.read_csv(f)
    print(data.head(5))
    data[['Volume']].groupby('')
    # TODO
    # 这个图暂时还画不了, 有些API我不知道怎么去查

study_log_stat()
