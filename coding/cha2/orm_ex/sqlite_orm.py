from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Test(Base):
    # 表的名字:
    __tablename__ = 'test'

    # 表的结构:
    id = Column(Integer, primary_key = True)
    sku = Column(String(20))
    price = Column(Integer)


# 初始化数据库连接:
engine = create_engine('sqlite:///D:\\tutorial\\Architecture_Patterns_with_Python\\coding\\cha2\\db_test.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
# 创建新User对象:
new_test = Test(sku = "cup", price = 10)
# 添加到session:
session.add(new_test)
# 提交即保存到数据库:
session.commit()