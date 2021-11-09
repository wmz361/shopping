from sqlalchemy import Column, Integer, ForeignKey
from myapp.models.base import  Base


class MyCollect(Base):
    """ 我的收藏 """

    __tablename__ = 'sp_myCollect'
    collectId=Column(Integer, primary_key=True)
    uid = Column(Integer,  ForeignKey('sp_user.userid'))  # 商品收藏人员
    spuId=Column(Integer,  ForeignKey('sp_spu.spuId'))  # 商品spuid
