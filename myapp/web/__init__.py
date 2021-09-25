from flask import Blueprint, render_template

web=Blueprint('web',__name__)

@web.app_errorhandler(404)
def not_found(e):
    ''' 重写找不到资源时的业务逻辑（基于AOP思想） '''
    return render_template('404.html'),404