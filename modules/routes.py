from .app import app
from .KeyGen import get
from flask import jsonify, request, render_template

default_response = {'message':'endpoint is not set'}

def get_request_info():
    return jsonify({
        'url': request.url,
        'method':request.method
    })


@app.route('/', methods=['GET', 'POST'])
def index():
    return get_request_info()


@app.route('/api/keygen')
def get_key():
    valid_key = get()
    return render_template('views/token.html', token = valid_key)
