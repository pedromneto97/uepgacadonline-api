from dataclasses import dataclass


@dataclass
class Activity:
    protocol: str
    date: str
    hours: str
    minutes: str
