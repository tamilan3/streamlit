from sqlalchemy import Column, Integer, String,ForeignKey,DateTime, Select
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    email = Column(String)

    def __init__(self,id,name,email):
        self.id=id
        self.name=name
        self.email=email

    def __str__(self):
        self.email      
   
    
class cheaker(Base):
    __tablename__ = 'cheaker'

    id=Column(Integer,primary_key=True,autoincrement=True)
    user_id=Column(Integer,ForeignKey(User.id))
    reason=Column(String,nullable=False)
    start=Column(DateTime(timezone=True),nullable=True)
    end=Column(DateTime(timezone=True),nullable=True)

    def __init__(self,user_id,reason,id=None,start=None,end=None):
        self.id=id
        self.user_id=user_id
        self.start=start
        self.reason=reason
        self.end=end

    def __str__(self):
        self.reason

def create_connection():
    engine = create_engine('postgresql+psycopg2://postgres:Tamilan123*@localhost:5432/postgres')
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    print("session created")
    return Session()

create_connection()