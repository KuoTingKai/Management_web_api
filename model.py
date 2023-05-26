from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, MetaData, Table, Date, UniqueConstraint
from datetime import datetime
from sqlalchemy.sql import exists    
from werkzeug.security import generate_password_hash

SQLALCHEMY_DATABASE_URL = "sqlite:///stock.db"

engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255))
    order_time = Column(Date,default=datetime.now)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

class Account(Base):
    __tablename__ = 'Account'
    id = Column(Integer, primary_key=True,autoincrement=True)
    account = Column(String(255),unique=True,nullable=False)
    password = Column(String(255),nullable=False)

    __table_args__ = (
        UniqueConstraint('account', name='unique_account'),
    )

    def __init__(self, account=None,password=None):
        self.account = account
        self.password = generate_password_hash(password)

class Inventory(Base):
    __tablename__ = 'Inventory'
    id = Column(Integer, primary_key=True,autoincrement=True)
    comsumed_name = Column(String(255))
    remaining = Column(Integer)

    def __init__(self, id=None, comsumed_name=None, remaining=None):
        self.id = id
        self.comsumed_name = comsumed_name
        self.remaining = remaining
        
class Machine(Base):
    __tablename__ = 'Machine'
    id = Column(Integer, primary_key=True,autoincrement=True)
    machine_name = Column(String(255))
    order_time = Column(Date,default=datetime.now)

    def __init__(self, id=None, name=None, order_time=None):
        self.id = id
        self.name = name
        self.order_time = order_time

class Sign_in(Base):
    __tablename__ = 'Sign_in'
    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(255))
    sign_in_time = Column(Date,default=datetime.now)

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

## 新增表格
# Session = sessionmaker(bind=engine)
# session = Session()

# metadata = MetaData()

# metadata.create_all(engine)
# Base.metadata.create_all(engine)
# session.commit()     #提交會話（事務） 
# session.rollback()     #回滾會話
# session.close()     #關閉會話