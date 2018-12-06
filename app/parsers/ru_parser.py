import re

from bs4 import BeautifulSoup

from app.models.weekly_menu import WeeklyMenu


def parse_menu(menu_page):
    try:
        day_regex = re.compile('.*dia\d.*')

        menu_raw = [
            [
                value.find("div", "dia_extenso").text,
                value.find("div", "dia_semana_extenso").text,
                [cell.text for cell in value("li")]
            ]
            for value in BeautifulSoup(menu_page.content, features="lxml").find_all("div", {"class": day_regex})
        ]
        menu = WeeklyMenu(menu_raw).__dict__["daily_menus"]
    except:
        menu = None

    return menu
