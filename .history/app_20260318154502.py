from flask import Flask
from flask_sqlalchemy import S
app = Flask(__name__)

if __name__ == '__main-__':
    app.run(debug=True)