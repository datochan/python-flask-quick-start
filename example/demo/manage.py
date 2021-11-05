import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import DEMO_MODULES
from configure import config, DemoConfig
from flask_quick.lib.bootstrap import create_app
from flask_quick.lib.extensions import db, login_manager

os.environ['PROJECT_PATH'] = os.path.abspath(os.path.dirname(__file__))

app = create_app(config.get(os.getenv('FLASK_CONFIG'), DemoConfig()),
                 extension=[db, login_manager], modules=DEMO_MODULES)

# 导入环境变量覆盖默认配置
if os.path.exists('./conf/config.properties'):
    print('Importing environment... ')
    for line in open('./conf/config.properties'):
        content = line.strip()
        if len(content) <= 0 or content[0] == '#':
            continue

        var = content.split('=')
        if len(var) == 2:
            app.config[var[0]] = var[1]

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))

#
# python3 ./manage.py db init
# python3 ./manage.py db migrate -m "initial migration"
# python3 ./manage.py db upgrade
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
