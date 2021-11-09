from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_mail import Mail
from flask_wtf import CSRFProtect
import logging
from myapp.libs.redisDealwith import Redis
from myapp.models.base import db
from myapp.utils.commons import ReConverter
from myapp.web.Merchant import merchantBP
from myapp.web.goods import goodsBP
from myapp.web.index import indexBP
from myapp.web.login import loginBP
from myapp.web.shoppingCart import shoppingCartBP
from myapp.web.test001 import testBP
from myapp.web.userCenter import userCenterBP
from myapp.web.web_html import html

mail=Mail()

# 配置日志信息
# 设置日志的记录等级
logging.basicConfig(level=logging.INFO)
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日记录器
logging.getLogger().addHandler(file_log_handler)

# 工厂模式
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # 为flask添加自定义转换器
    app.url_map.converters['re']=ReConverter
    app.config.from_object('myapp.config.secure')
    app.config.from_object('myapp.config.setting')
    app.register_blueprint(indexBP,url_prefix='/index')
    app.register_blueprint(loginBP,url_prefix='/login')
    app.register_blueprint(merchantBP,url_prefix='/merchant')
    app.register_blueprint(goodsBP,url_prefix='/goods')
    app.register_blueprint(userCenterBP,url_prefix='/userCenter')
    app.register_blueprint(shoppingCartBP,url_prefix='/shopping')
    app.register_blueprint(testBP,url_prefix='/test')
    app.register_blueprint(html)
    # redis_store=Redis._get_r()
    # db绑定app
    db.init_app(app)
    # 为flask添加csrf防护机制
    CSRFProtect(app)
    # login_manager.init_app(app)
    # login_manager.login_view='loginBP.index'  # 访问未授权页面时直接跳转到loginBP.login页面
    # login_manager.login_message='请先注册或者登录！'  # 访问未授权页面时直接跳转到loginBP.login页面时的提示信息
    mail.init_app(app)

    with app.app_context():
        # 删除表
        db.drop_all()
        # 创建表
        db.create_all()
    return app
