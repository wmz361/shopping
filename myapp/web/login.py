# coding=utf-8
from flask import  render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required
from myapp.forms.register import RegisterForm, LoginForm, PhoneNumForm, EmailForm, ResetPasswordForm
from myapp.models.base import db
from myapp.models.user import User
from myapp.web import web


@web.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')

@web.route('/register', methods=['GET','POST'])
def register():
    registerForm=RegisterForm(request.form)
    if request.method == 'POST' and registerForm.validate():
        with db.auto_commit():
            user = User()
            user.set_attrs(registerForm.data)
            db.session.add(user)
        flash('注册成功，跳转至首页！')
        return redirect(url_for('webBP.indexLogin',uname=registerForm['username']))
    return render_template('register.html',form=registerForm)

@web.route('/login', methods=['GET','POST'])
def login():
    loginForm = LoginForm(request.form)
    if request.method == 'POST' and loginForm.validate():
        user = User.query.filter_by(username=loginForm['username']).first()
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
    return render_template('login.html')

@web.route('/indexLogin/?', methods=['GET','POST'])
@login_required
def indexLogin():
    uname=request.args.get('uname')
    if request.method=='GET':
        good1={'title':'商品1',"price":25}
        good2 = {'title': '商品2', "price": 30}
        goods=[]
        goods.append(good1)
        goods.append(good2)
        goodssku=['种类1','种类2','种类3','种类4']
        return render_template('indexLogined1.html',username=uname,goods=goods,goodssku=goodssku)
    return '跳转首页失败'

@web.route('/reset/password', methods=['GET','POST'])
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
    return render_template('reset_password_request.html',form=form)

@web.route('/reset/password/<token>', methods=['GET','POST'])
def reset_password(token):
    form=ResetPasswordForm(request.form)
    if request.method=='POST' and form.validate():
        success=User.reset_password(token,form.password.data)
        if success:
            flash('您的密码已更新，请使用新密码登录！')
            return redirect(url_for('web.login'))
    return render_template('reset_password,html')

@web.route('/change/password', methods=['GET', 'POST'])
def change_password():
    pass




