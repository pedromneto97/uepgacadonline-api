from bs4 import BeautifulSoup

from app.models.group_news import GroupNews
from app.models.news import News


def parse_news(news_page):
    news_raw = [
        [
            value.find("div", "data").text,
            [
                News(
                    p.find("a")['href'],
                    p.find("span", "hora").text,
                    p.find("a").text
                ).__dict__ for p in value.find_all("p")
            ]
        ]
        for value in BeautifulSoup(news_page.content, features="lxml").find_all("div", {"class": "chamada"})[1:]
    ]
    news = GroupNews(news_raw).__dict__

    return news
