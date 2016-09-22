from sqlalchemy import Column, table, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    fullname = Column(String(40))
    email = Column(String(40), unique=True)
    password = Column(String(32))

    def __repr__(self):
        return "<User(full_name='%s', email='ed@gmail.com password='%s')>" % (
            self.fullname, self.email, self.password)

# Imports

from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine


# Setting Up a Session
Session = sessionmaker(bind=engine)
session = Session()


# Adding a User
ed_user = User(id=0, fullname='ed', email='ed@gmail.com', password='IamEd')
session.add(ed_user)

print("Reach", ed_user.fullname, "at", ed_user.email)


