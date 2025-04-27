from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages, current_app
from flask_login import login_required, current_user, logout_user
from cartvana.app import db
from cartvana.ui.models import Category, Product

ui = Blueprint('ui', __name__, template_folder='templates')

@ui.route('/',methods=['GET'])
def home():
    messages = get_flashed_messages()
    # Get 3 random products
    random_products = Product.query.order_by(db.func.random()).limit(3).all()
    categories = Category.query.all()
    return render_template('ui/home.html', messages=messages, random_products=random_products, categories=categories)

@ui.route('/login',methods=['GET'])
def login():
    messages = get_flashed_messages()
    if current_user.is_authenticated:
        return redirect(url_for('ui.home'))
    return render_template('ui/login.html', messages=messages)

@ui.route('/register',methods=['GET'])
def register():
    messages = get_flashed_messages()
    if current_user.is_authenticated:
        return redirect(url_for('ui.home'))
    return render_template('ui/register.html', messages=messages)

@ui.route('/shop',methods=['GET'])
def shop():
    products = Product.query.all()
    categories = Category.query.all()
    # Debug logging
    for category in categories:
        print(f"Category: {category.name}, Image: {category.image}")
    return render_template('ui/shop.html', products=products, categories=categories)

@ui.route('/Search',methods=['GET'])
def search():
    return 'Search Page'

@ui.route('/MyCart',methods=['GET'])
@login_required
def my_cart():
    return 'My Cart Page'

@ui.route('/MyOrders',methods=['GET'])
@login_required
def my_orders():
    return 'My Orders Page'

@ui.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('ui.home'))

@ui.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    if not product:
        flash('Product not found', 'error')
        return redirect(url_for('ui.shop'))
    return render_template('ui/product_detail.html', product=product)