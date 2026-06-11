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
