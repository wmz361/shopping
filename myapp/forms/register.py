from wtforms import PasswordField, Form, StringField
from wtforms.validators import Length, EqualTo, ValidationError
from .base import DataRequired
from ..models.user import User


class RegisterForm(Form):
    username = StringField(
        label='用户名：',  # 标签
        validators=[  # 验证方式
            DataRequired()  # 不能为空
        ]
    )
    password = PasswordField('密 码：', validators=[
        DataRequired(), Length(6, 100, message='密码长度至少需要在6个字符'),
        EqualTo('password2', message='两次输入的密码不相同')])

    def validate_username(self,field):
        """ 校验名称是否重复 """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')










