from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///localdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True, nullable=False)
    token = Column(String(100))
    hashed_name = Column(String(200))


class Songs(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(100))
    category = Column(String(100))
    path = Column(String(300))
    user_hashed_name = Column(String(200))