from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, MetaData, Table, Date, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.sql import exists    

SQLALCHEMY_DATABASE_URL = "sqlite:///stock.db"

engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

class Inventory(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(255))
    comsumed_name = Column(String(255))
    remaining = Column(Integer)

    def __init__(self, id=None, name=None, comsumed_name=None, remaining=None):
        self.id = id
        self.name = name
        self.comsumed_name = comsumed_name
        self.remaining = remaining

class Machine(Base):
    __tablename__ = 'Machine'
    id = Column(Integer, primary_key=True)
    machine_name = Column(String(255))
    order_time = Column(Date,default=datetime.now)


    def __init__(self, id=None, name=None, order_time=None):
        self.id = id
        self.name = name
        self.order_time = order_time

def check(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    check_e = False
    check_p = False
    
    if session.query(exists().where(table.c.Email == email)).scalar():
        check_e = True
    else:
        check_e = False
        return check_e, check_p

    if session.query(table).filter_by(Email=email,Password=password).first():
        check_p = True
    else:
        check_p = False

    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話

    return check_e, check_p

def changePW(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    check_e = False
    check_p = False

    ins = table.update().values(Password=password).where(email == table.c.Email)
    conn = engine.connect()
    conn.execute(ins)

    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話
    return

def insert_value(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = table.insert().values(Email=email,Password=password)
    conn = engine.connect()
    conn.execute(ins)
    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話

# 創建表格
Base.metadata.create_all(engine)
Session.close()







# def add(table, id, name):
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     table.id = id
#     table.name = name
#     session.commit()
#     session.rollback()     #回滾會話
#     session.close()     #關閉會話




# Session = sessionmaker(bind=engine)
# session = Session()

# metadata = MetaData()

# metadata.create_all(engine)
# Base.metadata.create_all(engine)
# session.commit()     #提交會話（事務） 
# session.rollback()     #回滾會話
# session.close()     #關閉會話




# email = 'cov85741@gmail.com'
# password = 'adsfe'
# 新增 > 查詢 > 
# insert_value(user,'cov85741@gmail.com','adsfes')
# print(check(user,email,password))
