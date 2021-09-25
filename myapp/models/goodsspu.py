from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date,Float
from werkzeug.security import generate_password_hash

from myapp.models.base import  Base


class GoodsSpu(Base):

    __tablename__ = 'goodsspu'
    spuid=Column(Integer, primary_key=True)
    spuname = Column(String(24), nullable=False)
    skuid = Column(Integer)
    spudescribe = Column(String(256))  # 品牌描述
    stock=Column(Integer)  # 库存
    price=Column(Float)
    spupicture=Column(LargeBinary)  # 图片
    uid = Column(Integer)