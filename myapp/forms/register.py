from wtforms import PasswordField, Form, StringField,IntegerField,DateField
from wtforms.validators import Length, EqualTo, ValidationError, Email
from .base import DataRequired
from wtforms.fields import simple,html5
from ..models.user import User


class PhoneNumForm(Form):
    phone_num=simple.StringField(validators=[DataRequired(),Length(1,64,message='您输入的手机号不符合规范！')])

class EmailForm(Form):
    email = simple.StringField('邮箱', validators=[DataRequired(), Length(1, 64),Email(message='电子邮箱不符合规范')])

class ResetPasswordForm(Form):
    password = simple.PasswordField(validators=[DataRequired(), Length(1, 100, message='密码长度至少需要在1个字符'),
                                                 EqualTo('password2', message='两次输入的密码不相同')])
    password2=simple.PasswordField(validators=[DataRequired(),Length(1,100)])

class LoginForm(Form):
    username = simple.StringField(validators=[DataRequired()])
    password = simple.StringField()
    def validate_username(self, field):
        """ 校验名称是否存在 """
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名未注册')

class RegisterForm(LoginForm,ResetPasswordForm,PhoneNumForm):
    gender=html5.IntegerField()
    birthday=html5.DateField()
    def validate_username(self,field):
        """ 校验名称是否重复 """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')
















