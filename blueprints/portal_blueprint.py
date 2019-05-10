import datetime
from flask import Blueprint, request

from utils.date import now_formatted_subtracted_weeks
from utils.response import success

from repositories import portal_repository

portal_blueprint = Blueprint("portal", __name__, url_prefix="/portal")


@portal_blueprint.route('/featured', methods=["GET"])
def featured():
    _featured = portal_repository.featured()

    return success(message="Destaques retornados com sucesso", featured=_featured)


@portal_blueprint.route("/daily_news_items", methods=["GET"])
def daily_news_items():
    date = request.args.get("date")
    date = datetime.datetime.strptime(date, '%d/%m/%Y')

    _daily_news_items = portal_repository.daily_news_item(date)

    return success(message="Noticias retornadas com sucesso", daily_news=_daily_news_items)


@portal_blueprint.route("/weekly_news_items", methods=["GET"])
def weekly_news_items():
    date = request.args.get("date")
    date = datetime.datetime.strptime(date, '%d/%m/%Y')

    _weekly_news_items = portal_repository.weekly_news_items(date)

    return success(message="Noticias retornadas com sucesso", weekly_news=_weekly_news_items)


@portal_blueprint.route("/new_items", methods=["GET"])
def news_items():
    page = request.args.get("page", 1)

    initial_date = now_formatted_subtracted_weeks(page * 2)
    final_date = now_formatted_subtracted_weeks((page - 1) * 2)

    _news_items = portal_repository.news_items(initial_date, final_date)

    return success(message="Noticias retornadas com sucesso", weekly_news=_news_items)


@portal_blueprint.route("/news_item", methods=["GET"])
def news_item():
    cod = request.args.get("cod")

    _news_item = portal_repository.news(cod)

    return success(message="Noticias retornadas com sucesso", news=_news_item)
