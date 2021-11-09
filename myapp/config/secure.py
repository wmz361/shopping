# 启动配置
DEBUG=True

# 数据库连接及配置
DIALECT = 'mysql'  # 要用的什么数据库
DRIVER = 'cymysql'  # 连接数据库驱动
USERNAME = 'wmz2018'  # 用户名
PASSWORD = 'Zhuzhujiayou7'  # 密码
HOST = 'rm-wz94v5i7iuca05ftmqo.mysql.rds.aliyuncs.com'  # 服务器
PORT = '3306'  # 端口
DATABASE = 'shop'  # 数据库名
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SECRET_KEY = '\x88D\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJ:U\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'
SQLALCHEMY_TRACK_MODIFICATIONS=True
PROPAGATE_EXCEPTIONS=False

# Email 配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '2084346808@qq.com'
MAIL_PASSWORD = 'gylcbtlwzaqzdaha'
# MAIL_SUBJECT_PREFIX = '[国货集市]'
# MAIL_SENDER = '国货集市 <2084346808@qq.com>'

# redis配置
REDIS_HOST='139.224.18.59'
REDIS_PORT=6379
REDIS_DB=0
REDIS_EXPIRE=86400000

# 设置默认禁用所有的视图CSRF保护
WTF_CSRF_CHECK_DEFAULT = False