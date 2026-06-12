from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import db, Goal, Problem, Contest, AptitudeProgress
from auth.routes import login_required
from dsa.services import log_activity
from datetime import datetime

goals_bp = Blueprint('goals', __name__)

def update_goal_progress(user_id):
    goals = Goal.query.filter_by(user_id=user_id, is_completed=False).all()
