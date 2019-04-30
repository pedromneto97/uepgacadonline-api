from dataclasses import dataclass


@dataclass
class Discipline:
    cod: str
    content: str
    name: str
    className: str
    year: int
    plannedClasses: int
    givenClasses: int
    absences: int
    grade1: float
    grade2: float
    gradeE: float
    mean: float
    frequency: int
    status: str

    def __post_init__(self):
        if type(self.absences) is str:
            self.absences = int(self.absences)

        if type(self.frequency) is str:
            self.frequency = int(self.frequency)

        if type(self.plannedClasses) is str:
            self.plannedClasses = int(self.plannedClasses)

        if type(self.givenClasses) is str:
            self.givenClasses = int(self.givenClasses)

        if type(self.grade1) is str:
            if self.grade1 == "":
                self.grade1 = None
            else:
                self.grade1 = float(self.grade1)

        if type(self.grade2) is str:
            if self.grade2 == "":
                self.grade2 = None
            else:
                self.grade2 = float(self.grade2)

        if type(self.gradeE) is str:
            if self.gradeE == "":
                self.gradeE = None
            else:
                self.gradeE = float(self.gradeE)
