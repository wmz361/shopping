from sqlalchemy import Column, Integer, String, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship

from myapp.models.base import  Base


class Brand(Base):
    """ 品牌 """

    __tablename__ = 'sp_brand'
    brandId=Column(Integer, primary_key=True)
    brand_name = Column(String(24), nullable=False)  # 品牌名称
    logo=Column(String(128),nullable=False)  # 品牌logo
    declaration = Column(String(256))  # 品牌宣言
    brand_story=Column(UnicodeText)  # 品牌故事
    brand_url= Column(String(256))  # 品牌主页url
    phone_num = Column(String(18))  # 品牌联系方式
    uid = Column(Integer, ForeignKey('sp_user.userid'))  # 品牌主理人Id
    # 外键关联
    sku = relationship('Sku', backref='brand')



