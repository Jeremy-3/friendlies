from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String ,unique = True)
    age=db.Column(db.Integer)
    
    
