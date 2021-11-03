from sqlalchemy import Column, Integer, String, Float

from myapp.models.base import  Base


class GoodsSpu(Base):
    """ 商品spu """

    __tablename__ = 'goodsspu'
    spuId=Column(Integer, primary_key=True)
    spu_name = Column(String(24), nullable=False)  # spu名称
    skuId = Column(Integer, nullable=False)  # 所属skuID
    isDefault=Column(Integer, default=0)  # 是否是默认spu
    spu_describe = Column(String(256))  # 品牌描述
    stock=Column(Integer, nullable=False)  # 库存
    price=Column(Float, nullable=False)  # 价格
    index_image_url=Column(String(128), nullable=False)  # 主图的url