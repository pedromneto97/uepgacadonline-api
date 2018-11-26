import requests

from app import endpoints
from app.parsers import ru_parser


def weekly_menu(data):
    params = {
        "data": "prox" if data["next"] != None else "hj",
        "tp_refeicao": data["shift"],
        "unidade": "1-Restaurante Universitário Campus Central" if data[
                                                                       "campus"] == "central" else "2-Restaurante Universitário Campus Uvaranas"
    }

    menu_page = requests.post(
        endpoints.ru.menu,
        params
    )

    menu = ru_parser.parse_menu(menu_page)

    return menu


