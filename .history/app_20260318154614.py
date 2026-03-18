from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret"
db = SQLAlchemy(app)

if __name__ == '__main-__':
    app.run(debug=True)