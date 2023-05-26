from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Account
from werkzeug.security import generate_password_hash


class SUC(Account):
    def __init__(self):
        self.engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')
        self.table = Account.__table__

    def get(self, username):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            rows = session.query(self.table.c.account == username).first()
            # print(rows)
        except Exception as e:
            print(e)
        finally:
            session.close()
            return rows
        

    def add(self, username, userpassword):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            newuser = Account(username,generate_password_hash(userpassword))
            session.add(newuser)
            session.commit()
            session.close()
        except Exception as e:
            print(e)
        # finally:
            
            # return rows