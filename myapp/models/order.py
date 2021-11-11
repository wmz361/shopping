from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from myapp.models.base import Base, db


class Order(Base):
    """ 订单 """

    __tablename__ = 'sp_order'
    orderId=Column(Integer, primary_key=True)
    spuId = Column(Integer, ForeignKey('sp_spu.spuId'))  # spuId
    spu_count=Column(Integer, nullable=False)  # spu的数量
    addressId=Column(Integer, ForeignKey('sp_address.addressId'))  # 收货地址id
    payTypeId=Column(Integer, ForeignKey('sp_payType.payTypeId'))  # 支付方式id
    userId=Column(Integer, ForeignKey('sp_user.userid'))  # 用户id
    # 外键关联
    comment = relationship('Comment', backref='order')

    @staticmethod
    def reset_status(orderId,newStatus):
        ''' 重置订单状态 '''
        with db.auto_commit():
            order=Order.query.get(orderId)
            order.status=newStatus
            return True



