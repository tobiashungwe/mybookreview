import pymongo


'''

Experminnting with different types of connetions, one connection uses pymongo!
This is not best practice but i did this to get a better understanding of  what attributes i liked working with 
So i didn't have to lose time on deciding! 

'''


class ConnectPymongo:

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.mybookreview
