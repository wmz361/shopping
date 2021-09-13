from flask import Blueprint, render_template, request, redirect, url_for

indexBP=Blueprint('indexBP',__name__)

@indexBP.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')

@indexBP.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username=request.form['firstname']
        password=request.form['password']
        password2=request.form['password2']
        phone_num=request.form['phone_num']
        gender=request.form['gender']
        brithday=request.form['brithday']
        print(username)
        print(password)
        print(password2)
        print(phone_num)
        print(gender)
        print(brithday)
        return redirect(url_for('indexBP.login'))
    return render_template('register.html')

@indexBP.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')


