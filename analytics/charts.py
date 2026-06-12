from database.models import db, Problem, Contest, Goal, AptitudeProgress
from sqlalchemy import func
from datetime import datetime, timedelta

def get_dsa_topic_stats(user_id):
    stats = db.session.query(
        Problem.topic, 
        func.count(Problem.id)
