from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from myapp.models.base import  Base


class Sort(Base):
    """ 商品种类 """

    __tablename__ = 'sp_sort'
    sortId=Column(Integer, primary_key=True)
    sort_name = Column(String(24), nullable=False)  # 分类名称
    sort_logo=Column(String(128), nullable=False) # 分类logo
    declaration = Column(String(256))  # 分类描述
    fatherSort=Column(Integer, default=0)  # 父级分类名称
    # 外键关联
    sku=relationship('Sku', backref='sku')