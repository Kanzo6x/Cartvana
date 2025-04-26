from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin.contrib.sqla import ModelView
from cartvana.admin import AdminModelView

db = SQLAlchemy()
migrate = Migrate()
LoginManager = LoginManager()
bcrypt = Bcrypt()

#Set up Admin correctly with name and template_mode here
admin = Admin(name='Cartvana Admin', template_mode='bootstrap3')

def create_app():
    # Configure the app 
    app = Flask(__name__,static_folder='static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartvana.db'

    # Initialize extensions with the app 
    db.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    LoginManager.init_app(app)
    LoginManager.login_view = 'ui.login'  
    bcrypt.init_app(app)

    # Set the secret key for the app
    app.secret_key = 'cartvana'

    # Import the models
    from cartvana.ui.models import User, Category, Product, Cart, CartItem, Order, OrderItem  

    # Set the login loader manager class 
    @LoginManager.user_loader
    def load_user(uid):
        return User.query.get(int(uid))

    #Register blueprints here
    from cartvana.ui.routes import ui
    from cartvana.user_auth.routes import auth
    from cartvana.shop.routes import shop
    app.register_blueprint(ui)
    app.register_blueprint(auth)
    app.register_blueprint(shop)

    # Add views to the admin interface
    #admin.add_view(ModelView(User, db.session))
    admin.add_view(AdminModelView(Category, db.session))
    admin.add_view(AdminModelView(Product, db.session))
    admin.add_view(AdminModelView(Cart, db.session))
    admin.add_view(AdminModelView(CartItem, db.session))
    admin.add_view(AdminModelView(Order, db.session))
    admin.add_view(AdminModelView(OrderItem, db.session))
    admin.add_view(AdminModelView(User, db.session)) 

    return app
