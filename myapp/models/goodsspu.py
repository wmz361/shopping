from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date,Float
from werkzeug.security import generate_password_hash

from myapp.models.base import  Base


class GoodsSpu(Base):

    __tablename__ = 'goodsspu'
    spuid=Column(Integer, primary_key=True)
    spuname = Column(String(24), nullable=False)  # spu名称
    skuid = Column(Integer)  # 所属skuID
    isDefult=Column(Integer, default=0)  # 是否是默认spu
    spudescribe = Column(String(256))  # 品牌描述
    stock=Column(Integer)  # 库存
    price=Column(Float)  # 价格
    spupicture=Column(LargeBinary)  # 图片