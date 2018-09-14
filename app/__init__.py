from flask import Flask

from app.acadonline import acadonline
from app.pergamum import pergamum

app = Flask(__name__)

app.register_blueprint(acadonline)
app.register_blueprint(pergamum)
