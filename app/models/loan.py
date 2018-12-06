from dataclasses import dataclass

import datetime

@dataclass
class Loan:
    name: str
    title: str
    address: str
    date: str
    renew: str
