import requests

from app import endpoints

from app.parsers.portal_parser import parse_news


def news_item(date):
    params = {
        "ano": date.year,
        "mes": date.month
    }

    news_page = requests.post(
        endpoints.portal.news_item,
        params
    )

    group = parse_news(news_page)

    return group["news"]


def news(cod):
    params = {
        "id": cod
    }

    news_page = requests.get(
        endpoints.portal.news,
        params
    )

    print(news_page.content)

    return True

