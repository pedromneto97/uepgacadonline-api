from bs4 import BeautifulSoup

from app.models.loans import Loans


def parse_books(books_page):
    books_raw = [
        [
            row.find_all("td")[1].find("a").text.strip(),
            row.find_all("td")[1].find("a")["title"],
            row.find_all("td")[1].find("a")["href"],
            row.find_all("td")[2].text,
            row.find_all("td")[3].text[0],
            row.find_all("td")[3].text[-1],
            row.find_all("td")[4].find("center").find("input")["onclick"][19:25],
            row.find_all("td")[5].text
        ]
        for row in BeautifulSoup(books_page.content, features="lxml") \
                       .find("div", {"class": "c1"}) \
                       .find("table").find_all("tr")[1:]

    ]
    books = Loans(books_raw).__dict__["loans"]

    return books
