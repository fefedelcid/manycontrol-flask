from flask import Flask

# Flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# importar rutas
from . import routes
from . import errorhandler
