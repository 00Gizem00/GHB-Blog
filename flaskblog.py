from flask import Flask, jsonify, request, render_template, redirect, g
from flask_cors import CORS
import sqlite3
from flask import g
from db_helper import get_all_posts, get_post_by_slug


app = Flask(__name__, '/assets', 'assets')
cors = CORS(app)

DATABASE = 'blog.db'

# @app.route('//')
# def index2():
#     return get_all_posts()


@app.route('/')
@app.route('/index')
def index():
    conn = sqlite3.connect('blog.db')
    db = conn.cursor()
    cur = db.execute('SELECT * FROM blogs')
    rows = cur.fetchall()

    posts_data = []
    for row in rows:
        posts_data.append({"id": row[0], "title": row[1], "subtitle":row[2], "content": row[4], "created_on": row[5]})
    conn.close()
    return render_template('index.html', msg='Clean Blog', rows=posts_data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post2')
def post2():
    conn = sqlite3.connect('blog.db')
    db = conn.cursor()
    cur = db.execute('SELECT * FROM blogs')
    rows = cur.fetchall()

    posts_data = []
    for row in rows:
        posts_data.append({"id": row[0], "title": row[1], "subtitle":row[2], "content": row[4], "created_on": row[5]})
    conn.close()
    return render_template('post2.html', rows=posts_data)

@app.route('/post/<slug>')
def detay(slug):
    post = get_post_by_slug(slug)
    
    
    # conn = sqlite3.connect('blog.db')
    # cursor = conn.cursor()
    # cursor.execute('SELECT id, title, subtitle, content, created_on FROM blogs WHERE id = ?', (id,))
    # result = cursor.fetchone()

    if post is None:
        return render_template('404.html'), 404


    # posts_data = ({"id": result[0], "title": result[1], "subtitle":result[2], "content": result[5], "created_on": result[6]})

    # conn.close()
    return render_template('postdetay.html', post=post)

@app.route('/newpost')
def newpost():
    return render_template('addpost.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/editor')
def list_posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, title, content FROM blogs') 
    rows = cursor.fetchall()

    posts_data = [{"id": row[0], "title": row[1] , "content": row[2] } for row in rows]
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


@app.route('/posts/<int:id>/edit' , methods=['POST'])
def update_post(id):
    title = request.form['title']
    content = request.form['content']

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE blogs SET title = ?, content = ?  WHERE id = ?', (title, content, id))
    conn.commit()
    conn.close()

    return redirect('/editor')




if __name__== "__main__":
    app.debug = True
    app.run()