from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from werkzeug.security import generate_password_hash

from myapp.models.base import  Base


class User(Base):

    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    username = Column(String(24), nullable=False)
    phone_num = Column(String(18))
    role=Column(SmallInteger,default=0)
    gender=Column(SmallInteger,default=0)
    sign=Column(UnicodeText)
    avatar=Column(LargeBinary)
    _password = Column('password', String(128))
    birthday=Column(Date)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,raw):
        self._password=generate_password_hash(raw)






