import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from quick_flask import APP_MODULES
from quick_flask.lib.bootstrap import create_app
from quick_flask.lib.extensions import db

os.environ['PROJECT_PATH'] = os.path.abspath(os.path.dirname(__file__))

app = create_app(os.getenv('FLASK_CONFIG') or 'default', APP_MODULES)

# 导入环境变量覆盖默认配置
if os.path.exists('../conf/config.properties'):
    print('Importing environment... ')
    for line in open('../conf/config.properties'):
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
# python3 ./DTrader.py db init
# python3 ./DTrader.py db migrate -m "initial migration"
# python3 ./DTrader.py db upgrade
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()