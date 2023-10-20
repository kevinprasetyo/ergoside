from apps import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Cv(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    risiko = db.Column(db.Text, nullable=True)
    skor = db.Column(db.Integer, nullable=True)
    tanggal = db.Column(db.DateTime(timezone=True), default=func.now())