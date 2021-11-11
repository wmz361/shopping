from flask_login import UserMixin
from sqlalchemy import Column, Integer,ForeignKey
from myapp.models.base import Base


class Account(UserMixin,Base):
    """ 用户账户表 """

    __tablename__ = 'sp_account'
    account_id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('sp_user.userid'))  # 创建人id
    balance=Column(Integer)  # 余额
    payType_id=Column(Integer, ForeignKey('sp_user.userid'))  # 支付方式id
