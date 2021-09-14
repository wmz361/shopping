from flask import Flask
from myapp.web.index import indexBP


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('myapp.config.secure')
    app.config.from_object('myapp.config.setting')
    app.register_blueprint(indexBP)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app