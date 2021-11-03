from sqlalchemy import Column, Integer, String
from myapp.models.base import  Base


class spuImage(Base):
    """ 存储spu图片的url """

    __tablename__ = 'spuImage'
    imageId=Column(Integer, primary_key=True)
    image_url=Column(String(128),nullable=False)  # 图片的url
    spuId = Column(Integer,nullable=False)  # 所属的spu