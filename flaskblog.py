from flask import Flask, jsonify, request, render_template, redirect, g
from flask_cors import CORS
import sqlite3
from flask import g
from db_helper import get_all_posts, get_post_by_slug


app = Flask(__name__, '/assets', 'assets')
cors = CORS(app)

DATABASE = 'blog.db'


@app.route('/')
@app.route('/<slug>')
def detay(slug = None, msg = "GHB Blog"):
    if slug:
        post = get_post_by_slug(slug)

        if post == None:
            return render_template('404.html', msg = "404-Sayfa Bulunamadi"), 404
        
        return render_template('postdetay.html', post=post)
    else:
        return render_template('index.html' , posts = get_all_posts(), msg = msg)

@app.route('/about')
def about():
    return render_template('about.html')


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
    slug = request.form['slug']
    content = request.form['content']
    created_on = request.form['created_on']

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO blogs (title, subtitle, slug, content, created_on) VALUES (?, ?, ?, ?, ?)', (title, subtitle, slug, content, created_on))
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