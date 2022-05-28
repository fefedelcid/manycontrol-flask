from flask import Flask
from os.path import abspath

template_dir = abspath('../templates')
print(template_dir)
app = Flask(__name__, template_folder=template_dir)

from . import routes
