import enum

from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary, Date, Enum
from myapp.models.base import  Base


class tagEnum(enum.Enum):
    one = '家'
    two = '公司'
    three = '学校'

class Address(Base):

    __tablename__ = 'address'
    addressId=Column(Integer, primary_key=True)
    userId=Column(Integer)  # 创建人id
    provinceId=Column(Integer)  # 省ID
    cityId=Column(Integer)  # 市ID
    districtId=Column(Integer)  # 区ID
    name=Column(String)  # 收货人姓名
    tag=Column(Enum(tagEnum))  # 标签
    isDefult=Column(Integer,default=0)  # 是否为默认地址
    mobile=Column(String)  # 收货人手机号
    remark=Column(UnicodeText)  # 详细地址

