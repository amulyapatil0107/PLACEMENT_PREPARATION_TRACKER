from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.models import db, Note
from auth.routes import login_required
from dsa.services import log_activity

notes_bp = Blueprint('notes', __name__)

@notes_bp.route('/notes', methods=['GET'])
@login_required
def list_notes():
    user_id = session['user_id']
    query = Note.query.filter_by(user_id=user_id)
    
    search = request.args.get('search', '')
    category = request.args.get('category', '')
    
    if search:
        query = query.filter(Note.title.like(f'%{search}%') | Note.content.like(f'%{search}%'))
    if category:
        query = query.filter_by(category=category)
        
    notes = query.order_by(Note.date_updated.desc()).all()
