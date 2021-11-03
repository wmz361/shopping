import enum

from sqlalchemy import Column, Integer, String, UnicodeText,  Enum
from myapp.models.base import  Base


class tagEnum(enum.Enum):
    one = '家'
    two = '公司'
    three = '学校'

class Address(Base):
    """ 收货地址 """

    __tablename__ = 'address'
    addressId=Column(Integer, primary_key=True)
    userId=Column(Integer, nullable=False)  # 创建人id
    provinceId=Column(Integer, nullable=False)  # 省ID
    cityId=Column(Integer, nullable=False)  # 市ID
    districtId=Column(Integer, nullable=False)  # 区ID
    name=Column(String(24), nullable=False)  # 收货人姓名
    tag=Column(Enum(tagEnum))  # 标签
    isDefault=Column(Integer,default=0)  # 是否为默认地址
    mobile=Column(String(24), nullable=False)  # 收货人手机号
    remark=Column(UnicodeText)  # 详细地址

