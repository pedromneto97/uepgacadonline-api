from flask import Flask

from app.blueprints.acadonline_blueprint import acadonline_blueprint
from app.blueprints.pergamum_blueprint import pergamum_blueprint
from app.blueprints.ru_blueprint import ru_blueprint

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "<h1>uepg-acadonline api</h1>"


app.register_blueprint(acadonline_blueprint)
app.register_blueprint(pergamum_blueprint)
app.register_blueprint(ru_blueprint)
