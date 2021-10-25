from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from myapp.models.base import db
from myapp.web.Merchant import merchantBP
from myapp.web.goods import goodsBP
from myapp.web.index import indexBP
from myapp.web.login import loginBP
from myapp.web.shoppingCart import shoppingCartBP
from myapp.web.userCenter import userCenterBP

# login_manager=LoginManager()
mail=Mail()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('myapp.config.secure')
    app.config.from_object('myapp.config.setting')
    app.register_blueprint(indexBP)
    app.register_blueprint(loginBP)
    app.register_blueprint(merchantBP)
    app.register_blueprint(goodsBP)
    app.register_blueprint(userCenterBP)
    app.register_blueprint(shoppingCartBP)
    db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_view='loginBP.index'  # 访问未授权页面时直接跳转到loginBP.login页面
    # login_manager.login_message='请先注册或者登录！'  # 访问未授权页面时直接跳转到loginBP.login页面时的提示信息
    mail.init_app(app)

    with app.app_context():
        db.create_all()
    return app
