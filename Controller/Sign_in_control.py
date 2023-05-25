from model import Sign_in
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User


class SIC(Sign_in):
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')
        self.table = Sign_in.__table__

    def get(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        rows = []
        try:
            rows = session.query(self.table.c.sign_in_time).all()
        except Exception as e:
            print(e)
        finally:
            session.close()
            return rows