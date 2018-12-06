import requests

from app import endpoints
from bs4 import BeautifulSoup


def authenticate(login, password):
    auth = requests.request(
        "GET",
        "https://sistemas.uepg.br/pergamum///biblioteca/index.php?rs=ajax_valida_acesso_novo&rst=&rsargs[]={login}&rsargs[]={password}".format(
            login=login, password=password)
    )

    token = _get_cookies(auth)

    headers = {"cookie": f"PHPSESSID={token};"}
    home_page = requests.get(endpoints.pergamum.home, headers=headers)

    valid = len(BeautifulSoup(home_page.content, features="lxml").find_all("div", {"id": "div_logout"})) > 0

    return token if valid else None


def home():
    pass


def search():
    pass


def _get_cookies(response):
    headers_raw = dict((key, value) for key, value in response.cookies.items())

    return headers_raw["PHPSESSID"]
