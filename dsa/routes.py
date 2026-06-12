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
    
    user = User.query.get(user_id)
    update_streak(user)
    log_activity(user_id, 'DSA Solved' if status_val else 'DSA Added', f'Added problem: {name}')
    
    flash('Problem added successfully!', 'success')
    return redirect(url_for('dsa.list_problems'))

@dsa_bp.route('/dsa/edit/<int:id>', methods=['POST'])
@login_required
def edit_problem(id):
    user_id = session['user_id']
    problem = Problem.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    problem.name = request.form.get('name')
    problem.topic = request.form.get('topic')
    problem.difficulty = request.form.get('difficulty')
    problem.platform = request.form.get('platform')
    
    prev_status = problem.status
    new_status = request.form.get('status') == 'solved'
    problem.status = new_status
    problem.notes = request.form.get('notes')
    
    if new_status and not prev_status:
        problem.date_solved = datetime.today().date()
        user = User.query.get(user_id)
        update_streak(user)
    elif not new_status:
        problem.date_solved = None
        
    db.session.commit()
    log_activity(user_id, 'DSA Edit', f'Edited problem: {problem.name}')
    flash('Problem updated successfully!', 'success')
    return redirect(url_for('dsa.list_problems'))

@dsa_bp.route('/dsa/delete/<int:id>', methods=['POST'])
@login_required
def delete_problem(id):
    user_id = session['user_id']
    problem = Problem.query.filter_by(id=id, user_id=user_id).first_or_404()
    db.session.delete(problem)
    db.session.commit()
    log_activity(user_id, 'DSA Delete', f'Deleted problem: {problem.name}')
    flash('Problem deleted successfully!', 'info')
    return redirect(url_for('dsa.list_problems'))

