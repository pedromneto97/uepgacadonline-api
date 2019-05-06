import datetime
from flask import Blueprint, request, make_response

from utils.response import success, error

from app.repositories import portal_repository

portal_blueprint = Blueprint("portal", __name__, url_prefix="/portal")


@portal_blueprint.route('/featured', methods=["GET"])
def featured():
    _featured = portal_repository.featured()

    return success(
        message="Destaques retornados com sucesso",
        featured=_featured
    )


@portal_blueprint.route("/newsitem", methods=["GET"])
def news_item():
    date = request.args.get("date")
    date = datetime.datetime.strptime(date, '%d/%m/%Y')

    _news = portal_repository.news_item(date)

    return success(
        message="Noticias retornadas com sucesso",
        daily_news=_news
    )


@portal_blueprint.route("/newsitemsweekly", methods=["GET"])
def news_items_weekly():
    date = request.args.get("date")
    date = datetime.datetime.strptime(date, '%d/%m/%Y')

    _news = portal_repository.news_items_weekly(date)

    return success(
        message="Noticias retornadas com sucesso",
        weekly_news=_news
    )


@portal_blueprint.route("/news", methods=["GET"])
def news():
    cod = request.args.get("cod")

    _news = portal_repository.news(cod)

    return success(
        message="Noticias retornadas com sucesso",
        news=_news
    )
