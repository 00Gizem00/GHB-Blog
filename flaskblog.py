from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__, '/assets', 'assets')
cors = CORS(app)


@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')

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
    with sqlite3.connect('blog.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM blogs")
        con.commit()
        return render_template('post2.html', blogs=cur.fetchall())



@app.route('/contact')
def contact():
    return render_template('contact.html')











if __name__== "__main__":
    app.run()