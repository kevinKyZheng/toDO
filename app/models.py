from . import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'list'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64), unique=True)
    time = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Integer, default=0)