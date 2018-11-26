from app.services import portal_service


def news(date):
    return portal_service.news(date)
