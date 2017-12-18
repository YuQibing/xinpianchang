from flask import Blueprint

user = Blueprint('user', __name__)


# 蓝本的基本配置 方便蓝本的添加
# DEFAULT_BLUEPRINT = (
#     # 蓝本名字 前缀
#     (home, '/home'),
# )

# 注册蓝本
def config_blueprint(app):
    from app.user import views
    app.register_blueprint(user, url_prefix='/user')
