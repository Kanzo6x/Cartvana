from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user, logout_user
from cartvana.app import db

ui = Blueprint('ui', __name__, template_folder='templates' ,static_folder='static')

@ui.route('/',methods=['GET'])
def home():
    return render_template('ui/home.html')

@ui.route('/login',methods=['GET'])
def login():
    return 'Login Page'

@ui.route('/register',methods=['GET'])
def register():
    return 'Register Page'

@ui.route('/shop',methods=['GET'])
def shop():
    return 'shop'

@ui.route('/Search',methods=['GET'])
def search():
    return 'Search Page'

@login_required
@ui.route('/MyCart',methods=['GET'])
def my_cart():
    return 'My Cart Page'

@login_required
@ui.route('/MyOrders',methods=['GET'])
def my_orders():
    return 'My Orders Page'

@ui.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('ui.home'))