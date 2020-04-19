from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from dataclasses import dataclass
from project import app



db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@dataclass
class Category(db.Model):
    __tablename__ = "categories"
    id: int
    name: str
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)

    def __repr__(self):
        return '<Category %r>' % self.name
