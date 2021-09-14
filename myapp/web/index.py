from flask import Blueprint, render_template, request, redirect, url_for, flash

from myapp.forms.register import RegisterForm
from myapp.models.base import db
from myapp.models.user import User

indexBP=Blueprint('indexBP',__name__)

@indexBP.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')

@indexBP.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm()
    user = User()
    if request.method == 'POST':
        user.username=form.username.data
        user.password=form.password1.data
        user.phone_num=request.form['phone_num']
        user.gender=request.form['gender']
        user.birthday=request.form['birthday']
        db.session.add(user)
        db.session.commit()
        print(user.username)
        flash('注册成功，跳转至首页！')
        return redirect(url_for('indexLogin'))
    return render_template('register.html')

@indexBP.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@indexBP.route('/indexLogin', methods=['GET','POST'])
def indexLogin():
    name=request.form['username']
    return render_template('indexLogined.html',username=name)

