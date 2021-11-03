from sqlalchemy import Column, Integer, String
from myapp.models.base import  Base


class Order(Base):
    """ 订单 """

    __tablename__ = 'order'
    orderId=Column(Integer, primary_key=True)
    spuId = Column(String(24), nullable=False)  # spuId
    spu_count=Column(Integer, nullable=False)  # spu的数量
    addressId=Column(Integer, nullable=False)  # 收货地址id
    payTypeId=Column(Integer, nullable=False)  # 支付方式id
    userId=Column(Integer, nullable=False)  # 用户id

