from app.services import acadonline_service


def authenticate(data):
    return acadonline_service.authenticate(data)


def get_perfil(token):
    return acadonline_service.get_perfil(token)


def set_perfil(token, data):
    return acadonline_service.set_perfil(token, data)


def set_password(token, data):
    return acadonline_service.set_password(token, data)


def remember_password(token):
    return acadonline_service.remember_password(token)


def get_grades(token):
    return acadonline_service.get_grades(token)


def get_additional_activities(token):
    return acadonline_service.get_additional_activities(token)
