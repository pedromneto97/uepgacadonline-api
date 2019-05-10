from bs4 import BeautifulSoup

from models.featured import Featured
from models.group_news import GroupNews
from models.item_news import ItemNews
from models.news import News


def parse_featured(featured_page):
    image_prefix = "https://portal.uepg.br/"

    try:
        featured = [
            Featured(
                image_prefix + value.find("a").find("img")['src'],
                value.find("a")['href']
            ).__dict__
            for value in
            BeautifulSoup(featured_page.content, features="lxml").find("ul", {"id": "slider"}).find_all("li")
        ]
    except:
        featured = None

    return featured


def parse_news_item(news_page, date):
    try:
        news_raw = [
            [
                value.find("div", "data").text,
                [
                    ItemNews(
                        p.find("a")['href'],
                        p.find("span", "hora").text,
                        p.find("a").text
                    ).__dict__ for p in value.find_all("p")
                ]
            ]
            for value in BeautifulSoup(news_page.content, features="lxml").find_all("div", {"class": "chamada"})[1:]
        ]
        news = GroupNews(news_raw).__dict__
        news = [new for new in news["news"] if new["date"] == date][0]
    except:
        news = None

    return news


def parse_news_items_weekly(news_items_weekly_page, date):
    try:
        news_raw = [
            [
                value.find("div", "data").text,
                [
                    ItemNews(
                        p.find("a")['href'],
                        p.find("span", "hora").text,
                        p.find("a").text
                    ).__dict__ for p in value.find_all("p")
                ]
            ]
            for value in
            BeautifulSoup(news_items_weekly_page.content, features="lxml").find_all("div", {"class": "chamada"})[1:]
        ]
        news = GroupNews(news_raw).__dict__
        news = [new for new in news["news"]]
    except:
        news = None

    return news


def search_content(s):
    begin = s.find('<p align="justify"></p>')
    end = s.find('\n</div\r\n<p>&nbsp;</p>')

    return s[begin:end - 6]


def parse_news(news_page):
    # try:
    news_raw = BeautifulSoup(news_page.content, features="lxml").find("div", "noticia")

    print(news_raw.find_all("em"))

    state = len(news_raw.find_all("em"))

    if state == 1:
        news = News(
            news_raw.find("h1", "noticia").text,
            news_raw.find("h2").text if news_raw.find("h2") else "",
            news_raw.find("em").text[4:],
            search_content(str(news_raw)),
            news_raw.find("strong").text,
        ).__dict__
    else:
        news = News(
            news_raw.find("h1", "noticia").text,
            news_raw.find("h2").text if news_raw.find("h2") else "",
            news_raw.find_all("em")[1].text[4:],
            search_content(str(news_raw)),
            news_raw.find("strong").text,
            news_raw.find("em").text[14:]
        ).__dict__
    # except:
    #     news = None

    return news
