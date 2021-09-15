from flask import Flask
from myapp.models.base import db
from myapp.web.index import webBP


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('myapp.config.secure')
    app.config.from_object('myapp.config.setting')
    app.register_blueprint(webBP)
    db.init_app(app)
    db.create_all(app=app)
    @app.route('/hello')
    def hello():
        return 'Hello, World!'
    return app