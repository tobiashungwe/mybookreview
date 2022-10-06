import datetime
import mongoengine as me

    
class Like(me.EmbeddedDocument): 
    
    review_id =  me.IntField(me.ReferenceField('Review'))
    reviewer =  me.IntField(me.ReferenceField('User'))
    date_created = me.DateTimeField(default=datetime.datetime.now())
    meta = {'collection': 'likes', 'strict': False}
    
    def to_json(self):        
        return {
            "date_created": self.date_created,
                "review_id": self.review_id,
                "reviewer": self.reviewer,   
            }
        