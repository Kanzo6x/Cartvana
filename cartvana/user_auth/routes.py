from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_login import login_required, current_user, logout_user, login_user
from cartvana.app import db, bcrypt
from cartvana.ui.models import User
from datetime import datetime

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/create-account', methods=['POST'])
def create_new_account():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('ui.home'))
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validate input fields
        if not all([username, email, password]):
            flash('All fields are required')
            return redirect(url_for('ui.register'))
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('ui.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return redirect(url_for('ui.register'))
        
        try:
            # Create new user
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(
                username=username,
                email=email,
                password=hashed_password,
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
            
            # Save to database
            db.session.add(new_user)
            db.session.commit()
            
            # Log in the new user
            login_user(new_user)
            flash('Account created successfully!')
            return redirect(url_for('ui.home'))
            
        except Exception as e:
            db.session.rollback()
            flash('Error creating account. Please try again.')
            return redirect(url_for('ui.register'))
            
    except Exception as e:
        flash('An unexpected error occurred. Please try again.')
        return redirect(url_for('ui.register'))

@auth.route('/login-account', methods=['POST'])
def login_account():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('ui.home'))
        
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not all([email, password]):
            flash('All fields are required')
            return redirect(url_for('ui.login'))
        
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Logged in successfully!')
            return redirect(url_for('ui.home'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('ui.login'))
            
    except Exception as e:
        flash('An unexpected error occurred. Please try again.')
        return redirect(url_for('ui.login'))