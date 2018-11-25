import requests
from bs4 import BeautifulSoup
import re

from app import endpoints
from app.models.weekly_menu import WeeklyMenu


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

    menu = _parse_menu(menu_page)

    return menu


def _parse_menu(menu_page):
    day_regex = re.compile('.*dia\d.*')

    menu_raw = [
        [
            value.find("div", "dia_extenso").text,
            value.find("div", "dia_semana_extenso").text,
            [cell.text for cell in value("li")]
        ]
        for value in BeautifulSoup(menu_page.content, features="lxml").find_all("div", {"class": day_regex})
    ]
    menu = WeeklyMenu(menu_raw).__dict__

    return menu
