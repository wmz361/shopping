from wtforms.validators import Length, EqualTo, ValidationError, Regexp
from .base import DataRequired, BaseForm
from wtforms.fields import simple,html5
from ..models.user import User


class PhoneNumForm(BaseForm):
    phone_num=simple.StringField('手机号',validators=[DataRequired(),Regexp(r'1[34578]\d{9}', message='手机号格式错误')])

class ResetPasswordForm(BaseForm):
    password = simple.PasswordField(validators=[DataRequired(), Length(1, 100, message='密码长度至少需要在1个字符'),
                                                 EqualTo('password2', message='两次输入的密码不相同')])
    password2=simple.PasswordField(validators=[DataRequired(),Length(1,100)])

class LoginForm(BaseForm):
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
        if User.query.filter_by(phone_num=field.data).first():
            raise ValidationError('该手机号已经注册过！')

        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已存在')
















