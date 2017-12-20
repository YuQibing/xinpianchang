from .views import home

# 蓝本的基本配置 方便蓝本的添加
# DEFAULT_BLUEPRINT = (
#     # 蓝本名字 前缀
#     (home, '/home'),
# )


# 注册蓝本
def config_blueprint(app):
    # from app.home import views
    app.register_blueprint(home, url_prefix='/home')
