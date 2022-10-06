import os

app_config = {
    'ROOT_PATH': os.path.dirname(os.path.abspath(__file__))
}

mongo_config = {
    'IP': 'localhost',
    'PORT': 27017,
    'USERNAME': 'Tobiti',
    'PASSWORD': 'xfiE5ysw9PF41y3A',
    'DB': 'localhost',
    'AUTH': ''
}


email_config = {
    'ADDRESS': '',
    'PASSWORD': '',
    'SMTP': 'smtp.gmail.com',
    'PORT': 587
}

crypto_key = 'abcdefghijklmnopqrstuvwxyz'
session_key = '1'
secret_key = '1'
dev_computer_name = ''
jwt_secret = '1'


def get_mode():
    server = str(os.path.realpath('.'))
    if dev_computer_name in server:
        return 'test'
    else:
        return 'live'
