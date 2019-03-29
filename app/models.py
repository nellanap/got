from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    score = db.Column(db.Integer)
    responses = db.relationship('Response', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.String(64))
    q2 = db.Column(db.String(64))
    q3 = db.Column(db.String(64))
    q4 = db.Column(db.String(64))
    q5 = db.Column(db.String(64))
    q6 = db.Column(db.String(64))
    q7 = db.Column(db.String(64))
    q8 = db.Column(db.String(64))
    q9 = db.Column(db.String(64))
    q10 = db.Column(db.String(64))
    q11 = db.Column(db.String(64))
    q12 = db.Column(db.String(64))
    q13 = db.Column(db.String(64))
    q14 = db.Column(db.String(64))
    q15 = db.Column(db.String(64))
    q16 = db.Column(db.String(64))
    q17 = db.Column(db.String(64))
    q18 = db.Column(db.String(64))
    q19 = db.Column(db.String(64))
    q20 = db.Column(db.String(64))
    q21 = db.Column(db.String(64))
    q22 = db.Column(db.String(64))
    q23 = db.Column(db.String(64))
    q24 = db.Column(db.String(64))
    q25 = db.Column(db.String(64))
    q26 = db.Column(db.String(64))
    q27 = db.Column(db.String(64))
    q28 = db.Column(db.String(64))
    q29 = db.Column(db.String(64))
    q30 = db.Column(db.String(64))
    score = db.Column(db.Integer)
    rank = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Response {}>'.format(self.user_id)
