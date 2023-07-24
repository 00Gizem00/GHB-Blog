# sqlite db helper
import sqlite3
from flask import g


DATABASE = 'blog.db'

# Connect to database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE) # Create database if not exist
    return db

def get_posts():
    conn = get_db()
    posts = conn.execute('SELECT * FROM blogs').fetchall()
    conn.close()
    return posts

