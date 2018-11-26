from app.services import portal_service


def news_item(date):
    return portal_service.news_item(date)


def news(cod):
    return portal_service.news(cod)
