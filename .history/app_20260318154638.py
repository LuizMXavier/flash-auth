from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_UR']
db = SQLAlchemy(app)

if __name__ == '__main-__':
    app.run(debug=True)