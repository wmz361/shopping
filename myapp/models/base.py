from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import Column, Integer, SmallInteger, Date
from flask import current_app
from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy , BaseQuery

__all__ = ['db', 'Base']


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self, throw=True):
        """ 定义一个上下文管理器，实现数据库回滚 """
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            current_app.logger.exception('%r' % e)
            if throw:
                raise e

class Query(BaseQuery):
    def filter_by(self, **kwargs):
        ''' 重写filter_by，查询条件中默认添加status=1 '''
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def order_by(self, **kwargs):
        ''' 重写order_by，查询条件中默认添加status=1 '''
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).order_by(**kwargs)

# 先定义db
db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
    update_time=Column('update_time', Date,default=datetime.now(),onupdate=datetime.now())

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())
        self.status=1

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0

    def set_attrs(self, attrs):
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def to_dict(self,attrs):
        ''' 把查询出来的内容转换为字典 '''
        itemDic={}
        for key, value in attrs.items():
            if hasattr(self, key) and key != 'id':
                itemDic[key]=value
        return itemDic







