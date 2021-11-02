from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from myapp.models.base import  Base


class Brand(Base):

    __tablename__ = 'brand'
    brandid=Column(Integer, primary_key=True)
    brandname = Column(String(24), nullable=False)  # 品牌名称
    logo=Column(LargeBinary)  # 品牌logo
    declaration = Column(String(256))  # 品牌宣言
    brandstory=Column(UnicodeText)  # 品牌故事
    brandurl= Column(String(256))  # 品牌主页url
    phone_num = Column(String(18))  # 品牌联系方式
    uid = Column(Integer)  # 品牌主理人Id



