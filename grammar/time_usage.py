#coding=utf-8
# 1. 如何算出100天后是哪月哪天？
import datetime as dt
print(dt.datetime.now())
print(dt.datetime.now()+dt.timedelta(days=100))