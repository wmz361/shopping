# coding=utf-8
from flask import  render_template, request, redirect, url_for, flash
from flask_login import login_required

from myapp.forms.register import RegisterForm
from myapp.models.base import db
from myapp.models.user import User

from flask import Blueprint

webBP=Blueprint('webBP',__name__)

@webBP.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')

@webBP.route('/register', methods=['GET','POST'])
def register():
    form=request.form
    if request.method == 'POST':
        user = User()
        user.username=form['username']
        user.password = form['password']
        if form['gender']=='1':
            user.gender=1
        else:
            user.gender=0
        user.phone_num=form['phone_num']
        user.birthday=form['birthday']
        db.session.add(user)
        db.session.commit()
        flash('注册成功，跳转至首页！')
        return redirect(url_for('webBP.indexLogin',uname=form['username']))
    return render_template('register.html',form=form)

@webBP.route('/login', methods=['GET','POST'])
def login():
    form = request.form
    if request.method == 'POST':
        user=User()
        users = user.query.filter_by(username=form['username']).first()
        if users:
            flash('登录成功！')
            return redirect(url_for('webBP.indexLogin',uname=form['username']))
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
        return render_template('indexLogined1.html',username=uname,goods=goods)
    return '跳转首页失败'

@webBP.route('/test', methods=['GET','POST'])
@login_required
def test():
    if request.method=='GET':
        return render_template('indexLogined1.html')
    return '跳转首页失败'

