from datetime import datetime, date, timedelta
from database.models import db, User, Activity

def update_streak(user):
    today = date.today()
    if user.last_activity_date == today:
        return
    
    if user.last_activity_date == today - timedelta(days=1):
        user.streak_count += 1
