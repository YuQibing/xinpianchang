import os
from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand, migrate

config_name = os.environ.get('CONFIG') or 'default'

app = create_app(config_name)

# 创建manager来管理app
manager = Manager(app)
# 增加终端控制
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
