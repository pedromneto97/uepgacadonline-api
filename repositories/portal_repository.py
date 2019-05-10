from services import portal_service


def featured():
    return portal_service.featured()


def daily_news_item(date):
    return portal_service.daily_news_item(date)


def weekly_news_items(date):
    return portal_service.weekly_news_items(date)


def news_items(initial_date, final_date):
    return portal_service.news_items(initial_date, final_date)


def news(cod):
    return portal_service.news(cod)
