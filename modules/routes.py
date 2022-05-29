from .app import app
from .KeyGen import get
from flask import jsonify, request, render_template


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('views/mainpage.html')


@app.route('/temp/keygen')
def get_key():
    valid_key = get()
    return render_template('views/token.html', token = valid_key)
