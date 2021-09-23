# coding=utf-8
from flask import  render_template, request, redirect, url_for, flash
# from flask_login import login_required

from myapp.forms.register import RegisterForm, LoginForm
from myapp.models.base import db
from myapp.models.user import User

from flask import Blueprint

webBP=Blueprint('webBP',__name__)

@webBP.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')

@webBP.route('/register', methods=['GET','POST'])
def register():
    registerForm=RegisterForm(request.form)
    if request.method == 'POST' and registerForm.validate():
        user = User()
        user.username=registerForm['username']
        user.password = registerForm['password']
        if registerForm['gender']=='1':
            user.gender=1
        else:
            user.gender=0
        user.phone_num=registerForm['phone_num']
        user.birthday=registerForm['birthday']
        db.session.add(user)
        db.session.commit()
        flash('注册成功，跳转至首页！')
        return redirect(url_for('webBP.indexLogin',uname=registerForm['username']))
    return render_template('register.html',form=registerForm)

@webBP.route('/login', methods=['GET','POST'])
def login():
    loginForm = LoginForm(request.form)
    if request.method == 'POST' and loginForm.validate():
        user=User()
        users = user.query.filter_by(username=loginForm['username']).first()
        if users:
            flash('登录成功！')
            return redirect(url_for('webBP.indexLogin',uname=loginForm['username']))
        else:
            flash('用户没有注册，请先注册')
    return render_template('login.html')

@webBP.route('/indexLogin/?', methods=['GET','POST'])
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



