from .app import app
from ..KeyGen import get
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


@app.route('/api')
def api():
    return jsonify(get())


@app.route('/play')
def trolling():
    return render_template('views/trolling.html')
