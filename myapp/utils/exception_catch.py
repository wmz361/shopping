from contextlib import contextmanager
from flask import current_app, jsonify
from myapp.utils.response_code import RET


class exceptionCatch():
    ''' 捕获异常 '''
    @contextmanager
    def dataBase_exception(self):
        """ 定义一个上下文管理器，实现数据库异常的捕获和日志输出 """
        try:
            yield
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="数据库异常")
