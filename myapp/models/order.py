from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from myapp.models.base import  Base


class Order(Base):

    __tablename__ = 'order'
    orderId=Column(Integer, primary_key=True)
    spuId = Column(String(24), nullable=False)  # spuId
    spuCount=Column(Integer)  # spu的数量
    addressId=Column(Integer)  # 收货地址id
    payTypeId=Column(Integer)  # 支付方式id
    userId=Column(Integer)  # 用户id

