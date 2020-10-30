#coding=utf-8
import sqlite3
conn = sqlite3.connect('testDB.db')
ERROR_TABLE_EXIST = 'table log already exists'

if __name__ == '__main__':
    cursor = conn.cursor()
    # cursor.execute('create table student2(id INTEGER PRIMARY KEY AUTOINCREMENT,name text,age int)')
    # integer 和 int 在sqlite中是不一样的....!
    # cursor.execute('create table student3(id int PRIMARY KEY AUTOINCREMENT,name text,age int)')
    try:
        cursor.execute("create table log(id INTEGER PRIMARY KEY AUTOINCREMENT, task_id integer(8), level varchar(8), msg text )")
    except Exception as e:
        if str(e) == ERROR_TABLE_EXIST:
            print("表已经有了")
        else:
            print(e)

