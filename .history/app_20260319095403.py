from flask import Flask,request
from models.user import User
from database import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

@app.route('/login', (self, *args, **kwargs):
    return super().(*args, **kwargs)
)

if __name__ == '__main-__':
    app.run(debug=True)