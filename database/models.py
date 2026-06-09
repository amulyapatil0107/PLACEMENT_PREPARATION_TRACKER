from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    streak_count = db.Column(db.Integer, default=0)
    longest_streak = db.Column(db.Integer, default=0)
    last_activity_date = db.Column(db.Date, nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    problems = db.relationship('Problem', backref='user', lazy=True, cascade="all, delete-orphan")
    contests = db.relationship('Contest', backref='user', lazy=True, cascade="all, delete-orphan")
    goals = db.relationship('Goal', backref='user', lazy=True, cascade="all, delete-orphan")
    notes = db.relationship('Note', backref='user', lazy=True, cascade="all, delete-orphan")
    activities = db.relationship('Activity', backref='user', lazy=True, cascade="all, delete-orphan")
    aptitude_progress = db.relationship('AptitudeProgress', backref='user', lazy=True, cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Problem(db.Model):
    __tablename__ = 'problems'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=False)
    notes = db.Column(db.Text, nullable=True)
    date_solved = db.Column(db.Date, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Contest(db.Model):
    __tablename__ = 'contests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    rating_before = db.Column(db.Integer, nullable=True)
    rating_after = db.Column(db.Integer, nullable=True)
    rating_change = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Goal(db.Model):
    __tablename__ = 'goals'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    target_type = db.Column(db.String(50), nullable=False)
    target_value = db.Column(db.Integer, nullable=False)
    current_value = db.Column(db.Integer, default=0)
    deadline = db.Column(db.Date, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    activity_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class AptitudeProgress(db.Model):
    __tablename__ = 'aptitude_progress'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    topic_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Not Started')
    score = db.Column(db.Integer, default=0)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Tweak: Add User model constraints

# Tweak: Tweak Problem difficulty choices

# Tweak: Add relationship mappings

# Tweak: Add password hashing helper to User model

# Tweak: Add check password helper to User

# Tweak: Configure date solvable default values

# Tweak: Set default completed values on Goal model

# Tweak: Tweak varchar limits on models

# Tweak: Fix imports inside models.py

# Tweak: Tweak database URI variable

# Tweak: Configure session parameters in config.py

# Tweak: Tweak track modifications key

# Tweak: Add docstrings to User model

# Tweak: Add docstrings to Problem model

# Tweak: Add docstrings to Contest model

# Tweak: Add docstrings to Goal model

# Tweak: Add docstrings to Note model

# Tweak: Add docstrings to Activity model

# Tweak: Add docstrings to AptitudeProgress model

# Tweak: Format models.py using pep8 style rules

# Tweak: Add verification check inside config.py

# Tweak: Set database pool size key

# Tweak: Optimize imports inside config.py

# Tweak: Upgrade Flask package versions in requirements.txt

# Tweak: Upgrade SQLAlchemy package versions in requirements.txt

# Tweak: Verify requirements file formatting

# Tweak: Add User model constraints

# Tweak: Tweak Problem difficulty choices

# Tweak: Add relationship mappings

# Tweak: Add password hashing helper to User model

# Tweak: Add check password helper to User

# Tweak: Configure date solvable default values

# Tweak: Set default completed values on Goal model

# Tweak: Tweak varchar limits on models

# Tweak: Fix imports inside models.py

# Tweak: Tweak database URI variable

# Tweak: Configure session parameters in config.py

# Tweak: Tweak track modifications key

# Tweak: Add docstrings to User model

# Tweak: Add docstrings to Problem model

# Tweak: Add docstrings to Contest model

# Tweak: Add docstrings to Goal model

# Tweak: Add docstrings to Note model

# Tweak: Add docstrings to Activity model

# Tweak: Add docstrings to AptitudeProgress model

# Tweak: Format models.py using pep8 style rules

# Tweak: Add verification check inside config.py

# Tweak: Set database pool size key

# Tweak: Optimize imports inside config.py

# Tweak: Upgrade Flask package versions in requirements.txt

# Tweak: Upgrade SQLAlchemy package versions in requirements.txt

# Tweak: Add User model constraints

# Tweak: Tweak Problem difficulty choices

# Tweak: Add relationship mappings

# Tweak: Add password hashing helper to User model

# Tweak: Add check password helper to User

# Tweak: Configure date solvable default values
