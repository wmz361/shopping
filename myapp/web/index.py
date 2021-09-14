from flask import  render_template, request, redirect, url_for, flash

from myapp import web
from myapp.forms.register import RegisterForm
from myapp.models.base import db
from myapp.models.user import User
from myapp.web import webBP


@webBP.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')


@webBP.route('/register', methods=['GET','POST'])
def register():
    form=RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        flash('注册成功，跳转至首页！')
        return redirect(url_for('indexLogin'))
    return render_template('register.html',form=form)

@webBP.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@webBP.route('/indexLogin', methods=['GET','POST'])
def indexLogin():
    name=request.form['username']
    return render_template('indexLogined.html',username=name)

