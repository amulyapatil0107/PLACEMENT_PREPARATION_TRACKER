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


