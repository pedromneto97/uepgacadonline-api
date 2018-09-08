from dataclasses import dataclass


@dataclass
class Discipline:
    cod: str
    name: str
    className: str
    year: str
    absences: str
    grade1: str
    grade2: str
    gradeE: str
    mean: str
    frequency: str
    status: str
