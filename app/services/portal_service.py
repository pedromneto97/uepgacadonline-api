import requests

from app import endpoints

from app.parsers.portal_parser import parse_news_item, parse_news


def news_item(date):
    params = {
        "ano": date.year,
        "mes": date.month
    }

    news_page = requests.post(
        endpoints.portal.news_item,
        params
    )

    group = parse_news_item(news_page, date)

    return group


def news(cod):
    params = {
        "id": cod
    }

    news_page = requests.get(
        endpoints.portal.news,
        params
    )

    news = parse_news(news_page)

    return news
