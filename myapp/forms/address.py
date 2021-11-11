from html.entities import html5
from wtforms import simple
from wtforms.validators import Regexp
from .base import DataRequired, BaseForm


class addressForm(BaseForm):

    userName = simple.StringField(validators=[DataRequired()])
    provinceId = simple.StringField(validators=[DataRequired()])  # 省ID
    cityId = simple.StringField(validators=[DataRequired()])  # 市ID
    districtId = simple.StringField(validators=[DataRequired()])  # 区ID
    name = simple.StringField(validators=[DataRequired()])  # 收货人姓名
    tag = html5.IntegerField()  # 标签
    isDefault = simple.BooleanField() # 是否为默认地址
    mobile = simple.StringField(validators=[DataRequired(),Regexp(r'1[34578]\d{9}', message='手机号格式错误')])  # 收货人手机号
    remark = simple.TextAreaField()  # 详细地址

