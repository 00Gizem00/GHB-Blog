# sqlite db helper
import sqlite3


def get_db_connection():
    conn = sqlite3.connect('blog.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM blogs').fetchall()
    conn.close()
    return posts

