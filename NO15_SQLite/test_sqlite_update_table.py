#coding=utf-8
import sqlite3
conn = sqlite3.connect('testDB.db')

if __name__ == '__main__':
    cursor = conn.cursor()
    cursor.execute("insert into student2(name,age) values ('zhangsan',22)")

    cursor.execute("insert into student2(name,age) values ('lisi',24)")

    cursor.execute("insert into student2(name,age) values (?,?)", ("wangwu", 25))
    conn.commit() # - -插入完之后提交
    cursor.execute('select * from student2')
    print (cursor.fetchall())



