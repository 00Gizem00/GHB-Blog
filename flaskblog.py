from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3
from flask import g

app = Flask(__name__, '/assets', 'assets')
cors = CORS(app)

DATABASE = 'blog.db'


@app.route('/')
@app.route('/index')
def index():
    conn = sqlite3.connect('blog.db')
    db = conn.cursor()
    cur = db.execute('SELECT * FROM blogs')
    rows = cur.fetchall()

    posts_data = []
    for row in rows:
        posts_data.append({"id": row[0], "title": row[1], "content": row[2]})
    conn.close()
    return render_template('index.html', msg='Clean Blog', rows=posts_data)

@app.route('/base')
def home():
    return render_template('base.html', msg='Clean Blog')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/post2')
def post2():
    conn = sqlite3.connect('blog.db')
    db = conn.cursor()
    cur = db.execute('SELECT * FROM blogs')
    rows = cur.fetchall()

    posts_data = []
    for row in rows:
        posts_data.append({"id": row[0], "title": row[1], "content": row[2]})
    conn.close()
    return render_template('post2.html', rows=posts_data)

@app.route('/post/<int:id>')
def detay(id):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM blogs WHERE id = ?', (id,))
    result = cursor.fetchone()


    posts_data = ({"id": result[0], "title": result[1], "content": result[2]})

    conn.close()
    return render_template('postdetay.html', post=posts_data)



@app.route('/contact')
def contact():
    return render_template('contact.html')











if __name__== "__main__":
    app.run()