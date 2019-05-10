from dataclasses import dataclass

import datetime

@dataclass
class Activity:
    protocol: str
    date: datetime.datetime
    hours: str
    minutes: str

    def __post_init__(self):
        self.date = datetime.datetime.strptime(self.date, '%d/%m/%Y')
