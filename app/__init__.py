from flask import Flask

from app.acadonline import acadonline

app = Flask(__name__)

app.register_blueprint(acadonline)
