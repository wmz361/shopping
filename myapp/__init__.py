from flask import Flask
from flask_mail import Mail
from myapp.models.base import db
from myapp.web import web
from flask_login import LoginManager

login_manager=LoginManager()
mail=Mail()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('myapp.config.secure')
    app.config.from_object('myapp.config.setting')
    app.register_blueprint(web)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view='loginBP.login'  # 访问未授权页面时直接跳转到loginBP.login页面
    login_manager.login_message='请先注册或者登录！'  # 访问未授权页面时直接跳转到loginBP.login页面时的提示信息
    mail.init_app(app)

    with app.app_context():
        db.create_all()
    return app
