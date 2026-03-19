from flask import Flask
from models.user import User
from database import db
from flask_login import 

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'

db.init_app(app)

if __name__ == '__main-__':
    app.run(debug=True)