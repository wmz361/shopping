from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from myapp.models.base import  Base


class Spu(Base):
    """ 商品spu """

    __tablename__ = 'sp_spu'
    spuId=Column(Integer, primary_key=True)
    userId=Column(Integer,ForeignKey('sp_user.userid'))  # spu所属用户
    spu_name = Column(String(24), nullable=False)  # spu名称
    skuId = Column(Integer, ForeignKey('sp_sku.skuId'))  # 所属skuID
    isDefault=Column(Integer, default=0)  # 是否是默认spu
    spu_describe = Column(String(256))  # 品牌描述
    stock=Column(Integer, nullable=False)  # 库存
    price=Column(Float, nullable=False)  # 价格
    index_image_url=Column(String(128), nullable=False)  # 主图的url
    # 外键关联
    myCollect=relationship('MyCollect',backref='myCollect')
    order = relationship('Order', backref='order')
    spuImage=relationship('SpuImage', backref='spuImage')