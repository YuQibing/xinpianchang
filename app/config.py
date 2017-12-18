import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 设置基类
class Config:
    # 设置密钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or "\x98\xeb\xa6\xa1\xd1)\xb1\xc6\xad\x86\xd7\xf6l\xd2\xd8"
    # 设置数据库自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 数据库关闭警告关闭
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


# 配置Sql数据库
class SqlDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.sqlite')


class SqlTestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.sqlite')


class SqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'sql.sqlite')


# 配饰Mysql数据库
class MysqlDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/xinpianchang?charset=utf8'


class MysqlTestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/xinpianchang'


class MysqlConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/xinpianchang'


config = {
    'SqlDevelopmentConfig': SqlDevelopmentConfig,
    'SqlTestConfig': SqlTestConfig,
    'SqlConfig': SqlConfig,
    'MysqlDevelopmentConfig': MysqlDevelopmentConfig,
    'MysqlTestConfig': MysqlTestConfig,
    'MysqlConfig': MysqlConfig,
    'default': MysqlDevelopmentConfig
}
