from flask import Flask

from blueprints.acadonline_blueprint import acadonline_blueprint
from blueprints.eventos_blueprint import eventos_blueprint
from blueprints.pergamum_blueprint import pergamum_blueprint
from blueprints.ru_blueprint import ru_blueprint
from blueprints.portal_blueprint import portal_blueprint
from cache import cache

app = Flask(__name__)
cache.init_app(app)


@app.route("/", methods=["GET"])
def index():
    return "<h1>uepg-acadonline api</h1>"


app.register_blueprint(acadonline_blueprint)
app.register_blueprint(pergamum_blueprint)
app.register_blueprint(ru_blueprint)
app.register_blueprint(portal_blueprint)
app.register_blueprint(eventos_blueprint)
