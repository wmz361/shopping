# coding=utf-8
from flask import  render_template, request, redirect, url_for, flash
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
        user.gender=form['gender']
        user.phone_num=form['phone_num']
        user.birthday=form['birthday']
        db.session.add(user)
        db.session.commit()
        flash('注册成功，跳转至首页！')
        return redirect(url_for('webBP.indexLogin'))
    return render_template('register.html',form=form)

@webBP.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@webBP.route('/indexLogin', methods=['GET','POST'])
def indexLogin():
    if request.method=='GET':
        return render_template('indexLogined.html')
    return '跳转首页失败'

