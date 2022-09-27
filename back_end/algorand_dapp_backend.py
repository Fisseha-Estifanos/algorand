from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'Hello, World! This is the home page'
