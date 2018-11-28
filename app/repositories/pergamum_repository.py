from app.services import pergamum_service


def authenticate():
    return pergamum_service.authenticate()


def home():
    return pergamum_service.home()


def search():
    return pergamum_service.search()
