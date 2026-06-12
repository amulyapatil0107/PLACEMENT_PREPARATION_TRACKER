from flask import Blueprint, render_template, jsonify, session
from auth.routes import login_required
from analytics import charts

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics')
@login_required
def dashboard_analytics():
    return render_template('analytics.html')

@analytics_bp.route('/api/analytics-data')
@login_required
def get_analytics_data():
    user_id = session['user_id']
    
    topic_stats = charts.get_dsa_topic_stats(user_id)
    difficulty_stats = charts.get_dsa_difficulty_stats(user_id)
    monthly_progress = charts.get_monthly_solving_progress(user_id)
    contest_stats = charts.get_contest_participation_stats(user_id)
    goal_stats = charts.get_goal_completion_stats(user_id)
    
    return jsonify({
        'topics': topic_stats,
