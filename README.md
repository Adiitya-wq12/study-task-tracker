# StudyTask — Flask study task tracker

A small web application for students to record study tasks, assign subjects and due dates, mark tasks complete, and remove them. Built as an individual SaaS/PaaS demonstration project.

## Run locally

```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000/. The application creates `tasks.db` automatically. This database file is excluded from Git.

## Deploy with Render

1. Create your own public or private GitHub repository and upload the files in this folder, with `app.py` at the repository root.
2. In Render, select **New > Web Service**, connect GitHub, and select that repository.
3. Select **Python** if asked. Set build command to `pip install -r requirements.txt` and start command to `gunicorn app:app`. Alternatively, use the included `render.yaml` blueprint.
4. Deploy; open the resulting `https://...onrender.com` URL and add and complete a test task.
5. Change the heading in `templates/index.html`, commit and push to GitHub, and watch the new deployment on Render. Refresh the public URL to show the change.

**Storage limitation:** The sample uses a local SQLite file. Render instances may use an ephemeral filesystem, so tasks can disappear on restart or redeployment. For lasting multiuser data, replace SQLite with a managed PostgreSQL service and add authentication. Do not enter sensitive personal information in a public demo.

## Files and concepts

- `app.py`: Flask routes and database operations; parameterized SQL queries.
- `templates/index.html`: web page rendered by Flask.
- `static/style.css`: responsive styling.
- `requirements.txt`: Python packages installed locally and in the cloud.
- `render.yaml`: optional PaaS configuration.
- `gunicorn app:app`: production server loads the Flask application named `app` in `app.py`.
