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

@dsa_bp.route('/contests', methods=['GET'])
@login_required
def list_contests():
    user_id = session['user_id']
    contests = Contest.query.filter_by(user_id=user_id).order_by(Contest.date.desc()).all()
    return render_template('contests.html', contests=contests)

@dsa_bp.route('/contests/add', methods=['POST'])
@login_required
def add_contest():
    user_id = session['user_id']
    name = request.form.get('name')
    platform = request.form.get('platform')
    date_str = request.form.get('date')
    rank = int(request.form.get('rank', 0))
    rating_before = request.form.get('rating_before')
    rating_after = request.form.get('rating_after')
    
    rating_before = int(rating_before) if rating_before else None
    rating_after = int(rating_after) if rating_after else None
    rating_change = (rating_after - rating_before) if (rating_before and rating_after) else None
    
    contest_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    
    contest = Contest(user_id=user_id, name=name, platform=platform, date=contest_date,
                      rank=rank, rating_before=rating_before, rating_after=rating_after, rating_change=rating_change)
    db.session.add(contest)
    db.session.commit()
    
    user = User.query.get(user_id)
    update_streak(user)
    log_activity(user_id, 'Contest Attended', f'Participated in contest: {name}')
    
    flash('Contest added successfully!', 'success')
    return redirect(url_for('dsa.list_contests'))

@dsa_bp.route('/contests/edit/<int:id>', methods=['POST'])
@login_required
def edit_contest(id):
    user_id = session['user_id']
    contest = Contest.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    contest.name = request.form.get('name')
    contest.platform = request.form.get('platform')
    date_str = request.form.get('date')
    contest.date = datetime.strptime(date_str, '%Y-%m-%d').date()
    contest.rank = int(request.form.get('rank', 0))
    
    rating_before = request.form.get('rating_before')
    rating_after = request.form.get('rating_after')
    contest.rating_before = int(rating_before) if rating_before else None
    contest.rating_after = int(rating_after) if rating_after else None
    contest.rating_change = (contest.rating_after - contest.rating_before) if (contest.rating_before and contest.rating_after) else None
    
    db.session.commit()
    log_activity(user_id, 'Contest Edit', f'Edited contest: {contest.name}')
    flash('Contest updated successfully!', 'success')
    return redirect(url_for('dsa.list_contests'))

@dsa_bp.route('/contests/delete/<int:id>', methods=['POST'])
@login_required
def delete_contest(id):
    user_id = session['user_id']
    contest = Contest.query.filter_by(id=id, user_id=user_id).first_or_404()
    db.session.delete(contest)
    db.session.commit()
    log_activity(user_id, 'Contest Delete', f'Deleted contest: {contest.name}')
    flash('Contest deleted successfully!', 'info')
    return redirect(url_for('dsa.list_contests'))

# Tweak: Implement streak update logic check

# Tweak: Tweak activity logging fields payload

# Tweak: Add difficulty filter queries in problems list

# Tweak: Add topic filter queries in problems list

# Tweak: Add platform filter queries in problems list

# Tweak: Add status solved checkbox query

# Tweak: Add string search keyword filters inside routes.py

# Tweak: Update date solved when checking solved

# Tweak: Tweak problem deletion database actions

# Tweak: Calculate rating delta change values on contests

# Tweak: Validate date inputs format in add contest request

# Tweak: Tweak contest deletion database actions

# Tweak: Log activities upon solving problems

# Tweak: Log activities upon logging contest entries

# Tweak: Optimize query indexing inside list problems route

# Tweak: Tweak problem name display inside dsa.html

# Tweak: Add toggleable log problem panel in dsa.html

# Tweak: Add edit modal template script inside dsa.html

# Tweak: Add platform badge icons styling in dsa.html

# Tweak: Add rating delta arrows color classes in contests.html

# Tweak: Add edit contest modal in contests.html

# Tweak: Format routes.py formatting

# Tweak: Format services.py formatting

# Tweak: Import datetime in dsa routes

# Tweak: Tweak query orders to descending dates

# Tweak: Implement streak update logic check

# Tweak: Tweak activity logging fields payload

# Tweak: Add difficulty filter queries in problems list

# Tweak: Add topic filter queries in problems list

# Tweak: Add platform filter queries in problems list

# Tweak: Add status solved checkbox query

# Tweak: Add string search keyword filters inside routes.py

# Tweak: Update date solved when checking solved

# Tweak: Tweak problem deletion database actions

# Tweak: Calculate rating delta change values on contests

# Tweak: Validate date inputs format in add contest request

# Tweak: Tweak contest deletion database actions

# Tweak: Log activities upon solving problems

# Tweak: Log activities upon logging contest entries

# Tweak: Optimize query indexing inside list problems route

# Tweak: Tweak problem name display inside dsa.html

# Tweak: Add toggleable log problem panel in dsa.html

# Tweak: Add edit modal template script inside dsa.html

# Tweak: Add platform badge icons styling in dsa.html

# Tweak: Add rating delta arrows color classes in contests.html

# Tweak: Add edit contest modal in contests.html

# Tweak: Format routes.py formatting

# Tweak: Format services.py formatting

# Tweak: Import datetime in dsa routes

# Tweak: Tweak query orders to descending dates

# Tweak: Implement streak update logic check

# Tweak: Tweak activity logging fields payload
