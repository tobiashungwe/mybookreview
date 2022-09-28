from email.policy import default
from enum import unique
from pickle import FALSE
from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    reviews = db.relationship('Review', backref='user', passive_deletes=True)
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    reviewer = db.Column(db.Integer, db.ForeignKey('user.id',  ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref='review', passive_deletes=True)
    likes = db.relationship('Like', backref='review', passive_deletes=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    reviewer = db.Column(db.Integer, db.ForeignKey('user.id',  ondelete="CASCADE"), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey('review.id',  ondelete="CASCADE"), nullable=False)

    
