from flask import Blueprint, request, make_response

from app.repositories import ru_repository
from app.samples import ru_sample

from utils.response import success, error

ru_blueprint = Blueprint("ru", __name__, url_prefix="/ru")


@ru_blueprint.route("/menu", methods=["GET"])
def menu():
    campus = request.args.get("campus")
    shift = request.args.get("shift")
    next = request.args.get("next")
    sample = request.args.get("sample")

    weekly_menu = ru_sample.weekly_menu_sample() if sample else ru_repository.weekly_menu(campus, shift, next)

    return success(message="Cardápio retornado com sucesso", weekly_menu=weekly_menu)
