# Placement Prep Tracker

Hey! This is a personal web application I built to track my placement preparation journey. It helps me organize everything in one place—DSA questions, contest performance, core CS subject notes, goals, and aptitude progress.

I built this because tracking preparation across LeetCode, Codeforces, and local notebooks was getting messy. This app provides a unified dashboard and tracks my daily coding streak to keep me motivated!

---

## Tech Stack I Used

* **Backend**: Python Flask (using Blueprints for modularity and sessions for user auth)
* **Frontend**: HTML5, Vanilla CSS3 (glassmorphic dark theme, fully responsive), and JavaScript ES6
* **Database**: SQLite with SQLAlchemy ORM (7 tables for users, problems, contests, etc.)
* **Visualizations**: Chart.js (to see graphs of my solved problems by difficulty, category, and goal completion rates)

---

## Key Modules & Features

1. **Dashboard**: Shows my progress summary cards (total problems solved, active streak, contests attended, and active goals), recent activities, and progress bars.
2. **DSA Tracker**: Log coding questions from LeetCode, GFG, HackerRank, CodeChef, and Codeforces. I can filter them by topic, difficulty, and platform, and search by name.
3. **Contest Logger**: Logs my ranks, rating changes, and delta improvements.
4. **Interview Notes**: A handy notebook for core subjects like OOP, DBMS, Operating Systems, Computer Networks, and HR questions with search and category tags.
5. **Goal Board**: Lets me set milestones (e.g. "Solve 50 Tree problems") with deadlines. The app automatically updates their progress.
6. **Daily Streaks**: Keeps track of my daily activity and shows my current coding streak.
7. **Analytics**: Visual graphs (powered by Chart.js) showing solved problems by difficulty, category, and month.
8. **Admin Dashboard**: A special panel to view system-wide stats.

---

## Folder Structure

Here is how I organized the code:
```text
placement-preparation-tracker/
  ├── app.py              # Main entry point (app factory)
  ├── config.py           # Configuration (db path, secret key)
  ├── requirements.txt    # Required python packages
  ├── populate_db.py      # Script to seed sample data for testing
  ├── README.md           # This file
  ├── database/
  │   ├── __init__.py
  │   └── models.py       # SQLAlchemy database models
  ├── auth/
  │   ├── __init__.py
  │   ├── forms.py        # Validation forms
  │   └── routes.py       # Registration, login, logout, profile routes
  ├── dsa/
  │   ├── __init__.py
  │   ├── routes.py       # DSA problems and contests routes
  │   └── services.py     # Streak calculation logic
  ├── notes/
  │   ├── __init__.py
  │   └── routes.py       # Notes management routes
  ├── goals/
  │   ├── __init__.py
  │   └── routes.py       # Milestones tracking routes
  ├── aptitude/
  │   ├── __init__.py
  │   └── routes.py       # Aptitude syllabus routes
  ├── analytics/
  │   ├── __init__.py
  │   ├── routes.py       # Analytics dashboard routes
  │   └── charts.py       # Query helpers for charts data
  ├── templates/          # Jinja2 HTML layouts
  └── static/
      ├── css/
      │   └── style.css   # Main styles (dark glassmorphic theme)
      └── js/
          ├── main.js     # Modals, toasts, theme toggler script
          └── charts.js   # Chart.js rendering script
```

---

## Database Design

I designed a relational schema using SQLite:
1. `User`: User profiles, password hashes, and streak details.
2. `Problem`: Logged DSA coding questions (platform, difficulty, topic).
3. `Contest`: Logs for contest ranks and ratings.
4. `Goal`: Milestones with target metrics and deadlines.
5. `Note`: Personal subject notes (DBMS, OOP, OS, CN).
6. `ActivityLog`: Log of recent user actions.
7. `AptitudeTopic`: Completion checklist for aptitude modules.

---

## Git Development Branches

I worked on this project using a structured branch strategy:
* `database`: Configured SQLAlchemy and models.
* `authentication`: Added signup, login, session guard decorators, and profile pages.
* `dsa-tracker`: Added CRUD endpoints for coding questions and contests.
* `notes-manager`: Built notes, goals, and aptitude checklist endpoints.
* `analytics`: Configured Chart.js data API and CSS themes.
* `main`: Consolidated all features and tested integration.

---

## How to Run This Project on Your System

Follow these simple steps to set up and run the tracker locally:

### 1. Install Python
Ensure you have **Python 3.8+** installed.

### 2. Open your terminal in the project directory
```bash
cd placement-preparation-tracker
```

### 3. Create a Virtual Environment and Activate it
* **Windows (Command Prompt / PowerShell)**:
  ```cmd
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 4. Install all required packages
```bash
pip install -r requirements.txt
```

### 5. Seed the database with sample data
I wrote a seeder script to populate the database with realistic sample problems, notes, and contest entries so you don't have to start from scratch:
```bash
python populate_db.py
```

### 6. Run the Flask application
```bash
python app.py
```

### 7. Open in your browser
Go to **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** to view the app!

### Seeded Test Accounts:
I pre-populated two accounts for testing:
* **Developer Account**:
  * **Username**: `prep_dev`
  * **Password**: `pass123`
* **Admin Account**:
  * **Username**: `admin`
  * **Password**: `admin123` (Accesses system-wide overview statistics)
