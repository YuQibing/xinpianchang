from flask import Flask
from app.config import config
from app import extensions
from app import home, user


def create_app(config_name):
    # 创建一个实例
    app = Flask(__name__)
    # 初始化配置
    app.config.from_object(config[config_name])
    # 初始化函数
    config[config_name].init_app(app)
    # 初始化扩展包
    extensions.config_extensions(app)
    # 初始化
    home.config_blueprint(app)
    user.config_blueprint(app)
    # from app.home import home
    # app.register_blueprint(home, url_prefix='/home')
    return app
