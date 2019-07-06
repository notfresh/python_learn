import json
import pandas as pd

with open('user_study.json') as f:
    data = json.loads(f.read())
print(type(data)) # 一个列表
print(data[0]) # 一个字典
print(type(data[0])) # 字典

# user_data = pd.DataFrame(data=data, columns=['user_id', 'lab', 'course', 'minutes', 'created_at'])
# print(user_data)
# print(user_data.iloc[0])
# print(user_data.iloc[1])
# print(user_data[user_data['user_id']==199071])
# print(user_data[['user_id','minutes']][user_data['user_id']==199071]).group_by('course').sum()
# res = user_data[user_data['user_id']==199071][['user_id','minutes','course']].groupby('course').sum()
# print(type(res))
# print(type(user_data[user_data['user_id']==199071][['user_id','minutes','course']].groupby('course').sum()))


def study_log(filename, user_id):
    with open(filename) as f:
        data = json.loads(f.read())
        user_data = pd.DataFrame(data=data, columns=['user_id', 'lab', 'course', 'minutes', 'created_at'])
    print(user_data[user_data['user_id'] == user_id][['user_id', 'minutes', 'course']].groupby('course').sum())

study_log('user_study.json', 199071)
study_log('user_study.json', 1)