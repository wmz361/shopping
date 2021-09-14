from wtforms import PasswordField, Form, StringField
from wtforms.validators import Length, EqualTo
from .base import DataRequired

class RegisterForm(Form):
    username = StringField(
        label='用户名：',  # 标签
        validators=[  # 验证方式
            DataRequired()  # 不能为空
        ]
    )
    password1 = PasswordField('密 码：', validators=[
        DataRequired(), Length(6, 100, message='密码长度至少需要在6个字符'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField('确认密码', validators=[
        DataRequired(), Length(6, 100)])






