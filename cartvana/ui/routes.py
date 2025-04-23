from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from cartvana.app import db

ui = Blueprint('ui', __name__, template_folder='templates' ,static_folder='static')

@ui.route('/',methods=['GET'])
def home():
    return render_template('ui/home.html')

@ui.route('/login',methods=['GET'])
def login():
    pass

@ui.route('/register',methods=['GET'])
def register():
    pass

@ui.route('/all_categories',methods=['GET'])
def all_categories():
    pass

@ui.route('/Search',methods=['GET'])
def search():
    pass

@login_required
@ui.route('/MyCart',methods=['GET'])
def my_cart():
    pass