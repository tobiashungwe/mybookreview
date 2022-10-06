import datetime
import mongoengine as me

class Comment(me.EmbeddedDocument): 
    
    text = me.StringField()
    date_created = me.DateTimeField(default=datetime.datetime.now())
    review_id =  me.ReferenceField('Review')
    reviewer = me.ReferenceField('User')
    meta = { 'collection': 'comments', 'strict': False}
    
    def to_json(self):        
        return {"text": self.text,
                "date_created": self.date_created,
                 "review_id": self.review_id,
                 "reviewer": self.reviewer,   
                }
        