from sqlalchemy import Column, Integer, String, ForeignKey
from myapp.models.base import  Base


class SpuImage(Base):
    """ 存储spu图片的url """

    __tablename__ = 'sp_spuImage'
    imageId=Column(Integer, primary_key=True)
    image_url=Column(String(128),nullable=False)  # 图片的url
    spuId = Column(Integer,ForeignKey('sp_spu.spuId'))  # 所属的spu