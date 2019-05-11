from samples import ru_sample
from services import ru_service


def weekly_menu(campus, shift, next, sample):
    data = {
        "campus": campus,
        "shift": shift,
        "next": next
    }

    return ru_sample.weekly_menu_sample() if sample else ru_service.weekly_menu(data)
