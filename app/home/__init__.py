from flask import Blueprint

# 创建前端home蓝本对象
home = Blueprint('home', __name__)

# import app.home.views


# 蓝本的基本配置 方便蓝本的添加
# DEFAULT_BLUEPRINT = (
#     # 蓝本名字 前缀
#     (home, '/home'),
# )


# 注册蓝本
def config_blueprint(app):
    from app.home import views
    app.register_blueprint(home, url_prefix='/home')
