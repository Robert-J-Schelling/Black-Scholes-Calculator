import time
from flask import Flask, redirect, url_for, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/result', methods=('GET', 'POST'))
def get_current_time():
    if request.method == 'POST':
        data = request.get_json(force=True)
        print(data)
        return data
    else:
        return "hello"
