from model import Inventory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class IC(Inventory):
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')
        self.table = Inventory.__table__

    def find(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        rows = []
        try:
            rows = session.query(self.table.c.comsumed_name).all()
        except Exception as e:
            print(e)
        finally:
            session.close()
            return rows

    def get(self,item):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            rows = session.query(self.table).filter_by(comsumed_name=item).first()
        except Exception as e:
            print(e)
        finally:
            session.close()
            return rows
    
    def update(self,option_value,update_data):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        rows = 0
        try:
            rows = session.query(self.table).filter_by(comsumed_name=option_value).update({Inventory.remaining: update_data})
            rows = self.get(option_value)
        except Exception as e:
            print(e)
        finally:
            session.commit()
            session.close()
            return rows