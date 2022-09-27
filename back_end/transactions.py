from flask import Flask, render_template

app = Flask(__name__)


@app.route('/transactions')
def transactions():
    return render_template('transactions.html')


@app.route('/certificates')
def certificates():
    return render_template('certificates.html')


@app.route('/')
def index():
    return render_template('index.html')
