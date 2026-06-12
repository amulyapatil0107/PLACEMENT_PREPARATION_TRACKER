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
    if topic:
        query = query.filter_by(topic=topic)
    if platform:
        query = query.filter_by(platform=platform)
    if status != '':
        query = query.filter_by(status=(status == 'solved'))
        
    problems = query.order_by(Problem.date_created.desc()).all()
    topics = [p[0] for p in db.session.query(Problem.topic).filter_by(user_id=user_id).distinct().all()]
    
    return render_template('dsa.html', problems=problems, topics=topics, 
                           search=search, difficulty=difficulty, topic=topic, platform=platform, status=status)

@dsa_bp.route('/dsa/add', methods=['POST'])
@login_required
def add_problem():
    user_id = session['user_id']
    name = request.form.get('name')
    topic = request.form.get('topic')
    difficulty = request.form.get('difficulty')
    platform = request.form.get('platform')
    status_val = request.form.get('status') == 'solved'
    notes = request.form.get('notes')
    
    date_solved = None
    if status_val:
        date_solved = datetime.today().date()
        
    problem = Problem(user_id=user_id, name=name, topic=topic, difficulty=difficulty, 
                      platform=platform, status=status_val, notes=notes, date_solved=date_solved)
    db.session.add(problem)
    db.session.commit()
    
