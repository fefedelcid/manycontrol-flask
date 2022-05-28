from flask import Flask
app = Flask(__name__)

# importar rutas
from . import routes
from . import errorhandler

if __name__=='__main__':
    # Ejecutar servidor
    app.run(debug=True)