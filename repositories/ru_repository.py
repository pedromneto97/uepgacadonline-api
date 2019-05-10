from services import ru_service


def weekly_menu(campus, shift, next):
    data = {
        "campus": campus,
        "shift": shift,
        "next": next
    }

    return ru_service.weekly_menu(data)
