from dataclasses import dataclass
import datetime


@dataclass
class Event:
    name: str
    slug: str
    start_date: datetime.datetime

    def __post_init__(self):
        self.start_date = datetime.datetime.strptime(self.start_date, '%d/%m/%Y - %Hh%M')
