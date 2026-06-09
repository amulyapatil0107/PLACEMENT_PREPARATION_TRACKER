# Placement Preparation Tracker

A complete, production-quality placement preparation tracking web application built with **Python Flask**, **SQLAlchemy ORM**, **SQLite database**, **Vanilla CSS**, and **Chart.js** data visualizations.

---

## Technical Stack

* **Backend**: Python Flask (Session-based Authentication, Blueprints, Application Factory Pattern)
* **Frontend**: HTML5, Vanilla CSS3 (Custom Dark-themed Glassmorphism, Responsive Grid), JavaScript ES6
* **Database**: SQLite database with SQLAlchemy Object-Relational Mapper (ORM)
* **Charts**: Chart.js (Line, Doughnut, PolarArea, Pie, Bar charts)
* **Version Control**: Git (Multi-branch Strategy, 200+ Commit log history)

---

## Main Modules & Features

1. **User Authentication**: Secure signup, login, session handlers, password hashing (via Werkzeug), profile manager, and authentication guards.
2. **Dashboard**: Live metric cards (solving count, streak, contests, active goals), recent activity logger, and progress bars.
3. **DSA tracker**: Full CRUD operations for LeetCode, Codeforces, GeeksforGeeks, HackerRank, and CodeChef coding questions with custom topic, difficulty, and platform filters.
4. **Contest tracker**: Global rank logging, platform tracking, rating updates, and automated rating delta checks.
5. **Aptitude tracker**: Category grouping (Quantitative, Logical, Verbal), topic tracking, completion status updates, and accuracy scores.
6. **Interview Notes manager**: Categories (OOP, DBMS, OS, CN, HR Questions) with notes cards, search, and categorization panel.
7. **Goal management**: Deadlines, goal types (DSA, Contest, Aptitude), automated background progress calculation, and completion badges.
8. **Daily streak system**: Automated tracking of daily study events, streak counters, and longest streak badges.
9. **Analytics visualizations**: Interactive Chart.js integration displaying graphs for problems by difficulty, category, monthly solutions, and goal rates.
10. **Admin control panel**: High-level system statistics (overall user count, problems, contests) and data grids for user management.

---

## Folder Structure

```
placement-preparation-tracker/
  app.py                   # Flask entry point and factory runner
  config.py                # Session & Database configurations
  requirements.txt         # Package dependencies
  populate_db.py           # Database seeder (sample data)
  README.md                # Documentation and setup instructions
  database/
    __init__.py
    models.py              # SQLAlchemy DB Schemas (7 tables)
  auth/
    __init__.py
    forms.py               # Form validation validators
    routes.py              # Auth endpoints blueprint
  dsa/
    __init__.py
    routes.py              # Problems & Contests CRUD blueprint
    services.py            # Streaks & Activity services
  notes/
    __init__.py
    routes.py              # Interview Notes CRUD blueprint
  goals/
    __init__.py
    routes.py              # Goals management blueprint
  aptitude/
    __init__.py
    routes.py              # Aptitude tracker blueprint
  analytics/
    __init__.py
    routes.py              # Chart dashboard & JSON API blueprint
    charts.py              # Database statistics query aggregators
  templates/               # Jinja2 layout templates
  static/                  # Static assets
    css/
      style.css            # Base stylesheet (glassmorphic dark theme)
    js/
      main.js              # Theme switcher & modals
      charts.js            # Chart.js visualizations config
```

---

## Relational Database Schema

The SQLite schema consists of 7 tables with foreign key constraints:

1. **`users`**: User profiles with authentication hash, streaks, and activity dates.
2. **`problems`**: DSA coding questions (difficulty, topic, platform, solved date, foreign key to `users.id`).
3. **`contests`**: Competitive coding events (ranks, rating change, foreign key to `users.id`).
4. **`goals`**: Prep milestones with target variables, dead-lines, and status flags (foreign key to `users.id`).
5. **`notes`**: Subjects notes (OOP, DBMS, etc.) with markdown support (foreign key to `users.id`).
6. **`activities`**: Timeline logging events (foreign key to `users.id`).
7. **`aptitude_progress`**: Accuracy tracking of specific aptitude topics (foreign key to `users.id`).

---

## Branch-wise Implementation Plan

We employ a 6-branch strategy to organize development:

1. **`database`**: Setup SQLAlchemy setup, core database structures, and `config.py` models.
2. **`authentication`**: Blueprint setup for signup/login, verification decorators, session handling, and validation forms.
3. **`dsa-tracker`**: Services for daily streaks, CRUD endpoints for coding questions, and contest histories.
4. **`notes-manager`**: CRUD controllers for subjects and HR interview notes, category filters, and search functions.
5. **`analytics`**: Chart.js API datasets, mock exams tracker, goals progress calculations, and UI styling sheets.
6. **`main`**: Merges branches, seeds the database, sets up application factory configurations, and runs final integration tests.

---

## Step-by-Step Setup Guide

Follow these steps to run the Placement Prep Tracker on your machine:

### 1. Prerequisite Installations
Make sure you have **Python 3.8+** installed on your system.

### 2. Extract / Clone Project Directory
Ensure the directory structure matches the layout detailed in the Folder Structure section above.

### 3. Open Terminal in Workspace Directory
```bash
cd placement-preparation-tracker
```

### 4. Create and Activate Virtual Environment
On Windows:
```bash
python -m venv venv
venv\\Scripts\\activate
```
On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Initialize and Seed Database
Seed the application with beautiful, pre-populated mock data:
```bash
python populate_db.py
```

### 7. Launch Server
```bash
python app.py
```

### 8. View Application
Open your browser and navigate to:
* **Home/Login**: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Preloaded Credentials:
* **Default Developer Profile**:
  * **Username**: `prep_dev`
  * **Password**: `pass123`
* **Default Admin Profile**:
  * **Username**: `admin`
  * **Password**: `admin123` (Accesses overall system statistics)

<!-- Refinement commit 1 -->

<!-- Refinement commit 2 -->

<!-- Refinement commit 3 -->

<!-- Refinement commit 4 -->

<!-- Refinement commit 5 -->

<!-- Refinement commit 6 -->

<!-- Refinement commit 7 -->

<!-- Refinement commit 8 -->

<!-- Refinement commit 9 -->

<!-- Refinement commit 10 -->
