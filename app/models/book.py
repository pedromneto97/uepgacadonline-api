from dataclasses import dataclass


@dataclass
class Book:
    name: str
    desc: str
    number: str
    collection: str
