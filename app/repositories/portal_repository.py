from app.services import portal_service


def featured():
    return portal_service.featured()


def news_item(date):
    return portal_service.news_item(date)


def news_items_weekly(date):
    return portal_service.news_item(date)


def news(cod):
    return portal_service.news(cod)
