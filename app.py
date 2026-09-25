import os
import sqlite3
from contextlib import closing
from datetime import date
from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
DATABASE = os.environ.get('DATABASE_PATH', os.path.join(os.path.dirname(__file__), 'tasks.db'))


def connection():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def init_db():
    with closing(connection()) as db:
        db.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            due_date TEXT,
            completed INTEGER NOT NULL DEFAULT 0
        )''')
        db.commit()


@app.get('/')
def index():
    init_db()
    with closing(connection()) as db:
        tasks = db.execute('SELECT * FROM tasks ORDER BY completed, due_date IS NULL, due_date, id DESC').fetchall()
    total = len(tasks)
    done = sum(task['completed'] for task in tasks)
    return render_template('index.html', tasks=tasks, total=total, done=done, today=date.today().isoformat())


@app.post('/tasks')
def add_task():
    title = request.form.get('title', '').strip()
    subject = request.form.get('subject', '').strip()
    due_date = request.form.get('due_date', '').strip() or None
    if not title or not subject or len(title) > 120 or len(subject) > 60:
        abort(400, 'Enter a title (up to 120 characters) and subject (up to 60 characters).')
    if due_date:
        try:
            date.fromisoformat(due_date)
        except ValueError:
            abort(400, 'Invalid due date.')
    init_db()
    with closing(connection()) as db:
        db.execute('INSERT INTO tasks (title, subject, due_date) VALUES (?, ?, ?)', (title, subject, due_date))
        db.commit()
    return redirect(url_for('index'))


@app.post('/tasks/<int:task_id>/toggle')
def toggle_task(task_id):
    init_db()
    with closing(connection()) as db:
        cursor = db.execute('UPDATE tasks SET completed = 1 - completed WHERE id = ?', (task_id,))
        db.commit()
        if cursor.rowcount == 0:
            abort(404)
    return redirect(url_for('index'))


@app.post('/tasks/<int:task_id>/delete')
def delete_task(task_id):
    init_db()
    with closing(connection()) as db:
        cursor = db.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        db.commit()
        if cursor.rowcount == 0:
            abort(404)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
