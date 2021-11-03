from sqlalchemy import Column, Integer, String, UnicodeText
from myapp.models.base import  Base


class GoodsSku(Base):
    """ 商品sku """

    __tablename__ = 'goodssku'
    skuId=Column(Integer, primary_key=True)
    sku_name = Column(String(24), nullable=False)  # 商品名称
    brandId = Column(Integer, nullable=False)  # 所属品牌ID
    sortId=Column(Integer, nullable=False)  # 所属分类ID
    introduction=Column(String(200), nullable=False)  # 商品简介
    uid = Column(Integer, nullable=False)  # 商品发布人员
    describe=Column(UnicodeText)  # 商品描述
    sales=Column(Integer, default=0)  # 销量
    index_image_url=Column(Integer, nullable=False)  # 主图的url


