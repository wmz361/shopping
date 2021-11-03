from sqlalchemy import Column, Integer
from myapp.models.base import  Base


class Mycollect(Base):
    """ 我的收藏 """

    __tablename__ = 'mycollect'
    collectId=Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)  # 商品收藏人员
    spuId=Column(Integer, nullable=False)  # 商品spuid