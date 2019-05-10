import requests

import endpoints

from parsers.portal_parser import parse_news_item, parse_news, parse_featured, parse_news_items_weekly


def featured():
    featured_page = requests.get(
        endpoints.portal.featured
    )

    featured_ = parse_featured(featured_page)

    return featured_


def daily_news_item(date):
    params = {
        "ano": date.year,
        "mes": date.month
    }

    news_page = requests.post(
        endpoints.portal.news_item,
        params,
        verify=False
    )

    group = parse_news_item(news_page, date)

    return group


def weekly_news_items(date):
    params = {
        "ano": date.year,
        "mes": date.month
    }

    news_weekly_page = requests.post(
        endpoints.portal.news_item,
        params,
        verify=False
    )

    group = parse_news_items_weekly(news_weekly_page, date)

    return group

def news_items(initial_date, final_date):
    params = {
        "ano": initial_date.year,
        "mes": final_date.month
    }

    news_weekly_page = requests.post(
        endpoints.portal.news_item,
        params,
        verify=False
    )

    group = parse_news_items_weekly(news_weekly_page, initial_date)

    return group

def news(cod):
    params = {
        "id": cod
    }

    news_page = requests.get(
        endpoints.portal.news,
        params
    )

    news_ = parse_news(news_page)

    return news_
