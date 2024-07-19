import sqlite3
from datetime import datetime


def connectDB():
    conn = sqlite3.connect('database.db')# if not ,create
    return conn

def close(conn):
    conn.close()

def commit_close(conn):
    conn.commit()
    conn.close()

def create_login_tables():
    conn  = connectDB()
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS logins
                 (username TEXT, timestamp TEXT)''')
    commit_close(conn)

def create_code_tables():
    conn  = connectDB()
    c = conn.cursor()
    c.execute(f'''CREATE TABLE IF NOT EXISTS codes
                 (filename TEXT, similarity REAL)''')
    commit_close(conn)


def save_login():
    conn = connectDB()
    c = conn.cursor()
    c.execute("INSERT INTO logins VALUES (?, ?)", ("admin", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_last_login():
    conn = connectDB()
    c = conn.cursor()
    c.execute("SELECT timestamp FROM logins ORDER BY timestamp DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result[0] if result else "No previous login"


def create_all_tables():
    create_login_tables()
    create_code_tables()
    
def sys_show_history():
    conn = connectDB()
    c = conn.cursor()
    c.execute("SELECT * FROM codes")
    result = c.fetchall()
    conn.close()
    return result

def get_history():
    conn = connectDB()
    c = conn.cursor()
    c.execute("SELECT * FROM codes")
    result = c.fetchall()
    conn.close()
    return result