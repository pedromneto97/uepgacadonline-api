import datetime
import locale
from dataclasses import dataclass


@dataclass
class News:
    title: str
    subtitle: str
    author: str
    content: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __post_init__(self):
        pass
        # if type(self.date) == str:
        # locale.setlocale(locale.LC_ALL, 'pt_BR')
        # self.created_at = datetime.datetime.strptime(self.created_at, '%d %b %Y')
        # self.updated_at = datetime.datetime.strptime(self.updated_at, '%d %b %Y')
