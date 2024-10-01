from flask import Flask
from flask_migrate import Migrate
from models import db

#create a flask application
app = Flask(__name__)  # Creates a new instance of the Flask application

#configure database connection to local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskdb.db'

#disable modification tracking to use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

#create a migrate object to get schema modifications
migrate = Migrate(app,db)

#initialize the flask application to use the database
db.init_app(app)


@app.route('/')
def index():
    return "Welcome to Flask"

@app.route('/users/<string:username>/<int:age>')
def getUsername(username,age):
    return f"Welcome to Flask Development, {username} and you are {age} years old !"

# @app.route('/users/<int:age>')
# def getAge(age):
#     return f"User here is your age:"




if __name__ == '__main__':
    app.run(port=5900, debug=True)  # Set to debug=True during development


 