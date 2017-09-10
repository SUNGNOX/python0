from sqlalchemy import create_engine, Column
from sqlalchemy.types import *
from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/python_test', echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()
ret=session.execute('desc user2')
print(ret)
print(ret.fetchall())
print(ret.first())


from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()

class User(BASE):
    __tablename__ = 'user2'
    id = Column(VARCHAR(20), primary_key=True)
    name = Column(VARCHAR(20), nullable=False)

users = User(id='13', name='Bob')
session.add(users)

session.commit()
session.close()
###############################

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
users = session.query(User).filter(User.id=='6').all()
# 打印类型和对象的name属性:
print('type:', type(users))
print('name:', users[0].name)
# 关闭Session:
session.close()