from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from werkzeug.security import generate_password_hash

from myapp.models.base import  Base


class GoodsSku(Base):

    __tablename__ = 'goodssku'
    skuid=Column(Integer, primary_key=True)
    skuname = Column(String(24), nullable=False)
    skufatherid = Column(Integer, primary_key=True)
    bramdid = Column(Integer, primary_key=True)
