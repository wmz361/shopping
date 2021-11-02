from sqlalchemy import Column, Integer, String, UnicodeText, LargeBinary

from myapp.models.base import  Base


class GoodsSku(Base):

    __tablename__ = 'goodssku'
    skuid=Column(Integer, primary_key=True)
    skuname = Column(String(24), nullable=False)  # 商品名称
    brandid = Column(Integer)  # 所属品牌ID
    sortId=Column(Integer)  # 所属分类ID
    introduction=Column(String(200))  # 商品简介
    uid = Column(Integer)  # 商品发布人员
    describe=Column(UnicodeText)  # 商品描述
    picture=Column(LargeBinary)  # 商品图片
    sales=Column(Integer)  # 销量


