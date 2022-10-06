import datetime
from Models.Comment import Comment
from Models.Like import Like
from Models.User import User
from Services.Database.database_monoengine import db
import mongoengine as me

class Review(me.Document):
    
    text = me.StringField(required=True)
    date_created = me.DateTimeField(default=datetime.datetime.now)
    reviewer = me.ReferenceField('User')
    comments = me.ListField(me.EmbeddedDocumentField(Comment))
    likes = me.ListField(me.EmbeddedDocumentField(Like))
    meta = {'allow_inheritance': True, 'collection': 'reviews', 'strict': False}