import datetime
from dataclasses import dataclass


@dataclass
class ItemNews:
    cod: str
    time: datetime.datetime
    title: str

    def __post_init__(self):
        self.cod = self.cod.split("?id=", 1)[1]

        if type(self.time) == str:
            self.time = datetime.datetime.strptime(self.time, '%Hh%M')
