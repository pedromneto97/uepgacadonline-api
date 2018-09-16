from flask import Flask

from app.acadonline import acadonline
from app.pergamum import pergamum

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>uepg-acadonline api</h1>"


app.register_blueprint(acadonline)
app.register_blueprint(pergamum)
