from sqlalchemy import Column, Integer, String, SmallInteger, Boolean, Float, UnicodeText, LargeBinary
from werkzeug.security import generate_password_hash

from myapp.models.base import  Base


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(24), nullable=False)
    phone_number = Column(String(18))
    confirmed = Column(Boolean, default=False)
    role=Column(SmallInteger,default=0)
    gender=Column(SmallInteger,default=0)
    sign=Column(UnicodeText)
    Avatar=Column(LargeBinary)
    _password = Column('password', String(128))

    @property
    def password(self):
        return self._password


    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)






