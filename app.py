from flask import Flask
app = Flask(__name__)


if __name__=='__main__':
    # importar rutas
    from modules import routes
    from modules import errorhandler

    # Ejecutar servidor
    app.run(debug=True)
