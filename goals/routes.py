from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import db, Goal, Problem, Contest, AptitudeProgress
from auth.routes import login_required
from dsa.services import log_activity
from datetime import datetime

goals_bp = Blueprint('goals', __name__)

def update_goal_progress(user_id):
    goals = Goal.query.filter_by(user_id=user_id, is_completed=False).all()
    for goal in goals:
        if goal.target_type == 'DSA':
            solved_count = Problem.query.filter_by(user_id=user_id, status=True).count()
            goal.current_value = solved_count
        elif goal.target_type == 'Contest':
            contest_count = Contest.query.filter_by(user_id=user_id).count()
            goal.current_value = contest_count
        elif goal.target_type == 'Aptitude':
            aptitude_count = AptitudeProgress.query.filter_by(user_id=user_id, status='Completed').count()
            goal.current_value = aptitude_count
        
        if goal.current_value >= goal.target_value:
            goal.is_completed = True
            log_activity(user_id, 'Goal Completed', f'Completed goal: {goal.description}')
    db.session.commit()

@goals_bp.route('/goals', methods=['GET'])
@login_required
def list_goals():
    user_id = session['user_id']
