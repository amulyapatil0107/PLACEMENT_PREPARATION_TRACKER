import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-placement-prep-tracker-12345'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///placement_prep.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

