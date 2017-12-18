# 引入扩展包
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# 创建相关对象
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate(db=db)


# 初始化对象
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app)

    # 设置浏览的条件必须登录 以及登录的提示信息
    login_manager.login_message = '必须登录后才能浏览'
    # 跳转到此views
    login_manager.login_view = ''
    # 设置登录的安全级别
    login_manager.session_protection = 'strong'
