from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
LoginManager = LoginManager()
admin = Admin()
bcrypt = Bcrypt()

def createApp():
    #configure the app 
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartvana.db'

    #intilize extensions with the app 
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    LoginManager.init_app(app)
    bcrypt.init_app(app)

    #set the secret key for the app
    app.secret_key='cartvana'

    #setting the admin dashboard
    admin.setup(name='Cartvana Admin', template_mode='bootstrap3', index_view_name='Cartvana Admin')
    

    #set the login loader manager class 
    # import the class here 
    @LoginManager.user_loader
    def load_user(uid):
        #return User.query.get(int(uid))
        pass
    
    #put here all the registers and blueprints


    #put here all the modules and add it to admin view 


    return app
