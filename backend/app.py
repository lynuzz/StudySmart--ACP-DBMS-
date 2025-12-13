from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from models import db, User, Task
import os

app = Flask(__name__)
app.secret_key = "studysmart_secret_key"

# Database setup
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   

#db = SQLAlchemy()
db.init_app(app)


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for('register'))
        new_user = User(username=username, password=password, email=email) 
        db.session.add(new_user)
        db.session.commit()
        flash("Account created! Please login.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    tasks = Task.query.filter_by(user_id=session['user_id']).all()
    total_tasks = len(tasks)
    completed_tasks = len([t for t in tasks if t.status == "Completed"])
    return render_template('dashboard.html', tasks=tasks, total=total_tasks, completed=completed_tasks)

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        subject = request.form['subject']
        deadline = datetime.strptime(request.form['deadline'], "%Y-%m-%dT%H:%M")
        new_task = Task(title=title, subject=subject, deadline=deadline, user_id=session['user_id'])
        db.session.add(new_task)
        db.session.commit()
        flash("Task added successfully!")
        return redirect(url_for('dashboard'))
    return render_template('add_task.html')

@app.route('/edit_task/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if 'user_id' not in session or task.user_id != session['user_id']:
        return redirect(url_for('login'))
    if request.method == 'POST':
        task.title = request.form['title']
        task.subject = request.form['subject']
        task.deadline = datetime.strptime(request.form['deadline'], "%Y-%m-%dT%H:%M")
        task.status = request.form['status']
        db.session.commit()
        flash("Task updated successfully!")
        return redirect(url_for('dashboard'))
    return render_template('edit_task.html', task=task)

@app.route('/delete_task/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    if 'user_id' not in session or task.user_id != session['user_id']:
        return redirect(url_for('login'))
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!")
    return redirect(url_for('dashboard'))

# Initialize database and run server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)