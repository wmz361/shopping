from wtforms import PasswordField, Form, StringField
from wtforms.validators import Length, EqualTo, ValidationError, Email
from .base import DataRequired
from ..models.user import User


class PhoneNumForm(Form):
    phone_num=StringField(validators=[DataRequired(),Length(11,message='您输入的手机号不符合规范！')])

class EmailForm(Form):
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64),Email(message='电子邮箱不符合规范')])

class ResetPasswordForm(Form):
    password = PasswordField(validators=[DataRequired(), Length(6, 100, message='密码长度至少需要在6个字符'),
                                                 EqualTo('password2', message='两次输入的密码不相同')])
    password2=PasswordField(validators=[DataRequired(),Length(6,100)])

class LoginForm(Form):
    username = StringField(validators=[DataRequired()])
    # def validate_username(self, field):
    #     """ 校验名称是否存在 """
    #     if not User.query.filter_by(username=field.data).first():
    #         raise ValidationError('用户名未注册')

class RegisterForm(LoginForm,ResetPasswordForm):

    def validate_username(self,field):
        """ 校验名称是否重复 """

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已存在')













