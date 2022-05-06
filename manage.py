
from app import create_app,db
from flask_script import Manager,Server
from app.dbmodels import User,Role
from  flask_migrate import Migrate,MigrateCommand
from app.dbmodels import User,Role,Review


app=create_app('development')
manager = Manager(app)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Role=Role,Review=Review )


migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
