import sqlite3
import os

# Define database paths matching your root files
USERS_DB = "users.db"
REPORTS_DB = "thyroiddetect.db"

def init_db():
    """Initializes the SQLite databases and tables if they don't exist."""
    # Users Table
    conn = sqlite3.connect(USERS_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            dob TEXT,
            age TEXT,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

    # Reports Table
    conn = sqlite3.connect(REPORTS_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            age TEXT,
            gender TEXT,
            phone TEXT,
            email TEXT,
            image_path TEXT,
            prediction TEXT,
            confidence REAL,
            date_time TEXT
        )
    """)
    conn.commit()
    conn.close()

def create_user(name, dob, age, email, phone, password):
    """Registers a new user in the users database."""
    try:
        conn = sqlite3.connect(USERS_DB)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, dob, age, email, phone, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, dob, age, email, phone, password))
        conn.commit()
    except Exception as e:
        print("Error creating user:", e)
    finally:
        conn.close()

def verify_login(identifier, password):
    """Verifies user login using either email or phone and password."""
    conn = sqlite3.connect(USERS_DB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name FROM users 
        WHERE (email = ? OR phone = ?) AND password = ?
    """, (identifier, identifier, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return user[0], user[1] # returns user_id, name
    return None, None

def get_user_by_id(user_id):
    """Retrieves user profile details by ID."""
    conn = sqlite3.connect(USERS_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def save_patient_report(data):
    """Saves an AI analysis report to the database."""
    conn = sqlite3.connect(REPORTS_DB)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reports (patient_name, age, gender, phone, email, image_path, prediction, confidence, date_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["patient_name"],
        data["age"],
        data["gender"],
        data["phone"],
        data["email"],
        data["image_path"],
        data["prediction"],
        data["confidence"],
        data["date_time"]
    ))
    conn.commit()
    conn.close()

def search_reports(keyword):
    """Searches past reports by keyword (patient name or phone)."""
    conn = sqlite3.connect(REPORTS_DB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM reports 
        WHERE patient_name LIKE ? OR phone LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_user_reports(phone):
    """Fetches all reports associated with a specific user phone number."""
    conn = sqlite3.connect(REPORTS_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports WHERE phone = ?", (phone,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_user_stats(phone):
    """Calculates basic stats for user profile display."""
    conn = sqlite3.connect(REPORTS_DB)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM reports WHERE phone = ?", (phone,))
    total_scans = cursor.fetchone()[0]
    conn.close()
    return {"total_scans": total_scans}