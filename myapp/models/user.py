from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from werkzeug.security import generate_password_hash, check_password_hash

from myapp.libs.error_code import NotFound, AuthFailed
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

    @staticmethod
    def verify(username,password):
        user=User.query.filter_by(username=username).first()
        if not user:
            raise NotFound('user not fpund')
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid':user.userid}

    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)







