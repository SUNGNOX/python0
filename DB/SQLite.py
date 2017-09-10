# -*- coding: utf-8 -*-
#在Python中操作数据库时，要先导入数据库对应的驱动，然后，通过Connection对象和Cursor对象操作数据。
# 要确保打开的Connection对象和Cursor对象都正确地被关闭，否则，资源就会泄露。
# 如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象呢？请回忆try:...except:...finally:...的用法。
import os, sqlite3
from contextlib import contextmanager

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

#定义链接和关闭sqlite的上下文管理器
@contextmanager
def sqlite_db():
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        yield cursor
    finally:
        cursor.close()
        conn.commit()
        conn.close()

# 初始数据:
with sqlite_db() as cursor:
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    cursor.execute('SELECT * from user')#使用Cursor对象执行select语句时，通过featchall()可以拿到结果集
    value = cursor.fetchall()
    print(value)

def get_score_in(low, high):
    with sqlite_db() as cursor:
        cursor.execute('SELECT name from user where score>=? and score<=?', (low, high))
        value = cursor.fetchall()
        S = map(lambda x:x[0], value)
        # for name in value:
        #     S.append(name[0])
    return list(S)

print('----------------------------------------')
S = get_score_in(60, 100)
print(S)
