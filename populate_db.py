import os
from datetime import datetime, date, timedelta
from app import create_app
from database.models import db, User, Problem, Contest, Goal, Note, Activity, AptitudeProgress

def populate():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        user1 = User(username='prep_dev', email='dev@placementprep.com', is_admin=False)
        user1.set_password('pass123')
        
        admin = User(username='admin', email='admin@placementprep.com', is_admin=True)
        admin.set_password('admin123')
        
        db.session.add(user1)
        db.session.add(admin)
        db.session.commit()
        
        problems = [
            Problem(user_id=user1.id, name='Two Sum', topic='Arrays', difficulty='Easy', platform='LeetCode', status=True, notes='Used HashMap for O(N) complexity.', date_solved=date.today() - timedelta(days=5)),
            Problem(user_id=user1.id, name='Longest Substring Without Repeating Characters', topic='String', difficulty='Medium', platform='LeetCode', status=True, notes='Sliding window technique.', date_solved=date.today() - timedelta(days=4)),
            Problem(user_id=user1.id, name='Merge k Sorted Lists', topic='Heaps', difficulty='Hard', platform='LeetCode', status=False, notes='Need to use a min-heap.', date_solved=None),
            Problem(user_id=user1.id, name='Detect Cycle in a Directed Graph', topic='Graphs', difficulty='Medium', platform='GeeksforGeeks', status=True, notes='DFS classification with back edges.', date_solved=date.today() - timedelta(days=3)),
            Problem(user_id=user1.id, name='Subset Sum Problem', topic='Dynamic Programming', difficulty='Medium', platform='GeeksforGeeks', status=True, notes='Tabulation approach similar to Knapsack.', date_solved=date.today() - timedelta(days=2)),
            Problem(user_id=user1.id, name='Beautiful Towers I', topic='Monotonic Stack', difficulty='Medium', platform='LeetCode', status=True, notes='Find heights sum with peak elements.', date_solved=date.today() - timedelta(days=1)),
            Problem(user_id=user1.id, name='Water Container', topic='Two Pointers', difficulty='Medium', platform='LeetCode', status=True, notes='Shrink boundaries from left and right.', date_solved=date.today()),
            Problem(user_id=user1.id, name='Binary Tree Inorder Traversal', topic='Trees', difficulty='Easy', platform='LeetCode', status=True, notes='Recursive left-root-right traversal.', date_solved=date.today() - timedelta(days=6)),
            Problem(user_id=user1.id, name='Sudoku Solver', topic='Backtracking', difficulty='Hard', platform='LeetCode', status=False, notes='Recursive backtracking.', date_solved=None)
        ]
        db.session.add_all(problems)
        
        contests = [
            Contest(user_id=user1.id, name='LeetCode Weekly Contest 370', platform='LeetCode', date=date.today() - timedelta(days=15), rank=1850, rating_before=1500, rating_after=1545, rating_change=45),
            Contest(user_id=user1.id, name='Codeforces Round 900 (Div. 3)', platform='Codeforces', date=date.today() - timedelta(days=8), rank=1200, rating_before=1150, rating_after=1220, rating_change=70),
            Contest(user_id=user1.id, name='LeetCode Biweekly Contest 115', platform='LeetCode', date=date.today() - timedelta(days=3), rank=2400, rating_before=1545, rating_after=1530, rating_change=-15)
        ]
        db.session.add_all(contests)
        
        goals = [
            Goal(user_id=user1.id, description='Solve 150 DSA Problems', target_type='DSA', target_value=150, current_value=7, deadline=date.today() + timedelta(days=30), is_completed=False),
            Goal(user_id=user1.id, description='Participate in 10 Contests', target_type='Contest', target_value=10, current_value=3, deadline=date.today() + timedelta(days=60), is_completed=False),
            Goal(user_id=user1.id, description='Complete Quantitative Aptitude revision', target_type='Aptitude', target_value=7, current_value=1, deadline=date.today() + timedelta(days=15), is_completed=False),
            Goal(user_id=user1.id, description='Revise OOP Concepts', target_type='General', target_value=1, current_value=1, deadline=date.today() - timedelta(days=1), is_completed=True)
        ]
        db.session.add_all(goals)
        
        notes = [
            Note(user_id=user1.id, title='Four Pillars of OOP', category='OOP', content='1. Encapsulation: Hiding internal details and exposing only what is necessary using access specifiers.\\n2. Inheritance: Code reusability mechanism where child class inherits parent properties.\\n3. Polymorphism: Ability to take multiple forms (Compile-time: Overloading; Run-time: Overriding).\\n4. Abstraction: Hiding implementation details using interfaces and abstract classes.'),
            Note(user_id=user1.id, title='ACID Properties in DBMS', category='DBMS', content='Atomicity: All operations in a transaction complete successfully, or none do.\\nConsistency: Database transitions from one valid state to another, maintaining constraints.\\nIsolation: Transactions execute concurrently without interfering with each other.\\nDurability: Once committed, changes survive system failures.'),
            Note(user_id=user1.id, title='Process vs Thread', category='Operating Systems', content='Process: A program in execution. Independent execution unit with its own address space, memory, heap, and file descriptors. High context switch overhead.\\nThread: A subset of a process (lightweight process). Shares memory space, code section, and data section with sibling threads, but has its own stack and registers. Fast context switching.'),
            Note(user_id=user1.id, title='OSI Model Layers', category='Computer Networks', content='7. Application Layer (HTTP, FTP)\\n6. Presentation Layer (SSL/TLS, JPEG)\\n5. Session Layer (Sockets, NetBIOS)\\n4. Transport Layer (TCP, UDP)\\n3. Network Layer (IP, ICMP)\\n2. Data Link Layer (Ethernet, MAC)\\n1. Physical Layer (Cables, Bits)'),
            Note(user_id=user1.id, title='Introduce Yourself Answers', category='HR Questions', content='Structure: Past, Present, Future.\\n- Start with brief summary of background and academic credentials (Past).\\n- Highlight your technical projects, coding achievements, and core skills (Present).\\n- Conclude by stating why you are excited about this role and how you fit the company (Future).')
        ]
        db.session.add_all(notes)
        
        aptitude_items = [
            AptitudeProgress(user_id=user1.id, category='Quantitative Aptitude', topic_name='Percentage', status='Completed', score=85),
            AptitudeProgress(user_id=user1.id, category='Quantitative Aptitude', topic_name='Profit & Loss', status='In Progress', score=0),
            AptitudeProgress(user_id=user1.id, category='Quantitative Aptitude', topic_name='Time & Work', status='Not Started', score=0),
            AptitudeProgress(user_id=user1.id, category='Logical Reasoning', topic_name='Number Series', status='Completed', score=90),
            AptitudeProgress(user_id=user1.id, category='Logical Reasoning', topic_name='Coding-Decoding', status='Completed', score=75),
            AptitudeProgress(user_id=user1.id, category='Logical Reasoning', topic_name='Blood Relations', status='Not Started', score=0),
            AptitudeProgress(user_id=user1.id, category='Verbal Ability', topic_name='Reading Comprehension', status='In Progress', score=0),
            AptitudeProgress(user_id=user1.id, category='Verbal Ability', topic_name='Sentence Correction', status='Not Started', score=0)
        ]
        db.session.add_all(aptitude_items)
        
        activities = [
            Activity(user_id=user1.id, activity_type='Register', description='User prep_dev registered.', timestamp=datetime.utcnow() - timedelta(days=6)),
            Activity(user_id=user1.id, activity_type='Goal Created', description='Created goal: Solve 150 DSA Problems', timestamp=datetime.utcnow() - timedelta(days=6)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Binary Tree Inorder Traversal', timestamp=datetime.utcnow() - timedelta(days=6)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Two Sum', timestamp=datetime.utcnow() - timedelta(days=5)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Longest Substring Without Repeating Characters', timestamp=datetime.utcnow() - timedelta(days=4)),
            Activity(user_id=user1.id, activity_type='Contest Attended', description='Participated in LeetCode Biweekly Contest 115', timestamp=datetime.utcnow() - timedelta(days=3)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Detect Cycle in a Directed Graph', timestamp=datetime.utcnow() - timedelta(days=3)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Subset Sum Problem', timestamp=datetime.utcnow() - timedelta(days=2)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Beautiful Towers I', timestamp=datetime.utcnow() - timedelta(days=1)),
            Activity(user_id=user1.id, activity_type='DSA Solved', description='Added problem: Water Container', timestamp=datetime.utcnow())
        ]
        db.session.add_all(activities)
        
        user1.streak_count = 5
        user1.longest_streak = 5
        user1.last_activity_date = date.today()
        
        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate()
