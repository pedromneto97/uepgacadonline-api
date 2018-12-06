from app.services import pergamum_service


def authenticate(login, password):
    return pergamum_service.authenticate(login, password)


def home():
    return pergamum_service.home()


def search():
    return pergamum_service.search()
