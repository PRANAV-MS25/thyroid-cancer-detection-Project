from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'thyroid_secure_secret_key'  # Required for session handling

DATABASE = 'thyroiddetect.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns by name like a dictionary
    return conn

# Ensure database tables exist on startup
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        with open('database/schema.sql', 'r') as f:
            conn.executescript(f.read())
        conn.close()
        print("Database initialized successfully.")

# ----------------- ROUTING -----------------

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='scrypt')
        
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)',
                (username, email, hashed_password)
            )
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username or Email already exists!', 'danger')
        finally:
            conn.close()
            
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    scans = conn.execute(
        'SELECT * FROM scan_records WHERE user_id = ? ORDER BY scanned_at DESC',
        (session['user_id'],)
    ).fetchall()
    conn.close()
    
    return render_template('dashboard.html', scans=scans)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Processing routes will be expanded when we hook up model scripts
    return render_template('upload.html')

@app.route('/report/<int:scan_id>')
def report(scan_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    scan = conn.execute(
        'SELECT * FROM scan_records WHERE id = ? AND user_id = ?', 
        (scan_id, session['user_id'])
    ).fetchone()
    conn.close()
    
    if not scan:
        flash('Scan record not found.', 'danger')
        return redirect(url_for('dashboard'))
        
    return render_template('report.html', scan=scan)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
