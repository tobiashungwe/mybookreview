from flask_mongoengine import MongoEngine



'''
The initial launch of the application uses mongo engine when connecting to external apis it uses pyongo to still provide SOC
The Options and conenction settings can be found on inilization

Experminnting with different types of connetions, one connection uses pymongo!
This is not best practice but i did this to get a better understanding of  what attributes i liked working with 
So i didn't have to lose time on deciding! 

'''

db = MongoEngine()
