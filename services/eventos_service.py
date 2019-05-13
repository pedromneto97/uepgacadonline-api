import requests

import endpoints
from parsers.eventos_parser import parse_home


def home():
    home_page = requests.get(endpoints.eventos.home)
    _home = parse_home(home_page)

    return _home
