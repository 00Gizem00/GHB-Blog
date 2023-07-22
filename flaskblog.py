from flask import Flask, jsonify, request, render_template, redirect
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
        posts_data.append({"id": row[0], "title": row[1], "subtitle":row[2], "content": row[3], "created_on": row[4]})
    conn.close()
    return render_template('index.html', msg='Clean Blog', rows=posts_data)

@app.route('/base')
def home():
    return render_template('base.html', msg='ALOOOOOO')

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
        posts_data.append({"id": row[0], "title": row[1], "subtitle":row[2], "content": row[3], "created_on": row[4]})
    conn.close()
    return render_template('post2.html', rows=posts_data)

@app.route('/post/<int:id>')
def detay(id):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, subtitle, content, created_on FROM blogs WHERE id = ?', (id,))
    result = cursor.fetchone()


    posts_data = ({"id": result[0], "title": result[1], "subtitle":result[2], "content": result[3], "created_on": result[4]})

    conn.close()
    return render_template('postdetay.html', post=posts_data)





@app.route('/contact')
def contact():
    return render_template('contact.html')








@app.route('/editor')
def list_posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title FROM blogs') 
    rows = cursor.fetchall()

    posts_data = [{"id": row[0], "title": row[1]} for row in rows]
    conn.close()
    return render_template('adminpanel.html', posts_data=posts_data) 



@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    subtitle = request.form['subtitle']
    content = request.form['content']
    created_on = request.form['created_on']

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO blogs (title, subtitle, content, created_on) VALUES (?, ?, ?, ?)', (title, subtitle, content, created_on))
    conn.commit()
    conn.close()

    return redirect('/editor')  


@app.route('/delete_post/<int:id>', methods=['POST'])
def delete_post(id):
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()

    
    cursor.execute('DELETE FROM blogs WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    return redirect('/editor')







if __name__== "__main__":
    app.debug = True
    app.run()