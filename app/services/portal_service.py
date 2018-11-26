import requests

from app import endpoints

from app.parsers.portal_parser import parse_news


def news(date):
    params = {
        "ano": date.year,
        "mes": date.month
    }

    news_page = requests.post(
        endpoints.portal.news,
        params
    )

    group = parse_news(news_page)

    return group["news"]
