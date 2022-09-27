from flask import Flask, render_template
import sys, os
import sqlite3
from dotenv import load_dotenv
load_dotenv()
sys.path.append('..')
sys.path.append('.')
sys.path.insert(1, '../scripts/')
wallet_1 = os.getenv('my_address_w1')

#from transaction_helpers import get_records
import defaults as defs

app = Flask(__name__)


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


@app.route('/certificates')
def certificates():
    return render_template('certificates.html')


@app.route('/transactions')
def transactions():
    return render_template('transactions.html')


@app.route('/transactions/display_balance')
def display_balance():
    print(f"loading the account: {wallet_1}'ns balance")
    account_balance = 888
    return render_template('transactions.html', balance=account_balance)
