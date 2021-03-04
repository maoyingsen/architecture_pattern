from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date,
    ForeignKey, create_engine
)
from sqlalchemy.orm import mapper, sessionmaker

metadata = MetaData()

user = Table('user', metadata,
    Column('user_id', Integer, primary_key = True),
    Column('user_name', String(16), nullable = False),
    Column('email_address', String(60), key='email'),
    Column('password', String(20), nullable = False)
)

class User:
    def __init__(self, user_name, email_address, password):
        self.user_name = user_name
        self.email_address = email_address
        self.password = password

mapper(User, user)

engine = create_engine('sqlite:///D:\\tutorial\\Architecture_Patterns_with_Python\\coding\\cha2\\db_test.db')

metadata.create_all(engine)

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()

new_user = User(user_name = "daniel", email_address="123@163.com", password="123")
session.add(new_user)
session.commit()