from datetime import datetime, date, timedelta
from database.models import db, User, Activity

def update_streak(user):
    today = date.today()
    if user.last_activity_date == today:
        return
    
    if user.last_activity_date == today - timedelta(days=1):
        user.streak_count += 1
        if user.streak_count > user.longest_streak:
            user.longest_streak = user.streak_count
    elif user.last_activity_date is None or user.last_activity_date < today - timedelta(days=1):
        user.streak_count = 1
        if user.longest_streak == 0:
            user.longest_streak = 1
            
    user.last_activity_date = today
    db.session.commit()

def log_activity(user_id, activity_type, description):
    activity = Activity(user_id=user_id, activity_type=activity_type, description=description)
    db.session.add(activity)
    db.session.commit()
