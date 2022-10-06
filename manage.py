from flask import Flask
from Models.User import User
from config import session_key, app_config, jwt_secret
from Controllers import AuthRoutes, ErrorRoutes, ReviewRoutes, BookRoutes
from Services.Database.database_monoengine import db
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_mongoengine import MongoEngine

'''
Basic start up of application 
Database gets imported then configured and injected in the lifetime of the application
Jwt configuration for authentication and authorization
'''

app = Flask(__name__)

# app settings
app.secret_key = session_key
app.static_folder = app_config['ROOT_PATH'] + '/Views/static'
app.template_folder = app_config['ROOT_PATH'].split('Controllers')[0] + '/Views/templates'


# blueprints init
blueprints = [
    ErrorRoutes.mod,
    AuthRoutes.mod,
    ReviewRoutes.mod,
    BookRoutes.mod
    
]

for bp in blueprints:
    app.register_blueprint(bp)

# db stuff
app.config['MONGODB_SETTINGS'] = {
    'db': 'bookreview',
    'host': 'mongodb://localhost/mybookreview'
}
app.url_map.strict_slashes = False



login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth_routes.login'
@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

# jwt stuff
app.config['JWT_SECRET_KEY'] = jwt_secret
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
jwt = JWTManager(app)


if __name__ == '__main__':
    app.run(host="localhost", port=5010, debug=True)
