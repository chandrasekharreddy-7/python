# Python Projects and Practice

A growing collection of Python exercises and small applications created while learning core programming, object-oriented design, and backend development.

## Highlights

- Python fundamentals and problem-solving exercises
- Object-oriented programming examples, including inheritance and method overriding
- A demo **online voting system** built with Flask and SQLite
- Password hashing, sessions, role-based routes, registration, voting, and result display

## Technologies

- Python
- Flask
- SQLite
- Werkzeug security helpers
- HTML and CSS rendered through Flask templates

## Online Voting Demo

The voting application demonstrates:

- Voter registration with generated voter IDs
- Secure password hashing
- User and administrator login flows
- Candidate management
- One-vote-per-user application logic
- Result calculation and display

> This is an educational demo and is not intended for real elections or production use.

## Run Locally

```bash
python -m venv .venv
```

Activate the environment and install Flask:

```bash
pip install flask
```

Run the required Python file:

```bash
python <filename>.py
```

Then open the local URL shown in the terminal.

## Learning Goals

- Write clean and reusable Python code
- Strengthen OOP concepts
- Build database-backed web applications
- Improve validation, security, testing, and project structure

## Future Improvements

- Separate Flask routes, templates, and database services
- Add automated tests
- Use environment variables for all secrets
- Add stronger input validation and CSRF protection
- Replace demo credentials before any deployment