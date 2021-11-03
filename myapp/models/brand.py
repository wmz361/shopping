from sqlalchemy import Column, Integer, String, UnicodeText
from myapp.models.base import  Base


class Brand(Base):
    """ 品牌 """

    __tablename__ = 'brand'
    brandId=Column(Integer, primary_key=True)
    brand_name = Column(String(24), nullable=False)  # 品牌名称
    logo=Column(String(128),nullable=False)  # 品牌logo
    declaration = Column(String(256))  # 品牌宣言
    brand_story=Column(UnicodeText)  # 品牌故事
    brand_url= Column(String(256))  # 品牌主页url
    phone_num = Column(String(18))  # 品牌联系方式
    uid = Column(Integer, nullable=False)  # 品牌主理人Id



