from flask import Blueprint

from repositories import eventos_repository
from utils.response import success

eventos_blueprint = Blueprint("eventos", __name__, url_prefix="/eventos")


@eventos_blueprint.route('/home', methods=["GET"])
def home():
    _home = eventos_repository.home()

    return success(message="Eventos retornados com sucesso", home=_home)
