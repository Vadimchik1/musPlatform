from application import manager
from main import *


@manager.command
def db_create():
    db.create_all()


if __name__ == '__main__':
    manager.run()
