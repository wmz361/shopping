# 注册登录相关内容
from flask import jsonify
from myapp.api import apiBP
from myapp.forms.register import RegisterForm, LoginForm, ResetPasswordForm
from myapp.models.base import db
from myapp.models.user import User
from myapp.utils.exception_catch import exceptionCatch
from myapp.utils.response_code import RET

ec=exceptionCatch()

@apiBP.route('/user', methods=['POST'])
def register():
    """ 用户注册 """
    registerForm = RegisterForm().body_data()
    if registerForm.validate():
        with ec.dataBase_exception():
            with db.auto_commit():
                user = User()
                user.set_attrs(registerForm.data)
                db.session.add(user)
        return jsonify(errno=RET.OK, errmsg="OK", data={'userId':user.userid})

@apiBP.route('/login', methods=['POST'])
def login():
    ''' 登录 '''
    loginForm = LoginForm().body_data()
    if loginForm.validate():
        with ec.dataBase_exception():
            user = User.query.filter(User.username==loginForm.data['username']).first()
            if user and user.check_password(loginForm.password.data):
                return jsonify(errno=RET.OK, errmsg="OK", data={'userId':user.userid})
            else:
                return jsonify(errno=RET.LOGINERR, errmsg="登录信息验证失败", data=[])
    else:
        return jsonify(errno=RET.LOGINERR, errmsg="登录信息验证失败", data=[])

@apiBP.route('/reset/password/<token>', methods=['POST'])
def reset_password(token):
    ''' 重置密码 '''
    form=ResetPasswordForm().body_data()
    if form.validate():
        with ec.dataBase_exception():
            success=User.reset_password(token,form.password.data)
            if success:
                return jsonify(errno=RET.OK, errmsg="OK", data={'userId':User.userid})
            else:
                return jsonify(errno=RET.PARAMERR, errmsg="密码重置失败", data={'userId': User.userid})
    else:
        return jsonify(errno=RET.DATAERR, errmsg="数据错误", data={'userId': User.userid})





