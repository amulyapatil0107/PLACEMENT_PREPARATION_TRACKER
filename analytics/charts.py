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
