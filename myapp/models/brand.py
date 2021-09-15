from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from werkzeug.security import generate_password_hash

from myapp.models.base import  Base


class Brand(Base):

    __tablename__ = 'brand'
    brandid=Column(Integer, primary_key=True)
    brandname = Column(String(24), nullable=False)
    logo=Column(LargeBinary)
    declaration = Column(String(256))  # 品牌宣言
    brandstory=Column(UnicodeText)  # 品牌故事
    brandurl= Column(String(256))  # 品牌主页url
    phone_num = Column(String(18))


