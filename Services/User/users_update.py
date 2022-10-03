import pymongo

from Models.User import User

import Services.Database.database_pymongo

def update_users(users_, User): 
    users_update =Services.database_pymongo.ConnectPymongo.db.users
    dic_set = {'$set': users_}
    users_id = users_update.update_one(User.__dict__(), dic_set)

    return f"User successfully updated"
