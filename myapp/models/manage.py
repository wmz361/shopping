

from myapp.models.base import Base,db # 导入数据库对象
from werkzeug.security import generate_password_hash  # 哈希加密
from myapp.models import user # 导入数据表类

def db_init():
    db.drop_all() # 删除已有数据表
    db.create_all() # 创建新数据表
    db.session.add() # 添加入session
    db.session.commit() # 提交给数据库
    print("数据库初始化成功")