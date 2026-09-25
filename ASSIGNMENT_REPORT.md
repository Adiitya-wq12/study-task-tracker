# Assignment report: StudyTask

**Student name:** Aditya Sudhir

**GitHub repository:** https://github.com/Adiitya-wq12/study-task-tracker

**Deployed application:** https://study-task-tracker-3jal.onrender.com/

## Description and problem

Students often track assignments and revision across multiple subjects in scattered notes. StudyTask provides one browser page for entering a task, its subject, and an optional due date, and for tracking completion. It is a small demonstration application rather than a full learning management system.

## Target users and objectives

The target users are students managing their own study tasks. The objectives are to record tasks, show upcoming work, identify overdue tasks, update completion, and remove tasks. The page also shows a completed/total count.

## Features and workflow

1. Open the home page to view tasks and progress.
2. Enter a task title, subject, and optional due date, then select **Add task**.
3. Select **Complete** or **Undo** to change its status.
4. Select **Delete** to remove a task.
5. Tasks appear with incomplete ones first; tasks with due dates are ordered by date. An overdue label appears after the due date.

The HTML form sends a POST request to Flask. Flask validates the input and runs a parameterized SQLite query, then redirects to the home page. The home page reads records and renders them in a Jinja template.

## Technologies and roles

| Technology | Role |
| --- | --- |
| Python | Implements application logic and SQLite access. |
| Flask | Handles URLs, form submissions, templates, and HTTP responses. |
| SQLite | Stores demonstration tasks in a local database file. |
| HTML/CSS | Presents a responsive browser interface. |
| GitHub | Hosts the source repository and its change history. |
| Gunicorn | Runs the Flask app as a production web server. |
| Render (PaaS) | Installs dependencies and runs the web service on managed infrastructure. |
| Public URL | Gives users a web address to reach the deployed service. |

## Development, local demonstration, and deployment

Run the commands in `README.md`, open `http://127.0.0.1:5000/`, and demonstrate add, complete, undo, and delete. Capture screenshots of the empty form, an added task, and the updated count. Upload the project to a new GitHub repository. Create a Render Web Service linked to that repository. Configure the build command `pip install -r requirements.txt` and start command `gunicorn app:app`, then deploy. Capture screenshots of the configuration, successful deploy, and working public page. Copy the actual repository and public links into the fields at the top of this report.

For automatic redeployment, change the heading text in `templates/index.html`, commit and push. Check that Render begins a new deploy, then refresh the public URL and capture the updated heading. If automatic deployment is disabled in the Render service settings, enable it before this step.

## How it demonstrates SaaS and PaaS

Users access the running application through a browser using the public URL; they do not install Python or Flask. This browser-delivered application demonstrates the basic SaaS delivery model. Render is the PaaS: it builds and hosts the Python process, supplies the runtime and public endpoint, and deploys changes from GitHub. The code and user interface are the student's responsibility, while the platform handles hosting operations.

## Results and limitations

**Results:** [After testing, record the features you demonstrated and paste screenshot references.]  
**Conclusion:** StudyTask shows the path from a real user need through Flask development and local testing to repository upload and PaaS hosting.  
**Limitation:** SQLite stored on a Render instance may be lost after a restart or deploy. This demo has no user accounts; everyone using the same public service can see and change its tasks. Production use requires authentication and a persistent managed database.

## Short viva prompts

- **Why use POST for changes?** Adding, toggling, and deleting modify data; GET is reserved here for viewing the page.
- **What is `app:app`?** The first `app` is the Python module `app.py`; the second is its Flask object.
- **What happens after a form submission?** Flask validates input, updates SQLite, and redirects to the home page.
- **What is SaaS here?** Users access the application as an online service through a browser.
- **What is PaaS here?** Render supplies and operates the hosting environment for the Python web application.
- **How does a code change reach users?** A commit pushed to connected GitHub triggers a new Render build and deployment when auto deploy is enabled.
