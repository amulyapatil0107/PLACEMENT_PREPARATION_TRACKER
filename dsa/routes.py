from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import db, Problem, Contest, User
from auth.routes import login_required
from dsa.services import update_streak, log_activity
from datetime import datetime

dsa_bp = Blueprint('dsa', __name__)

@dsa_bp.route('/dsa', methods=['GET'])
@login_required
def list_problems():
    user_id = session['user_id']
    query = Problem.query.filter_by(user_id=user_id)
    
    search = request.args.get('search', '')
    difficulty = request.args.get('difficulty', '')
    topic = request.args.get('topic', '')
    platform = request.args.get('platform', '')
    status = request.args.get('status', '')
    
    if search:
        query = query.filter(Problem.name.like(f'%{search}%') | Problem.notes.like(f'%{search}%'))
    if difficulty:
        query = query.filter_by(difficulty=difficulty)
