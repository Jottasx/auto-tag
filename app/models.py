from . import db 

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    emb = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(300), nullable=True)
    edited = db.Column(db.Integer, nullable=False)
    printed = db.Column(db.Integer, nullable=False)
    local = db.Column(db.Integer, nullable=False)
