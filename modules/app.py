from flask import Flask

# Flask app
app = Flask(__name__)

# importar rutas
from . import routes
from . import errorhandler
