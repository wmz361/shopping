from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from myapp.models.base import  Base


class payType(Base):
    """ 支付方式 """

    __tablename__ = 'sp_payType'
    payTypeId=Column(Integer, primary_key=True)
    payType_name=Column(String(64),nullable=False)  # 支付方式name
    payType_logo = Column(String(128),nullable=False)  # 支付方式图标
    # 外键关联
    order = relationship('Order', backref='order')
