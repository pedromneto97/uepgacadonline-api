from app.services import acadonline_service


def authenticate(data):
    return acadonline_service.authenticate(data)


def get_perfil(token):
    return acadonline_service.get_perfil(token)


def set_perfil(token, data):
    return acadonline_service.set_perfil(token, data)
