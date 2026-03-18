from app import db

class User(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    
