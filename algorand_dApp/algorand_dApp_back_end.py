# import jsonify
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import os
import sys
import sqlite3
from dotenv import load_dotenv
sys.path.append('.')
sys.path.append('..')
sys.path.insert(1, '/scripts/')
from scripts.transaction_helpers import *
import scripts.defaults as defs

load_dotenv()
wallet_1 = os.getenv('my_address_w1')

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


"""def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
"""

@app.route('/index')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/certificates')
def certificates():
    return render_template('certificates.html')


@app.route('/transactions')
def transactions():
    return render_template('transactions.html')


@app.route('/transactions/display_balance', methods=['GET', 'POST'])
def display_balance():
    print('in get')
    account = request.form['address']
    # account = request.data
    print(f"loading the account: {account}'s balance")
    if not account:
        flash('Account address is required')
    else:
        print(f"loading the account: {account}'s balance")
        account_balance = 888
        return render_template('transactions.html',
                               balance=account_balance)
