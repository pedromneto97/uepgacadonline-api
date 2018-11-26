import datetime
from flask import Blueprint, request, make_response

from utils.response import success, error

from app.repositories import portal_repository

portal_blueprint = Blueprint("portal", __name__, url_prefix="/portal")


@portal_blueprint.route("/newsitem", methods=["GET"])
def news_item():
    date = request.args.get("date")
    date = datetime.datetime.strptime(date, '%d/%m/%Y')

    news = portal_repository.news_item(date)

    return success(
        message="Noticias retornadas com sucesso",
        news=news
    )


@portal_blueprint.route("/news", methods=["GET"])
def news():
    cod = request.args.get("cod")

    news = portal_repository.news(cod)

    return success(
        message="Noticias retornadas com sucesso",
        news=news
    )
