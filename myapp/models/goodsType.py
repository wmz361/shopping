from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from myapp.models.base import  Base


class Sort(Base):

    __tablename__ = 'sort'
    sortId=Column(Integer, primary_key=True)
    sortName = Column(String(24), nullable=False)  # 分类名称
    sortLogo=Column(LargeBinary)  # 分类logo
    declaration = Column(String(256))  # 分类描述
    fatherSort=Column(Integer, default=0)  # 父级分类名称