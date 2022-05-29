from .app import app
from flask import jsonify, render_template

@app.errorhandler(405) # Method not allowed
def errorhandler(err):
    return jsonify({
    'code':err.code,
    'description':err.description
    })


@app.errorhandler(404) # Page not found
def not_found(err):
    return render_template('errors/404.html')
