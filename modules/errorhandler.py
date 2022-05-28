from .app import app
from flask import jsonify

@app.errorhandler(405) # Method not allowed
@app.errorhandler(404) # Page not found
def errorhandler(err):
    return jsonify({
    'code':err.code,
    'description':err.description
    })
