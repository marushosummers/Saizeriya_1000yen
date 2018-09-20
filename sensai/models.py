from sensai import db
from sqlalchemy import Column, Integer, String

class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    category = db.Column(db.String(32))
    type = db.Column(db.String(32))
    price = db.Column(db.Integer)
    calorie = db.Column(db.Integer)
    salt = db.Column(db.Integer)


def init():
    db.create_all()
