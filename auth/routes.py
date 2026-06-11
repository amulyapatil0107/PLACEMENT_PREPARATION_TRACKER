from flask import Blueprint, request, redirect, url_for, flash, session, render_template
from database.models import db, User
from auth.forms import RegistrationForm, LoginForm, ProfileForm
from dsa.services import log_activity
from functools import wraps

auth_bp = Blueprint('auth', __name__)
