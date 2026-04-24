from flask import Flask, request, redirect, url_for, session, flash, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import sqlite3
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")
DB_NAME = "online_voting.db"


# -----------------------------
# Database helpers
# -----------------------------
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def generate_voter_id(conn):
    """Generate unique voter ID like VOTER123456"""
    cur = conn.cursor()
    while True:
        voter_id = f"VOTER{random.randint(100000, 999999)}"
        cur.execute("SELECT id FROM users WHERE voter_id = ?", (voter_id,))
        existing = cur.fetchone()
        if not existing:
            return voter_id


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            voter_id TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin INTEGER NOT NULL DEFAULT 0,
            has_voted INTEGER NOT NULL DEFAULT 0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            party TEXT NOT NULL,
            votes INTEGER NOT NULL DEFAULT 0
        )
    """)

    # Create default admin if not exists
    cur.execute("SELECT id FROM users WHERE voter_id = ?", ("ADMIN001",))
    admin = cur.fetchone()

    if not admin:
        cur.execute("""
            INSERT INTO users (voter_id, name, email, password, is_admin, has_voted)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            "ADMIN001",
            "Administrator",
            "admin@vote.com",
            generate_password_hash("admin123"),
            1,
            0
        ))

    conn.commit()
    conn.close()


# -----------------------------
# Decorators
# -----------------------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.")
            return redirect(url_for("login"))
        if session.get("is_admin") != 1:
            flash("Admin access only.")
            return redirect(url_for("home"))
        return f(*args, **kwargs)
    return wrapper


# -----------------------------
# Shared HTML
# -----------------------------
BASE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
            background: #f1f5f9;
        }
        .navbar {
            background: #0f172a;
            color: white;
            padding: 14px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .navbar a {
            color: white;
            text-decoration: none;
            margin-left: 14px;
            font-weight: bold;
        }
        .container {
            width: 92%;
            max-width: 1000px;
            margin: 25px auto;
            background: white;
            border-radius: 14px;
            padding: 24px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
        }
        h1, h2, h3 {
            color: #0f172a;
        }
        input, button, select {
            width: 100%;
            padding: 11px;
            margin: 8px 0 14px 0;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            box-sizing: border-box;
            font-size: 14px;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #1d4ed8;
        }
        .card {
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 14px;
            background: #f8fafc;
        }
        .flash {
            background: #dbeafe;
            color: #1e3a8a;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 14px;
        }
        .success {
            background: #dcfce7;
            color: #166534;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 14px;
        }
        .danger {
            background: #fee2e2;
            color: #991b1b;
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 14px;
        }
        .small {
            font-size: 13px;
            color: #475569;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 12px;
        }
        th, td {
            border: 1px solid #e2e8f0;
            padding: 10px;
            text-align: left;
            font-size: 14px;
        }
        th {
            background: #e2e8f0;
        }
        .inline-btn {
            width: auto;
            padding: 8px 12px;
            display: inline-block;
        }
        .result-bar {
            width: 100%;
            background: #e2e8f0;
            border-radius: 8px;
            overflow: hidden;
            margin-top: 8px;
        }
        .result-fill {
            background: #2563eb;
            color: white;
            padding: 8px 0;
            text-align: center;
        }
        .voter-id-box {
            background: #ecfeff;
            color: #155e75;
            padding: 16px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            margin: 16px 0;
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div><strong>Online Voting System</strong></div>
        <div>
            <a href="{{ url_for('home') }}">Home</a>

            {% if session.get('user_id') %}
                {% if session.get('is_admin') == 1 %}
                    <a href="{{ url_for('admin_dashboard') }}">Admin</a>
                {% else %}
                    <a href="{{ url_for('vote') }}">Vote</a>
                {% endif %}
                <a href="{{ url_for('results') }}">Results</a>
                <a href="{{ url_for('logout') }}">Logout</a>
            {% else %}
                <a href="{{ url_for('register') }}">Register</a>
                <a href="{{ url_for('login') }}">Login</a>
                <a href="{{ url_for('results') }}">Results</a>
            {% endif %}
        </div>
    </div>

    <div class="container">
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for msg in messages %}
                    <div class="flash">{{ msg }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {{ body|safe }}
    </div>
</body>
</html>
"""


def render_page(title, body_template, **context):
    body_html = render_template_string(body_template, **context)
    return render_template_string(BASE_HTML, title=title, body=body_html)


# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    body = """
    <h1>Welcome to the Online Voting System</h1>
    <p>This project uses a unique <strong>Voter ID</strong> for every voter.</p>

    {% if session.get('user_id') %}
        <div class="card">
            <h3>Hello, {{ session.get('user_name') }}</h3>
            <p><strong>Your Voter ID:</strong> {{ session.get('voter_id') }}</p>

            {% if session.get('is_admin') == 1 %}
                <p>You are logged in as Admin.</p>
                <a href="{{ url_for('admin_dashboard') }}"><button>Go to Admin Dashboard</button></a>
            {% else %}
                <p>You are logged in as a voter.</p>
                <a href="{{ url_for('vote') }}"><button>Go to Voting Page</button></a>
            {% endif %}
        </div>
    {% else %}
        <div class="card">
            <h3>How it works</h3>
            <p>1. Register as a voter</p>
            <p>2. Get your Voter ID</p>
            <p>3. Login using Voter ID and password</p>
            <p>4. Cast your vote once</p>
            <a href="{{ url_for('register') }}"><button>Register Now</button></a>
        </div>
    {% endif %}

    <div class="card">
        <p class="small">
            This is a student/demo project. It should not be used for real public elections.
        </p>
    </div>
    """
    return render_page("Home", body)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not name or not email or not password:
            flash("All fields are required.")
            return redirect(url_for("register"))

        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT id FROM users WHERE email = ?", (email,))
        existing = cur.fetchone()
        if existing:
            conn.close()
            flash("Email already registered.")
            return redirect(url_for("register"))

        voter_id = generate_voter_id(conn)

        cur.execute("""
            INSERT INTO users (voter_id, name, email, password, is_admin, has_voted)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            voter_id,
            name,
            email,
            generate_password_hash(password),
            0,
            0
        ))

        conn.commit()
        conn.close()

        body = """
        <h2>Registration Successful</h2>
        <div class="success">Your account has been created successfully.</div>

        <p>Your generated Voter ID is:</p>
        <div class="voter-id-box">{{ voter_id }}</div>

        <p><strong>Please save this Voter ID.</strong> You will need it to login and vote.</p>
        <a href="{{ url_for('login') }}"><button>Go to Login</button></a>
        """
        return render_page("Registration Success", body, voter_id=voter_id)

    body = """
    <h2>Voter Registration</h2>
    <form method="POST">
        <label>Full Name</label>
        <input type="text" name="name" placeholder="Enter full name">

        <label>Email</label>
        <input type="email" name="email" placeholder="Enter email">

        <label>Password</label>
        <input type="password" name="password" placeholder="Create password">

        <button type="submit">Register</button>
    </form>
    """
    return render_page("Register", body)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        voter_id = request.form.get("voter_id", "").strip().upper()
        password = request.form.get("password", "").strip()

        conn = get_db()
        cur = conn.cursor()

        cur.execute("SELECT * FROM users WHERE voter_id = ?", (voter_id,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["voter_id"] = user["voter_id"]
            session["is_admin"] = user["is_admin"]

            flash("Login successful.")

            if user["is_admin"] == 1:
                return redirect(url_for("admin_dashboard"))
            return redirect(url_for("vote"))

        flash("Invalid Voter ID or password.")
        return redirect(url_for("login"))

    body = """
    <h2>Login</h2>
    <form method="POST">
        <label>Voter ID</label>
        <input type="text" name="voter_id" placeholder="Enter your Voter ID">

        <label>Password</label>
        <input type="password" name="password" placeholder="Enter password">

        <button type="submit">Login</button>
    </form>

    <div class="card">
        <p><strong>Admin Login</strong></p>
        <p>Voter ID: ADMIN001</p>
        <p>Password: admin123</p>
    </div>
    """
    return render_page("Login", body)


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully.")
    return redirect(url_for("home"))


@app.route("/vote", methods=["GET", "POST"])
@login_required
def vote():
    if session.get("is_admin") == 1:
        flash("Admin account cannot vote.")
        return redirect(url_for("admin_dashboard"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],))
    user = cur.fetchone()

    cur.execute("SELECT * FROM candidates ORDER BY id ASC")
    candidates = cur.fetchall()

    if request.method == "POST":
        if user["has_voted"] == 1:
            conn.close()
            flash("You have already voted.")
            return redirect(url_for("vote"))

        candidate_id = request.form.get("candidate_id")
        entered_voter_id = request.form.get("voter_id", "").strip().upper()

        if not candidate_id or not entered_voter_id:
            conn.close()
            flash("Please enter your Voter ID and select a candidate.")
            return redirect(url_for("vote"))

        if entered_voter_id != user["voter_id"]:
            conn.close()
            flash("Entered Voter ID does not match your account.")
            return redirect(url_for("vote"))

        cur.execute("SELECT * FROM candidates WHERE id = ?", (candidate_id,))
        candidate = cur.fetchone()

        if not candidate:
            conn.close()
            flash("Invalid candidate selected.")
            return redirect(url_for("vote"))

        cur.execute("UPDATE candidates SET votes = votes + 1 WHERE id = ?", (candidate_id,))
        cur.execute("UPDATE users SET has_voted = 1 WHERE id = ?", (session["user_id"],))
        conn.commit()
        conn.close()

        flash("Your vote has been submitted successfully.")
        return redirect(url_for("results"))

    conn.close()

    body = """
    <h2>Cast Your Vote</h2>
    <div class="card">
        <p><strong>Logged in as:</strong> {{ user["name"] }}</p>
        <p><strong>Your Voter ID:</strong> {{ user["voter_id"] }}</p>
    </div>

    {% if user["has_voted"] == 1 %}
        <div class="success">You have already voted. Thank you.</div>
        <a href="{{ url_for('results') }}"><button>View Results</button></a>
    {% else %}
        {% if candidates %}
            <form method="POST">
                <label>Confirm Your Voter ID</label>
                <input type="text" name="voter_id" placeholder="Re-enter your Voter ID to vote">

                <label>Select Candidate</label>
                {% for candidate in candidates %}
                    <div class="card">
                        <label style="display:flex; align-items:center; gap:10px;">
                            <input type="radio" name="candidate_id" value="{{ candidate['id'] }}" style="width:auto;">
                            <div>
                                <strong>{{ candidate["name"] }}</strong><br>
                                <span class="small">Party: {{ candidate["party"] }}</span>
                            </div>
                        </label>
                    </div>
                {% endfor %}
                <button type="submit">Submit Vote</button>
            </form>
        {% else %}
            <div class="danger">No candidates available yet.</div>
        {% endif %}
    {% endif %}
    """
    return render_page("Vote", body, user=user, candidates=candidates)


@app.route("/results")
def results():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM candidates ORDER BY votes DESC, id ASC")
    candidates = cur.fetchall()
    conn.close()

    total_votes = sum(c["votes"] for c in candidates)

    result_rows = []
    for c in candidates:
        percentage = 0
        if total_votes > 0:
            percentage = round((c["votes"] / total_votes) * 100, 2)

        result_rows.append({
            "name": c["name"],
            "party": c["party"],
            "votes": c["votes"],
            "percentage": percentage
        })

    body = """
    <h2>Election Results</h2>
    <p><strong>Total Votes Cast:</strong> {{ total_votes }}</p>

    {% if result_rows %}
        {% for row in result_rows %}
            <div class="card">
                <h3>{{ row["name"] }}</h3>
                <p>Party: {{ row["party"] }}</p>
                <p>Votes: <strong>{{ row["votes"] }}</strong></p>
                <p>Percentage: <strong>{{ row["percentage"] }}%</strong></p>
                <div class="result-bar">
                    <div class="result-fill" style="width: {{ row['percentage'] }}%;">
                        {{ row["percentage"] }}%
                    </div>
                </div>
            </div>
        {% endfor %}
    {% else %}
        <div class="card">No candidates found.</div>
    {% endif %}
    """
    return render_page("Results", body, result_rows=result_rows, total_votes=total_votes)


@app.route("/admin")
@admin_required
def admin_dashboard():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM candidates ORDER BY id ASC")
    candidates = cur.fetchall()

    cur.execute("SELECT * FROM users WHERE is_admin = 0 ORDER BY id DESC")
    voters = cur.fetchall()

    cur.execute("SELECT COUNT(*) AS total_voters FROM users WHERE is_admin = 0")
    total_voters = cur.fetchone()["total_voters"]

    cur.execute("SELECT COUNT(*) AS voted_count FROM users WHERE is_admin = 0 AND has_voted = 1")
    voted_count = cur.fetchone()["voted_count"]

    conn.close()

    body = """
    <h2>Admin Dashboard</h2>

    <div class="card">
        <p><strong>Total Voters:</strong> {{ total_voters }}</p>
        <p><strong>Already Voted:</strong> {{ voted_count }}</p>
        <p><strong>Not Yet Voted:</strong> {{ total_voters - voted_count }}</p>
    </div>

    <div class="card">
        <h3>Add Candidate</h3>
        <form method="POST" action="{{ url_for('add_candidate') }}">
            <label>Candidate Name</label>
            <input type="text" name="name" placeholder="Enter candidate name">

            <label>Party Name</label>
            <input type="text" name="party" placeholder="Enter party name">

            <button type="submit">Add Candidate</button>
        </form>
    </div>

    <div class="card">
        <h3>Add Voter</h3>
        <form method="POST" action="{{ url_for('add_voter') }}">
            <label>Voter ID (leave blank to auto-generate)</label>
            <input type="text" name="voter_id" placeholder="Optional custom voter ID">

            <label>Voter Name</label>
            <input type="text" name="name" placeholder="Enter voter name">

            <label>Email</label>
            <input type="email" name="email" placeholder="Enter voter email">

            <label>Password</label>
            <input type="password" name="password" placeholder="Set voter password">

            <button type="submit">Add Voter</button>
        </form>
    </div>

    <div class="card">
        <h3>Candidate List</h3>
        {% if candidates %}
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Party</th>
                    <th>Votes</th>
                    <th>Action</th>
                </tr>
                {% for c in candidates %}
                <tr>
                    <td>{{ c["id"] }}</td>
                    <td>{{ c["name"] }}</td>
                    <td>{{ c["party"] }}</td>
                    <td>{{ c["votes"] }}</td>
                    <td>
                        <a href="{{ url_for('delete_candidate', candidate_id=c['id']) }}">
                            <button class="inline-btn">Delete</button>
                        </a>
                    </td>
                </tr>
                {% endfor %}
            </table>
        {% else %}
            <p>No candidates added yet.</p>
        {% endif %}
    </div>

    <div class="card">
        <h3>Voter List</h3>
        {% if voters %}
            <table>
                <tr>
                    <th>Voter ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
                {% for v in voters %}
                <tr>
                    <td>{{ v["voter_id"] }}</td>
                    <td>{{ v["name"] }}</td>
                    <td>{{ v["email"] }}</td>
                    <td>
                        {% if v["has_voted"] == 1 %}
                            Voted
                        {% else %}
                            Not Voted
                        {% endif %}
                    </td>
                    <td>
                        <a href="{{ url_for('delete_voter', voter_id=v['id']) }}">
                            <button class="inline-btn">Delete</button>
                        </a>
                    </td>
                </tr>
                {% endfor %}
            </table>
        {% else %}
            <p>No voters found.</p>
        {% endif %}
    </div>

    <div class="card">
        <h3>Election Controls</h3>
        <a href="{{ url_for('results') }}"><button>View Results</button></a>
        <a href="{{ url_for('reset_election') }}"><button>Reset Election</button></a>
    </div>
    """
    return render_page(
        "Admin Dashboard",
        body,
        candidates=candidates,
        voters=voters,
        total_voters=total_voters,
        voted_count=voted_count
    )


@app.route("/admin/add_candidate", methods=["POST"])
@admin_required
def add_candidate():
    name = request.form.get("name", "").strip()
    party = request.form.get("party", "").strip()

    if not name or not party:
        flash("Candidate name and party are required.")
        return redirect(url_for("admin_dashboard"))

    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO candidates (name, party, votes) VALUES (?, ?, ?)", (name, party, 0))
    conn.commit()
    conn.close()

    flash("Candidate added successfully.")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/add_voter", methods=["POST"])
@admin_required
def add_voter():
    custom_voter_id = request.form.get("voter_id", "").strip().upper()
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "").strip()

    if not name or not email or not password:
        flash("Name, email, and password are required.")
        return redirect(url_for("admin_dashboard"))

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE email = ?", (email,))
    email_exists = cur.fetchone()
    if email_exists:
        conn.close()
        flash("Email already exists.")
        return redirect(url_for("admin_dashboard"))

    if custom_voter_id:
        cur.execute("SELECT id FROM users WHERE voter_id = ?", (custom_voter_id,))
        voter_exists = cur.fetchone()
        if voter_exists:
            conn.close()
            flash("This Voter ID already exists.")
            return redirect(url_for("admin_dashboard"))
        voter_id = custom_voter_id
    else:
        voter_id = generate_voter_id(conn)

    cur.execute("""
        INSERT INTO users (voter_id, name, email, password, is_admin, has_voted)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        voter_id,
        name,
        email,
        generate_password_hash(password),
        0,
        0
    ))

    conn.commit()
    conn.close()

    flash(f"Voter added successfully. Voter ID: {voter_id}")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/delete_candidate/<int:candidate_id>")
@admin_required
def delete_candidate(candidate_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM candidates WHERE id = ?", (candidate_id,))
    conn.commit()
    conn.close()

    flash("Candidate deleted successfully.")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/delete_voter/<int:voter_id>")
@admin_required
def delete_voter(voter_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE id = ? AND is_admin = 0", (voter_id,))
    voter = cur.fetchone()

    if not voter:
        conn.close()
        flash("Voter not found.")
        return redirect(url_for("admin_dashboard"))

    cur.execute("DELETE FROM users WHERE id = ?", (voter_id,))
    conn.commit()
    conn.close()

    flash("Voter deleted successfully.")
    return redirect(url_for("admin_dashboard"))


@app.route("/admin/reset")
@admin_required
def reset_election():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("UPDATE candidates SET votes = 0")
    cur.execute("UPDATE users SET has_voted = 0 WHERE is_admin = 0")

    conn.commit()
    conn.close()

    flash("Election reset successfully.")
    return redirect(url_for("admin_dashboard"))


# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)