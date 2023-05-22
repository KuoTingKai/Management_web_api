from sqlalchemy import create_engine, engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model import Inventory







Base = declarative_base()

# class Inventory(Base):
#     __tablename__ = 'Inventory'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))


class read_Inventory_name:
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')
        # session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        # self.engine = engine
        self.table = Inventory.__table__

    def find(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        rows = []
        try:
            # row = session.query(self.table).filter_by(name = 'comsumed_name').all()
            rows = session.query(self.table).all()
        except Exception as e:
            print(e)
            print('Maybe there is no such name in this database.')
        finally:
            session.close()
            return rows
    
row = read_Inventory_name().find()
print(row)