import requests

from app import endpoints
from bs4 import BeautifulSoup

from app.models.loans import Loans


def authenticate(login, password):
    auth = requests.request(
        "GET",
        endpoints.pergamum.auth.format(login=login, password=password)
    )

    token = _get_cookies(auth)
    home_page = requests.get(
        endpoints.pergamum.home,
        headers=_get_headers(token)
    )

    valid = len(BeautifulSoup(home_page.content, features="lxml").find_all("div", {"id": "div_logout"})) > 0

    if (valid):
        requests.get(
            endpoints.pergamum.validate,
            headers=_get_headers(token)
        )

        return token

    else:
        return None


def books(token):
    books_page = requests.get(
        endpoints.pergamum.books,
        headers=_get_headers(token)
    )

    books_raw = [
        [
            row.find_all("td")[1].find("a").text.strip(),
            row.find_all("td")[1].find("a")["title"],
            row.find_all("td")[1].find("a")["href"],
            row.find_all("td")[2].text,
            row.find_all("td")[4].find("center").find("input")["onclick"]
        ]
        for row in BeautifulSoup(books_page.content, features="lxml") \
                       .find("div", {"class": "c1"}) \
                       .find("table").find_all("tr")[1:]

    ]

    books = Loans(books_raw).__dict__

    return books["loans"]


def renew(token, book):
    requests.get(
        endpoints.pergamum.renew.format(book=book),
        headers=_get_headers(token)
    )

    return None


def home():
    pass


def search():
    pass


def _get_cookies(response):
    headers_raw = dict((key, value) for key, value in response.cookies.items())

    return headers_raw["PHPSESSID"]


def _get_headers(token):
    return {"cookie": f"PHPSESSID={token};"}
