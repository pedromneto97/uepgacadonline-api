import datetime
import locale
from dataclasses import dataclass
from typing import List

from app.models.item_news import ItemNews


@dataclass
class DailyNews:
    date: datetime.datetime
    daily_news: List[ItemNews]

    def __post_init__(self):
        if type(self.date) == str:
            locale.setlocale(locale.LC_ALL, 'pt_BR')
            self.date = datetime.datetime.strptime(self.date, '%d %b %Y')
