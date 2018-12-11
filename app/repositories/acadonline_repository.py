from app.services import acadonline_service


def authenticate(login, password):
    data = {"login": login, "password": password}

    return acadonline_service.authenticate(data)


def get_perfil(token):
    return acadonline_service.get_perfil(token)


def set_perfil(token, data):
    return acadonline_service.set_perfil(token, data)


def set_password(token, data):
    return acadonline_service.set_password(token, data)


def remember_password(token):
    return acadonline_service.remember_password(token)


def get_grade(token):
    grades = {
        "disciplines": acadonline_service.get_grade(token)
    }

    return grades


def get_grade_with_info(token):
    disciplines = acadonline_service.get_grade(token)

    general_mean = 0
    general_absences = 0
    general_frequency = 0

    total_disciplines = len(disciplines)
    total_valid_disciplines = 0

    for discipline in disciplines:
        general_absences += discipline["absences"]
        general_frequency += discipline["frequency"]

        discipline_mean = 0
        len_mean = 0

        discipline_grade_fields = ["grade1", "grade2", "gradeE"]

        for discipline_grade_field in discipline_grade_fields:
            if discipline[discipline_grade_field] is not None:
                discipline_mean += discipline[discipline_grade_field]
                len_mean += 1

        if len_mean == 0:
            continue

        discipline_mean = discipline_mean / len_mean if len_mean > 0 else 0
        general_mean += discipline_mean

        total_valid_disciplines += 1

    general_mean = general_mean / total_valid_disciplines if total_valid_disciplines > 0 else 0
    general_frequency = general_frequency / total_disciplines if total_disciplines > 0 else 0

    grades = {
        "disciplines": disciplines,
        "generalAbsences": general_absences,
        "generalFrequency": general_frequency,
        "generalMean": general_mean
    }

    return grades

def get_disciplines(token):
    disciplines = acadonline_service.get_disciplines(token)

    return disciplines



def get_additional_activities(token):
    return acadonline_service.get_additional_activities(token)
