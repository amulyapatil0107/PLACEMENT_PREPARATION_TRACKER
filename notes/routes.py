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
    categories = ['OOP', 'DBMS', 'Operating Systems', 'Computer Networks', 'HR Questions', 'General']
    
    return render_template('notes.html', notes=notes, categories=categories, search=search, category=category)

@notes_bp.route('/notes/add', methods=['POST'])
@login_required
def add_note():
    user_id = session['user_id']
    title = request.form.get('title')
    content = request.form.get('content')
    category = request.form.get('category')
    
    note = Note(user_id=user_id, title=title, content=content, category=category)
    db.session.add(note)
    db.session.commit()
    
    log_activity(user_id, 'Note Created', f'Created note: {title}')
    flash('Note created successfully!', 'success')
    return redirect(url_for('notes.list_notes'))

@notes_bp.route('/notes/edit/<int:id>', methods=['POST'])
@login_required
def edit_note(id):
    user_id = session['user_id']
    note = Note.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    note.title = request.form.get('title')
    note.content = request.form.get('content')
    note.category = request.form.get('category')
    
    db.session.commit()
    log_activity(user_id, 'Note Edit', f'Edited note: {note.title}')
    flash('Note updated successfully!', 'success')
    return redirect(url_for('notes.list_notes'))

@notes_bp.route('/notes/delete/<int:id>', methods=['POST'])
@login_required
def delete_note(id):
    user_id = session['user_id']
    note = Note.query.filter_by(id=id, user_id=user_id).first_or_404()
    db.session.delete(note)
    db.session.commit()
    log_activity(user_id, 'Note Delete', f'Deleted note: {note.title}')
    flash('Note deleted successfully!', 'info')
    return redirect(url_for('notes.list_notes'))

# Tweak: Add search query filter in notes list controller

# Tweak: Add category filter in notes list controller

# Tweak: Add categories array in list notes route

# Tweak: Log note creation activities

# Tweak: Log note edit activities

# Tweak: Log note delete activities

# Tweak: Add description field character clamps

# Tweak: Add read full note modal in notes.html

# Tweak: Add edit note modal template in notes.html

# Tweak: Add categories badges styles

# Tweak: Add write note toggleable container form

# Tweak: Tweak search placeholder texts inside notes.html

# Tweak: Format notes/routes.py formatting

# Tweak: Optimize DB session commit statements

# Tweak: Fix content word wrap styles on notes cards

# Tweak: Add empty state card inside notes.html

# Tweak: Verify notes edit parameters values

# Tweak: Add tooltip styling to notes cards

# Tweak: Tweak note updated date formatting

# Tweak: Import log activity in notes blueprint

# Tweak: Remove reduntant import statements in notes blueprint

# Tweak: Tweak category selection default options

# Tweak: Add confirmation box on notes deletes

# Tweak: Tweak card background colors in notes.html

# Tweak: Improve notes grid responsive flex widths

# Tweak: Optimize note titles character limits

# Tweak: Format notes routing scripts

# Tweak: Add search query filter in notes list controller

# Tweak: Add category filter in notes list controller

# Tweak: Add categories array in list notes route

# Tweak: Log note creation activities

# Tweak: Log note edit activities

# Tweak: Log note delete activities

# Tweak: Add description field character clamps

# Tweak: Add read full note modal in notes.html

# Tweak: Add edit note modal template in notes.html

# Tweak: Add categories badges styles

# Tweak: Add write note toggleable container form

# Tweak: Tweak search placeholder texts inside notes.html

# Tweak: Format notes/routes.py formatting

# Tweak: Optimize DB session commit statements

# Tweak: Fix content word wrap styles on notes cards

# Tweak: Add empty state card inside notes.html

# Tweak: Verify notes edit parameters values

# Tweak: Add tooltip styling to notes cards

# Tweak: Tweak note updated date formatting

# Tweak: Import log activity in notes blueprint

# Tweak: Remove reduntant import statements in notes blueprint

# Tweak: Tweak category selection default options

# Tweak: Add confirmation box on notes deletes

# Tweak: Tweak card background colors in notes.html

# Tweak: Improve notes grid responsive flex widths

# Tweak: Optimize note titles character limits

# Tweak: Format notes routing scripts

# Tweak: Add search query filter in notes list controller

# Tweak: Add category filter in notes list controller

# Tweak: Add categories array in list notes route

# Tweak: Log note creation activities

# Tweak: Log note edit activities

# Tweak: Log note delete activities

# Tweak: Add description field character clamps

# Tweak: Add read full note modal in notes.html

# Tweak: Add edit note modal template in notes.html

# Tweak: Add categories badges styles

# Tweak: Add write note toggleable container form

# Tweak: Tweak search placeholder texts inside notes.html

# Tweak: Format notes/routes.py formatting

# Tweak: Optimize DB session commit statements

# Tweak: Fix content word wrap styles on notes cards

# Tweak: Add empty state card inside notes.html

# Tweak: Verify notes edit parameters values

# Tweak: Add tooltip styling to notes cards

# Tweak: Tweak note updated date formatting

# Tweak: Import log activity in notes blueprint

# Tweak: Remove reduntant import statements in notes blueprint

# Tweak: Tweak category selection default options

# Tweak: Add confirmation box on notes deletes

# Tweak: Tweak card background colors in notes.html

# Tweak: Improve notes grid responsive flex widths

# Tweak: Optimize note titles character limits

# Tweak: Format notes routing scripts
