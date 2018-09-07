import json


class Discipline:
    def __init__(
        self,
        cod,
        name,
        className,
        year,
        absences,
        grade1,
        grade2,
        gradeE,
        mean,
        frequency,
        status,
    ):
        self.cod = cod
        self.name = name
        self.className = className
        self.year = year
        self.absences = absences
        self.grade1 = grade1
        self.grade2 = grade2
        self.gradeE = gradeE
        self.mean = mean
        self.frequency = frequency
        self.status = status
