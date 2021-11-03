from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText,Date
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from myapp.libs.error_code import NotFound, AuthFailed
from myapp.models.base import Base, db


class User(UserMixin,Base):
    """ 用户信息表 """

    __tablename__ = 'user'
    userid = Column(Integer, primary_key=True)
    user_name = Column(String(24),unique=True, nullable=False)  # 用户名称
    phone_num = Column(String(18),nullable=False,unique=True)  # 手机号
    role=Column(SmallInteger,default=0)  # 用户角色（普通买家，店家，管理员）
    gender=Column(SmallInteger,default=0)  # 性别 0为女，1为男
    sign=Column(UnicodeText)  # 签名
    avatar=Column(String(128))  # 头像路径
    _password = Column('password', String(128),nullable=False)  # 密码
    birthday=Column(Date)  # 出生日期

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
            raise NotFound('userCenter not fpund')
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid':user.userid}

    def generate_token(self,expiration=600):
        s=Serializer(current_app.config['SECRET_KEY'],expiration)
        temp=s.dumps({'id':self.id}).decode('utf-8')
        return temp

    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)

    @staticmethod
    def reset_password(token,new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token.encode('utf-8'))
        except:
            return False
        uid=data.get('id')
        with db.auto_commit():
            user=User.query.get(uid)
            user.password=new_password
        return True








