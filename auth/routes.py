from flask import Blueprint, request, redirect, url_for, flash, session, render_template
from database.models import db, User
from auth.forms import RegistrationForm, LoginForm, ProfileForm
from dsa.services import log_activity
from functools import wraps

auth_bp = Blueprint('auth', __name__)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        existing_user = User.query.filter((User.username == form.username.data) | (User.email == form.email.data)).first()
        if existing_user:
            flash('Username or Email already exists.', 'danger')
            return render_template('register.html', form=form)
        
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        log_activity(user.id, 'Register', f'User {user.username} registered.')
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            session['is_admin'] = user.is_admin
            
            log_activity(user.id, 'Login', f'User {user.username} logged in.')
            
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    log_activity(session['user_id'], 'Logout', f"User {session['username']} logged out.")
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = User.query.get(session['user_id'])
    form = ProfileForm(request.form, obj=user)
    if request.method == 'POST' and form.validate():
        user.email = form.email.data
        if form.password.data:
            user.set_password(form.password.data)
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('auth.profile'))
    return render_template('profile.html', form=form, user=user)

# Tweak: Implement login_required security guard decorator

# Tweak: Add email uniqueness validation in signup form

# Tweak: Add password matches constraint validation in signup

# Tweak: Add session handlers upon successful logins

# Tweak: Tweak session clear functionality inside logout controller

# Tweak: Refactor forms validation structure

# Tweak: Add success toast notices on registrations

# Tweak: Add failure alert notices on bad credentials

# Tweak: Add redirect checks if user is already authenticated

# Tweak: Import email validator helper inside forms.py

# Tweak: Tweak length checks on username in registration form

# Tweak: Format auth blueprint code block

# Tweak: Tweak sidebar navigation responsive classes inside base.html

# Tweak: Add dynamic active class links in base.html

# Tweak: Optimize main.js logic

# Tweak: Add fade animations trigger to toast notices in main.js

# Tweak: Implement theme storage handler inside main.js local storage

# Tweak: Add sidebar mobile toggle responsive triggers

# Tweak: Add custom error label placements inside register.html

# Tweak: Add description headings to profile.html

# Tweak: Format forms.py imports block

# Tweak: Refactor session storage keys

# Tweak: Implement login_required security guard decorator

# Tweak: Add email uniqueness validation in signup form

# Tweak: Add password matches constraint validation in signup

# Tweak: Add session handlers upon successful logins

# Tweak: Tweak session clear functionality inside logout controller

# Tweak: Refactor forms validation structure

# Tweak: Add success toast notices on registrations

# Tweak: Add failure alert notices on bad credentials

# Tweak: Add redirect checks if user is already authenticated

# Tweak: Import email validator helper inside forms.py

# Tweak: Tweak length checks on username in registration form

# Tweak: Format auth blueprint code block

# Tweak: Tweak sidebar navigation responsive classes inside base.html

# Tweak: Add dynamic active class links in base.html

# Tweak: Optimize main.js logic

# Tweak: Add fade animations trigger to toast notices in main.js

# Tweak: Implement theme storage handler inside main.js local storage

# Tweak: Add sidebar mobile toggle responsive triggers

# Tweak: Add custom error label placements inside register.html

# Tweak: Add description headings to profile.html

# Tweak: Format forms.py imports block

# Tweak: Refactor session storage keys

# Tweak: Implement login_required security guard decorator

# Tweak: Add email uniqueness validation in signup form

# Tweak: Add password matches constraint validation in signup

# Tweak: Add session handlers upon successful logins

# Tweak: Tweak session clear functionality inside logout controller

# Tweak: Refactor forms validation structure

# Tweak: Add success toast notices on registrations

# Tweak: Add failure alert notices on bad credentials
