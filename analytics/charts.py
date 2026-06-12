from database.models import db, Problem, Contest, Goal, AptitudeProgress
from sqlalchemy import func
from datetime import datetime, timedelta

def get_dsa_topic_stats(user_id):
    stats = db.session.query(
        Problem.topic, 
        func.count(Problem.id)
    ).filter_by(user_id=user_id, status=True).group_by(Problem.topic).all()
    return {topic: count for topic, count in stats}

def get_dsa_difficulty_stats(user_id):
    stats = db.session.query(
        Problem.difficulty, 
        func.count(Problem.id)
    ).filter_by(user_id=user_id, status=True).group_by(Problem.difficulty).all()
    return {diff: count for diff, count in stats}

def get_monthly_solving_progress(user_id):
    today = datetime.today()
    six_months_ago = today - timedelta(days=180)
    
    stats = db.session.query(
        func.strftime('%Y-%m', Problem.date_solved),
        func.count(Problem.id)
    ).filter(
        Problem.user_id == user_id,
        Problem.status == True,
        Problem.date_solved >= six_months_ago.date()
    ).group_by(
        func.strftime('%Y-%m', Problem.date_solved)
    ).order_by(
        func.strftime('%Y-%m', Problem.date_solved).asc()
    ).all()
    
    return {month: count for month, count in stats if month}

def get_contest_participation_stats(user_id):
    stats = db.session.query(
        Contest.platform, 
        func.count(Contest.id)
    ).filter_by(user_id=user_id).group_by(Contest.platform).all()
    return {plat: count for plat, count in stats}

def get_goal_completion_stats(user_id):
    total = Goal.query.filter_by(user_id=user_id).count()
    completed = Goal.query.filter_by(user_id=user_id, is_completed=True).count()
    return {
        'total': total,
        'completed': completed,
        'pending': total - completed
    }
