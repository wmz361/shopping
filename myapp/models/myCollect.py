from sqlalchemy import Column, Integer, String, UnicodeText, LargeBinary
from myapp.models.base import  Base


class Mycollect(Base):

    __tablename__ = 'mycollect'
    collectid=Column(Integer, primary_key=True)
    uid = Column(Integer)  # 商品收藏人员
    spuid=Column(Integer)  # 商品spuid