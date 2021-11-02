from datetime import datetime
from contextlib import contextmanager
from sqlalchemy import Column, Integer, SmallInteger
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

db = SQLAlchemy(query_class=Query)

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

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

    def to_dict(self):
        ''' 把查询出来的内容转换为字典 '''
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # 将查出来的所有对象都转换成json的函数
    def to_json(all_vendors):
        v = [ven.to_dict() for ven in all_vendors]
        return v




