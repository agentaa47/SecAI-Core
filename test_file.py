import os
import sqlite3
import subprocess

def run_command(user_input):
    subprocess.run(["echo", user_input], check=True)

def get_user_data(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchall()
