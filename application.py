from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

appplicaton = Flask(__name__)
appplicaton.config.from_object(Configuration)
bootstrap = Bootstrap(appplicaton)

login = LoginManager(appplicaton)
login.login_view = 'login'
login.login_message = 'Авторизуйтесь для доступа к закрытым страницам'

db = SQLAlchemy(appplicaton)
migrate = Migrate(appplicaton, db)

admin = Admin(appplicaton, name='mus_platform', template_mode='bootstrap3')

from models import *
from view import *

# manager = Manager(app)
# manager.add_command('db', MigrateCommand)
admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(Song, db.session))
