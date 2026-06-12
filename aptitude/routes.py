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
