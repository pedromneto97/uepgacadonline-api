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


def get_grades(token):
    return acadonline_service.get_grades(token)


def get_grades_with_info(token):
    grades = acadonline_service.get_grades(token)

    general_mean = 0
    general_absences = 0
    general_frequency = 0

    total_grades = len(grades)
    total_valid_grades = 0

    for grade in grades:
        general_absences += grade["absences"]
        general_frequency += grade["frequency"]

        grade_mean = 0
        len_mean = 0

        grades_fields = ["grade1", "grade2", "gradeE"]

        for grade_field in grades_fields:
            if grade[grade_field] is not None:
                grade_mean += grade[grade_field]
                len_mean += 1

        if len_mean == 0:
            continue

        grade_mean = grade_mean / len_mean if len_mean > 0 else 0
        general_mean += grade_mean

        total_valid_grades += 1

    general_mean = general_mean / total_valid_grades if total_valid_grades > 0 else 0
    general_frequency = general_frequency / total_grades if total_grades > 0 else 0

    return grades, general_mean, general_absences, general_frequency


def get_additional_activities(token):
    return acadonline_service.get_additional_activities(token)
