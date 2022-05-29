from .app import app
from flask import render_template



@app.route('/bs')
def index_bs():
    return render_template('bs/index.html')
