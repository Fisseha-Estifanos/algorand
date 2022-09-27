import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/transactions')
def transactions():
    return render_template('transactions.html')


@app.route('/certificates')
def certificates():
    return render_template('certificates.html')


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/index')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)
