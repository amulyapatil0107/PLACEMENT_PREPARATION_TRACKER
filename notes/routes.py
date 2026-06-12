from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import db, Note
from auth.routes import login_required
from dsa.services import log_activity

notes_bp = Blueprint('notes', __name__)

