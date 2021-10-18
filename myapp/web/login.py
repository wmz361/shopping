# coding=utf-8
from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user
from myapp.forms.register import RegisterForm, LoginForm, PhoneNumForm, EmailForm, ResetPasswordForm
from myapp.models.base import db
from myapp.models.user import User

loginBP = Blueprint("loginBP",__name__)
@loginBP.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST' :
        registerForm = RegisterForm(request.form)
        if registerForm.validate():
            with db.auto_commit():
                user = User()
                user.set_attrs(registerForm.data)
                db.session.add(user)
            flash('注册成功，跳转至首页！')
            # return redirect(url_for('indexBP.index'))
            return redirect(url_for('indexBP.indexLogin',uname=registerForm.data['username']))
        else:
            flash('数据验证失败！')
    return render_template('login/register.html')

@loginBP.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        loginForm = LoginForm(request.form)
        if loginForm.validate():
            user = User.query.filter(User.username==loginForm['username']).first()
            if user and user.check_password(loginForm.password.data):
                # 可以写入用户信息
                login_user(user,remember=True)
                next=request.args.get('next')  # 获取到url中next参数的值
                if not next or not next.startswith('/'):
                    next=url_for('webBP.indexLogin',uname=loginForm.username.data)
                flash('登录成功！')
                return redirect(next)
            else:
                flash('账号不存在或者密码错误！')
    return render_template('login/login.html')

@loginBP.route('/reset/password', methods=['GET','POST'])
def forget_password_request():
    if  'phone_num' in request.form.keys():
        form = PhoneNumForm(request.form)
        if request.method=='POST' and form.validate():
            account_phoneNum=form.phone_num.data
            user=User.query.filter_by(phone_num=account_phoneNum).first_or_404()
            redirect(url_for('web.login'))
    elif 'email' in request.form.keys():
        form = EmailForm(request.form)
        if request.method == 'POST' and form.validate():
            account_email = form.email.data
            user = User.query.filter_by(phone_num=account_email).first_or_404()
            from myapp.libs.email import send_email
            send_email(form.email.data,'重置你的密码','email/reset_password_request.html',user=user,token=user.generate_token())
            flash('验证邮件已发送至您的邮箱，请注意查收！')
            return redirect(url_for('web.login'))
    return render_template('email/reset_password_request.html',form=form)

@loginBP.route('/reset/password/<token>', methods=['GET','POST'])
def reset_password(token):
    form=ResetPasswordForm(request.form)
    if request.method=='POST' and form.validate():
        success=User.reset_password(token,form.password.data)
        if success:
            flash('您的密码已更新，请使用新密码登录！')
            return redirect(url_for('web.login'))
    return render_template('reset_password,html')

@loginBP.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass




