import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class DailyMenu:
    date: datetime.datetime
    day: str
    food: List[str]

    def __post_init__(self):
        self.date = datetime.datetime.strptime(self.date, '%d/%m/%Y')
