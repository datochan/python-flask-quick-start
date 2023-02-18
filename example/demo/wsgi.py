import os
from flask_migrate import Migrate

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

migrate = Migrate(app, db)

#
# # 初始化数据库：
# flask db init
#
# # 迁移新更改：
# flask db migrate
#
# # 升级：
# flask db upgrade
#
# # 启动服务
# flask run
