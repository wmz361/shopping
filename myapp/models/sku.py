from sqlalchemy import Column, Integer, String, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship

from myapp.models.base import  Base


class Sku(Base):
    """ 商品sku """

    __tablename__ = 'sp_sku'
    skuId=Column(Integer, primary_key=True)
    sku_name = Column(String(24), nullable=False)  # 商品名称
    brandId = Column(Integer, ForeignKey('sp_brand.brandId'))  # 所属品牌ID
    sort_id=Column(Integer, ForeignKey('sp_sort.sortId'))  # 所属分类ID
    introduction=Column(String(200), nullable=False)  # 商品简介
    uid = Column(Integer, ForeignKey('sp_user.userid'))  # 商品发布人员
    describe=Column(UnicodeText)  # 商品描述
    sales=Column(Integer, default=0)  # 销量
    index_image_url=Column(Integer, nullable=False)  # 主图的url
    # 外键关联
    spu = relationship('Spu', backref='spu')


