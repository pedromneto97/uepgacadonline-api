from bs4 import BeautifulSoup

from models.event import Event


def parse_home(eventos_page):
    events = []
    for e in BeautifulSoup(eventos_page.content, features="lxml").find_all("div", {"class": "card shadow"}):
        a = e.find("a", href=True)
        href = a["href"][a["href"].rfind('/') + 1:]
        events.append(Event(
            a.text,
            href,
            e.find("strong").text
        ).__dict__)
    return events
