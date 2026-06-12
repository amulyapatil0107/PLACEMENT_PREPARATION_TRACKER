from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import db, AptitudeProgress
from auth.routes import login_required
from dsa.services import log_activity
from datetime import datetime

aptitude_bp = Blueprint('aptitude', __name__)

DEFAULT_TOPICS = {
    'Quantitative Aptitude': [
        'Percentage', 'Profit & Loss', 'Simple & Compound Interest', 
        'Time & Work', 'Time, Speed & Distance', 'Permutation & Combination', 'Probability'
    ],
    'Logical Reasoning': [
        'Number Series', 'Coding-Decoding', 'Blood Relations', 
        'Direction Sense', 'Syllogism', 'Seating Arrangements', 'Data Sufficiency'
    ],
    'Verbal Ability': [
        'Reading Comprehension', 'Sentence Correction', 'Synonyms & Antonyms', 
        'Fill in the Blanks', 'Idioms & Phrases', 'Paragraph Jumbles'
    ]
}

def init_aptitude_topics(user_id):
    existing = AptitudeProgress.query.filter_by(user_id=user_id).first()
    if not existing:
        for category, topics in DEFAULT_TOPICS.items():
            for topic in topics:
                prog = AptitudeProgress(user_id=user_id, category=category, topic_name=topic, status='Not Started', score=0)
                db.session.add(prog)
        db.session.commit()

@aptitude_bp.route('/aptitude', methods=['GET'])
@login_required
def list_aptitude():
    user_id = session['user_id']
    init_aptitude_topics(user_id)
    
    progress_items = AptitudeProgress.query.filter_by(user_id=user_id).all()
    
    grouped = {}
    for cat in DEFAULT_TOPICS.keys():
        grouped[cat] = [item for item in progress_items if item.category == cat]
        
    return render_template('aptitude.html', grouped=grouped)

@aptitude_bp.route('/aptitude/update/<int:id>', methods=['POST'])
@login_required
def update_aptitude(id):
    user_id = session['user_id']
    item = AptitudeProgress.query.filter_by(id=id, user_id=user_id).first_or_404()
    
