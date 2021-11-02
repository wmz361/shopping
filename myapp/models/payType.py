from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from myapp.models.base import  Base


class payType(Base):

    __tablename__ = 'payType'
    payTypeId=Column(Integer, primary_key=True)
    payTypeName=Column(String)  # 支付方式name
    payTypeLogo = Column(LargeBinary)  # 支付方式图标
