from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists, insert, delete, update

class CURD_control:
    def __init__(self):
        engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/yixin')
        # session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.engine = engine
        self.table = 'Machine'
    
    def find(self, findname=None):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            # if session.query(exists().where(self.table.c.name == findname)).scalar():
            row = session.query(self.table).filter_by(name = findname)  
        except:
            print('Maybe there is no such name in this database.')
        finally:
            session.close()
            return row

        
    def add(self, name):
        Session = sessionmaker(bind=self.engine)
        session = Session()

        try:
            insert(self.table).values(name=name)
            session.commit()
        except:
            print('This name is already exist. Please change the other name.')
        finally:
            session.close()
            print('The name has add to table.')

        # if session.query(exists().where(self.table.c.name == machine_name)).scalar():
        #     return 'This name is already exist. Please change the other name.'
        # stmt = insert(self.table).values(name=machine_name)
        # return 'The name has add to table.'

    def delete(self, name):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        try:
            delete(self.table).values(name=name)
            session.commit()
        except:
            print('The name does not exist in this database')
        finally:
            session.close()
 
        

class machine_controller(CURD_control):
        def __init__(self):
            super().__init__()
            self.table = 'Machine'
    
class Inventory_controller(CURD_control):
        def __init__(self):
            super().__init__()
            self.table = 'Inventory'
        
        def update(self,name,value):
            Session = sessionmaker(bind=self.engine)
            session = Session()
            try:
                update(self.table).where(self.table.c.name == name).value(remaining=value)
                # session.query(self.table).filter_by(name=name).update({})
                session.commit()
            except:
                print('The name does not exist in this database')
            finally:
                session.close()