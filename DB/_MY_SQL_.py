#pip install mysql-connector==2.1.4
import mysql.connector
from contextlib import contextmanager
#与sqlite不同。mysql的占位符是'%s'，后面的赋值语句为列表

@contextmanager
def cnn_mysql():
    cnn = mysql.connector.connect(user='root', password='password')
    cursor = cnn.cursor()
    yield cursor
    cursor.close()
    cnn.commit()
    cnn.close()

id = 1
name = 'Write'
with cnn_mysql() as cursor:
    cursor.execute('CREATE DATABASE IF NOT EXISTS python_test')
    cursor.execute('USE python_test')
    cursor.execute('CREATE TABLE IF NOT EXISTS user2(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20) )')
    cursor.execute('INSERT INTO user2 (name) values (%s)', [name])
    cursor.execute('SELECT * from user2')
    print(cursor.fetchall())
