# Imports

from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine


# Setting Up a Session
Session = sessionmaker(bind=engine)
session = Session()


# Adding a User
ed_user = User(id=0, full_name='ed', email='ed@gmail.com', password='IamEd')
session.add(ed_user)


our_user = session.query(User).filter_by(fullname='ed').first()
print(our_user)



